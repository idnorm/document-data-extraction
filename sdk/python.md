# Python package

## Installation

We release our java client on publicaly available google artifact registry [https://console.cloud.google.com/artifacts/python/idnorm/us-central1/pyrepo/idnorm-ddx?project=idnorm](https://console.cloud.google.com/artifacts/python/idnorm/us-central1/pyrepo/idnorm-ddx?project=idnorm).

To install it using `pip` simply run the command
```bash
python3 -m pip install idnorm-ddx==1.6.2 --extra-index-url https://us-central1-python.pkg.dev/idnorm/pyrepo/simple/
```

To simplify dependency management, you might want to add our repo to your `pip.config` as
```toml
[global]
extra-index-url = https://us-central1-python.pkg.dev/idnorm/pyrepo/simple/
```

And you won't need to specify `--extra-index-url` when you are installing dependencies.

## Usage

Bellow is an example snippet of using `python` client in code.

We include both "blocking" and "async" example of using our client.

To run the code you will need to provide it with an image you want to process and a [license key](../license.md).

```python

import asyncio
from typing import Tuple

from idnorm_ddx import (
    ExtractionClient, ExtractionClientConfig, ExtractionClientAsync, ScanDocumentResponse,
    SexField, TextField, DateField, VisualField, ScanConfig, Mrz, Pdf417Barcode
)
import sys


def parse_args() -> Tuple[str, str]:
    if len(sys.argv) != 3:
        print(f"Usage: python {sys.argv[0]} <image_path> <license_key>", file=sys.stderr)
        sys.exit(-1)
    return sys.argv[1], sys.argv[2]

def main():
    img_path, license_key = parse_args()
    with open(img_path, 'rb') as f:
        image_bytes = f.read()

    with ExtractionClient(cfg=ExtractionClientConfig(
        license_key=license_key,
    )) as cli:
        resp = cli.scan_document(
            img_bytes=image_bytes,
            config=ScanConfig(
                # Request visual fields, not returned by default
                returnVisualFields=ScanConfig.ReturnVisualFields()
            )
        )
        print_results(resp)


async def async_main():

    img_path, license_key = parse_args()
    with open(img_path, 'rb') as f:
        image_bytes = f.read()

    async with ExtractionClientAsync(cfg=ExtractionClientConfig(
        license_key=license_key,
    )) as async_cli:
        result = await async_cli.scan_document(
            img_bytes=image_bytes,
            config=ScanConfig(
                # Request visual fields, not returned by default
                returnVisualFields=ScanConfig.ReturnVisualFields()
            )
        )
        print_results(result)

def print_results(result: ScanDocumentResponse):
    if result.status == ScanDocumentResponse.Status.STATUS_OK:
        print("Detected document quad: ")
        print(result.detection)

        print("Detected document class: ")
        print(result.classification)

        data = result.data

        print("Detected text fields: ")
        for field in data.textField:
            print(f"{TextField.Type.Name(field.type)}: {field.value}\n")

        print("Detected date fields: ")
        for field in data.dateField:
            print(f"{DateField.Type.Name(field.type)}: {field.value}")
            if field.date is not None:
                print(f" | Parsed -> Day: {field.date.day}, Month: {field.date.month}, Year: {field.date.year}\n")

        print("Detected sex field(s): ")
        for field in data.sexField:
            print(f"SEX: {field.value} | Parsed -> {SexField.Sex.Name(field.sex)}\n")

        # Stores all detected visual fields into current working dir
        print("Detected visual fields: ")
        for field in data.visualField:
            img = field.image
            with open(f"{VisualField.Type.Name(field.type)}_{field.type}.jpg", 'wb') as f:
                f.write(img)
    else:
        print(result.status)

    if result.status != ScanDocumentResponse.Status.STATUS_DOCUMENT_NOT_FOUND:
        if result.data.HasField('mrz'):
            print("Detected MRZ: ")
            print(result.data.mrz)

        if result.data.HasField('pdf417Barcode'):
            print("Detected PDF417 barcode: ")
            print(result.data.pdf417Barcode)

if __name__ == '__main__':
    main()
    asyncio.run(async_main())
```
