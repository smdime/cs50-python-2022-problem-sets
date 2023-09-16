import sys
import os
from PIL import Image, ImageOps

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

input_ext = os.path.splitext(sys.argv[1])[1].lower()
output_ext = os.path.splitext(sys.argv[2])[1].lower()
valid_ext = ['.jpg', '.jpeg', '.png']
if output_ext not in valid_ext:
    sys.exit("Invalid output file")
if input_ext != output_ext:
    sys.exit("Input and output have different extensions")

if len(sys.argv) == 3:
    try:
        image = Image.open(sys.argv[1])
        shirt = Image.open("shirt.png")
        image = ImageOps.fit(image, shirt.size)
        image.paste(shirt, (0, 0), shirt)
        image.save(sys.argv[2])
    except FileNotFoundError:
        sys.exit("Input does not exist")
