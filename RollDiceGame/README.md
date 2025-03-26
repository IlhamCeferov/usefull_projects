![MyGitQr](../MyGitQr.jpg)
# QR Code Generator

This project is a simple Python-based QR Code Generator. It allows users to create QR codes from text or URLs and save them as image files.

## Features

- Generate QR codes from any text or URL.
- Customize the QR code's size and border.
- Save the generated QR code as an image file.

## Requirements

- Python 3.x
- `qrcode` library

## Installation

1. Clone the repository or copy the script to your local machine.
2. Install the required library using pip:
    ```bash
    pip install qrcode[pil]
    ```

## Usage

1. Run the script:
    ```bash
    python qr_code_generator.py
    ```
2. Enter the text or URL you want to encode.
3. Provide a filename (e.g., `qrcode.png`) to save the QR code.
4. The QR code will be saved in the current directory.

## Example

```bash
Enter the text or URL: https://example.com
Enter the filename: example_qr.png
QR code saved as example_qr.png
```

## File Structure

```
/QrCodeGenerator/
│
├── qr_code_generator.py  # Main script to generate QR codes
```

## License

This project is open-source and available under the MIT License.  