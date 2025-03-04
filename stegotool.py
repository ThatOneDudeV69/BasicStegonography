import argparse
from PIL import Image

EOF_MARKER = '1111111111111110'  # End-of-message marker

def text_to_binary(text):
    """Convert text to binary representation."""
    return ''.join(format(ord(char), '08b') for char in text)

def binary_to_text(binary):
    """Convert binary back to text."""
    chars = [binary[i:i+8] for i in range(0, len(binary), 8)]
    return ''.join(chr(int(char, 2)) for char in chars if int(char, 2) != 0)

def hide_message(image_path, text_path, output_path):
    """Hide text from a file inside an image."""
    try:
        with open(text_path, "r", encoding="utf-8") as file:
            message = file.read()
    except FileNotFoundError:
        print(f"Error: File '{text_path}' not found.")
        return

    image = Image.open(image_path)
    pixels = image.load()
    
    binary_message = text_to_binary(message) + EOF_MARKER  # Append EOF marker
    index = 0

    for y in range(image.height):
        for x in range(image.width):
            if index < len(binary_message):
                r, g, b = pixels[x, y]
                r = (r & ~1) | int(binary_message[index])  # Modify LSB of red channel
                pixels[x, y] = (r, g, b)
                index += 1
            else:
                break

    image.save(output_path)
    print(f"[✅] Message hidden successfully in '{output_path}'")

def extract_message(image_path):
    """Extract hidden message from an image."""
    image = Image.open(image_path)
    pixels = image.load()
    
    binary_message = ""
    for y in range(image.height):
        for x in range(image.width):
            r, _, _ = pixels[x, y]
            binary_message += str(r & 1)

    binary_message = binary_message.split(EOF_MARKER)[0]  # Stop at EOF marker
    message = binary_to_text(binary_message)

    print("[📥] Extracted message:\n")
    print(message)

def main():
    parser = argparse.ArgumentParser(description="Steganography Tool - Hide and Extract Messages in Images")
    parser.add_argument("--hide", nargs=3, metavar=("IMAGE", "TEXTFILE", "OUTPUT"), 
                        help="Hide a message from a text file inside an image.")
    parser.add_argument("--extract", metavar="IMAGE", help="Extract hidden message from an image.")
    
    args = parser.parse_args()

    if args.hide:
        hide_message(*args.hide)
    elif args.extract:
        extract_message(args.extract)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
