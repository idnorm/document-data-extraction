# Java package

## Installation

We release our java client on publicaly available google artifact registry [https://console.cloud.google.com/artifacts/maven/idnorm/us-central1/mvn/com.idnorm:id-extraction](https://console.cloud.google.com/artifacts/maven/idnorm/us-central1/mvn/com.idnorm:id-extraction).

There you can see all package information.

To add it to your project you need to specify our maven repository `artifactregistry://us-central1-maven.pkg.dev/idnorm/mvn` and define out package
as your `maven` or `gradle` dependency.

Examples of both `pom.xml` and `build.gradle`.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <!-- usually project configurations... -->
    ...

    <!-- Must add our maven repository so maven knows where to find the dep -->
    <repositories>
        <repository>
            <id>google-artifact-registry</id>
            <url>artifactregistry://us-central1-maven.pkg.dev/idnorm/mvn</url>
        </repository>
    </repositories>

    <dependencies>
        <dependency>
            <groupId>com.idnorm</groupId>
            <artifactId>ddx</artifactId>
            <version>1.1.0</version>
        </dependency>
    </dependencies>
</project>
```

Grade
```groovy
repositories {
    mavenCentral()
    maven {
        url "https://us-central1-maven.pkg.dev/idnorm/mvn"
    }
}

dependencies {
    implementation 'com.idnorm:ddx:1.1.0'
}
```

## Usage

We expose different clients for different concurrency needs

- `ExtractionBlockingClient`
- `ExtractionAsnycClient`
- `ExtractionFutureClient`

to offer out-of-the-box options to use in "blocking" or "async" codebase.

Here is an example of using `ExtractionBlockingClient` to send and receive a request.
Request and response classes are the same, regardless of the selected client.

To run the code you will need to provide it with an image you want to process and a [license key](../license.md).

```java
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
```
