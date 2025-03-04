# StegoTool - A Simple Steganography CLI in Python 🖼️🔒

**StegoTool** is a simple CLI tool for hiding and extracting secret messages in images using **LSB (Least Significant Bit) encoding**.

## 🚀 Features
✔ Hide a message inside an image  
✔ Extract hidden messages from images  
✔ Uses LSB encoding for steganography  
✔ Simple CLI interface  

## 📌 Requirements
- Python 3.x  
- Pillow library (`pip install pillow`)

## 📖 Usage
### 🔹 Hide a Message
```sh
python stegotool.py --hide input.png secret.txt output.png
