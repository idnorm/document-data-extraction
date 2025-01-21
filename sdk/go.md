# Golang package

## Installation

To add our golang client to your go package as a dependency simply run

`go get github.com/idnorm/id-extraction/sdk/code/go/client`

## Usage

Bellow, we provide code snippet that demonstrates how send and receive a request to document data extraction service.

To run the code you will need to provide it with an image you want to process and a [license key](../license.md).

```go
package main

import (
	"context"
	"fmt"
	"github.com/idnorm/id-extraction/sdk/code/go/client"
	v1 "github.com/idnorm/id-extraction/sdk/code/go/proto/id_extract_service/v1"

	"log"
	"os"
)

func main() {

	if len(os.Args) < 3 {
		log.Fatalf("Usage: %s <image path> <license key>", os.Args[0])
	}
	imgPath := os.Args[1]
	licenseKeyBase64 := os.Args[2]

	cli, err := client.NewClient(
		client.WithLicenseKeyBase64(licenseKeyBase64),
	)

	if err != nil {
		log.Fatalf("failed to create client: %v", err)
	}

	imgBytes, err := os.ReadFile(imgPath)

	if err != nil {
		log.Fatalf("failed to read file %s: %v", imgPath, err)
	}

	resp, err := cli.Scan(context.Background(), imgBytes, &v1.ScanConfig{
		ReturnVisualFields: &v1.ScanConfig_ReturnVisualFields{},
	})

	if err != nil {
		log.Fatal(err)
	}

	if resp.Status != v1.ScanDocumentResponse_STATUS_OK {
		log.Fatal(resp.Status)
	} else {
		if resp.Status != v1.ScanDocumentResponse_STATUS_DOCUMENT_NOT_FOUND {
			fmt.Println("Document classification")
			fmt.Println(resp.Classification)
			fmt.Println("Detection coordinates")
			fmt.Println(resp.Detection)
		}
		fmt.Println("Detected text fields: ")
		for _, field := range resp.TextField {
			fmt.Printf("%s: %s\n", field.Type, field.Value)
		}
		fmt.Println("Detected date fields: ")
		for _, field := range resp.DateField {
			fmt.Printf("%s: %s", field.Type, field.TextValue)
			if field.Date != nil {
				fmt.Printf("| Parsed -> Day: %d, Month: %d, Year: %d", field.Date.Day, field.Date.Month, field.Date.Year)
			}
			fmt.Println()
		}
		fmt.Println("Detected sex fields: ")
		for _, field := range resp.SexField {
			fmt.Printf("Sex: %s | Parsed -> %s\n", field.TextValue, field.Sex)
		}
		fmt.Println("Detected visual fields: ")
		for _, field := range resp.VisualField {
			fmt.Printf("%s: saving to %s.jpg\n", field.Type, field.Type.String())
			err = os.WriteFile(field.Type.String()+".jpg", field.Image, 0644)
			if err != nil {
				log.Fatalf("failed to write file: %v", err)
			}
		}
	}

}
```
