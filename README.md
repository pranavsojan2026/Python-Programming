# QR Code Generator

This Python script generates a QR code for a given URL input by the user. It utilizes the `qrcode` library to create the QR code image.

## Prerequisites

- Python 3.x
- `qrcode` library (install using `pip install qrcode`)

## Usage

1. Run the script `generate_qrcode.py`.
2. Enter the URL for which you want to generate the QR code when prompted.
3. The script will validate the URL and generate a QR code image for it.
4. The generated QR code image will be saved as `qrimage.png` in the same directory as the script.

## Functionality

- The `generate_qrcode()` function takes a text input and generates a QR code image for it.
- The `get_valid_url()` function ensures that the user provides a valid URL input before generating the QR code.

## Files

- `generate_qrcode.py`: The main Python script.
- `qrimage.png`: The generated QR code image.

## Example


A QR code for `https://example.com` will be generated and saved as `qrimage.png`.

## Author

[Pranav Sojan]

