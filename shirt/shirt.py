import sys
from os.path import splitext
from PIL import Image, ImageOps

def main():
    command_line()

    try:
        image_file = Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("Input does not exist")

    shirt_file = Image.open("shirt.png")
    size = shirt_file.size
    muppet = ImageOps.fit(image_file, size)
    muppet.paste(shirt_file, shirt_file)
    muppet.save(sys.argv[2])

def command_line():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    file1 = splitext(sys.argv[1])
    file2 = splitext(sys.argv[2])
    if extensions(file1[1]) == False:
        sys.exit("Invalid input")
    if extensions(file2[1]) == False:
        sys.exit("Invalid output")
    if file1[1].lower() != file2[1].lower():
        sys.exit("Input and output have different extensions")

def extensions(file):
    if file in [".jpg", ".jpeg", ".png"]:
        return True
    return False

if __name__ == "__main__":
    main()
