#!/bin/bash

# Set default endpoint if ENDPOINT is not provided
ENDPOINT=${ENDPOINT:-"http://0.0.0.0:8000"}
IDNORM_LICENSE_KEY=${IDNORM_LICENSE_KEY:-""}

if [ $# -ne 1 ]; then
  echo "Usage: $0 <image-path>"
  exit 1
fi

IMAGE_PATH="$1"

if [ ! -f "$IMAGE_PATH" ]; then
  echo "Error: File '$IMAGE_PATH' not found!"
  exit 1
fi

# Create a single temporary file
TMP_FILE=$(mktemp)

# Write JSON payload with base64-encoded image
{
  echo -n '{"imageJpeg": "'
  base64 "$IMAGE_PATH" | tr -d '\n'
  echo '"}'
} > "$TMP_FILE"

# Send the request using curl
if [ -n "$IDNORM_LICENSE_KEY" ]; then
  curl -X POST "$ENDPOINT/api/v1/scan" \
       -H "Content-Type: application/json" \
       -H "idnorm-license-key: $IDNORM_LICENSE_KEY" \
       --data-binary @"$TMP_FILE"
else
  curl -X POST "$ENDPOINT/api/v1/scan" \
       -H "Content-Type: application/json" \
       --data-binary @"$TMP_FILE"
fi

# Clean up temporary file
rm -f "$TMP_FILE"
