import sys
import os
from PIL import Image, ImageOps


def is_not_valid(filenames):
    if len(filenames) < 3:
        return ("Too few command-line arguments"), None
    elif len(filenames) > 3:
        return ("Too many command-line arguments"), None

    filename_before = filenames[1]
    filename_after = filenames[2]
    ext1 = (os.path.splitext(filename_before))[-1].strip('.')
    ext2 = (os.path.splitext(filename_after))[-1].strip('.')

    valid_exts = ["jpg", "jpeg", "png"]
    if ext1 not in valid_exts:
        return ("Invalid input"), None
    elif ext2 not in valid_exts:
        return ("Invalid output"), None

    if (ext1 != ext2):
        return ("Input and output have different extensions"), None

    return None, [filename_before, filename_after]


def main():
    string, filenames = is_not_valid(sys.argv)
    if string and not filenames:
        sys.exit(string)

    input_image = filenames[0]
    output_image = filenames[1]

    i_image = Image.open(input_image)
    shirt_image = Image.open("shirt.png")
    o_image = ImageOps.fit(i_image, shirt_image.size)
    o_image.paste(shirt_image, shirt_image)
    o_image.save(output_image)


main()