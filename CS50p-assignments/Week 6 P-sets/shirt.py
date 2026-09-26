import sys
import os
from PIL import Image, ImageOps

def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    input_path = sys.argv[1]
    output_path = sys.argv[2]

    # Valid image extensions
    valid_extensions = [".jpg", ".jpeg", ".png"]

    # Extract extensions and convert to lowercase
    input_ext = os.path.splitext(input_path)[1].lower()
    output_ext = os.path.splitext(output_path)[1].lower()

    if input_ext not in valid_extensions or output_ext not in valid_extensions:
        sys.exit("Invalid output")

    if input_ext != output_ext:
        sys.exit("Input and output have different extensions")

    if not os.path.isfile(input_path):
        sys.exit("Input does not exist")

    try:
        # Open the background user image and the foreground shirt image
        user_image = Image.open(input_path)
        shirt_image = Image.open("shirt.png")

        # Get the size of the shirt image to resize the user image appropriately
        shirt_size = shirt_image.size

        # Resize and crop the user image to match the overlay dimensions perfectly
        cropped_user_image = ImageOps.fit(user_image, shirt_size)

        # Paste the shirt overlay on top using itself as a transparency mask
        cropped_user_image.paste(shirt_image, shirt_image)

        # Save the finalized image
        cropped_user_image.save(output_path)

    except FileNotFoundError:
        sys.exit("Input does not exist")

if __name__ == "__main__":
    main()
