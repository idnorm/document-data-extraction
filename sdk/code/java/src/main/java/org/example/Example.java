package org.example;

import com.google.protobuf.ByteString;
import com.idnorm.extraction.ExtractionBlockingClient;
import proto.ddx.v1.Service;

import java.io.FileInputStream;
import java.io.IOException;

// An example of usage of the extraction client
public class Example {

    public static void main(String[] args) {

        if (args.length != 2) {
            System.err.println("Usage: <license_key> <image_path>");
            System.exit(1);
        }
        var licenseKey = args[0];
        if (licenseKey.trim().isEmpty()) {
            System.err.println("License key can't be empty");
            System.exit(1);
        }
        var imagePath = args[1];
        if (imagePath.trim().isEmpty()) {
            System.err.println("Image path can't be empty");
            System.exit(1);
        }

        var builder = ExtractionBlockingClient.builder();
        var cli = builder.setLicenseKey(licenseKey).build();

        ByteString imgData;
        try {
            imgData = ByteString.readFrom(new FileInputStream(imagePath));
        } catch (IOException e) {
            throw new RuntimeException(e);
        }

        System.out.println("Sending request...");

        // request service to return all visual fields
        var scanConfig = Service.ScanConfig.newBuilder().setReturnVisualFields(
                Service.ScanConfig.ReturnVisualFields.getDefaultInstance()
        ).build();

        var result = cli.scanDocument(imgData, scanConfig);

        if (result.getStatus() != Service.ScanDocumentResponse.Status.STATUS_DOCUMENT_NOT_FOUND) {
            System.out.println("Response status: " + result.getStatus());

            // Prints detected card quad
            System.out.println("Detected card quad:");
            System.out.println(result.getDetection());
            if (result.hasData()) {
                var data = result.getData();
                // Prints all detected text fields
                for (var field : data.getTextFieldList()) {
                    System.out.println(field.getType() + ": " + field.getValue());
                }

                // Prints all detected date fields
                for (var field : data.getDateFieldList()) {
                    System.out.printf("%s: %s", field.getType(), field.getValue());
                    if (field.hasDate()) {
                        System.out.printf("| Parsed - Day: %d, Month: %d, Year: %d", field.getDate().getDay(), field.getDate().getMonth(), field.getDate().getYear());
                    }
                    System.out.println();
                }

                // Print all detected sex fields
                for (var field : data.getSexFieldList()) {
                    System.out.printf("Sex: %s | Parsed - %s", field.getValue(), field.getSex());
                }

                // Stores all detected visual field images to current working dir
                for (var field : data.getVisualFieldList()) {
                    var img = field.getImage();
                    var filename = field.getType() + ".jpg";
                    try {
                        img.writeTo(new java.io.FileOutputStream(filename));
                    } catch (IOException e) {
                        throw new RuntimeException(e);
                    }
                }

                if (data.hasMrz()) {
                    // Prints detected MRZ
                    System.out.println("Detected MRZ:");
                    System.out.println(data.getMrz());
                }

                if (data.hasPdf417Barcode()) {
                    // Prints detected PDF417 barcode
                    System.out.println("Detected PDF417 barcode:");
                    System.out.println(data.getPdf417Barcode());
                }
            }
        } else {
            // Prints status
            System.out.println(result.getStatus());
        }

    }
}