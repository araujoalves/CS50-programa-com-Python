from PIL import Image, ImageOps  
import sys


def main():
    check_command_line()
    adjust_pic()


def check_command_line():
    if len(sys.argv) != 3:  
        if len(sys.argv) < 3:
            sys.exit('Too few command-line arguments')
        elif len(sys.argv)>3:
            sys.exit('Too many command-line arguments')
    else:  
        if str(sys.argv[1]).endswith('.png') or str(sys.argv[1]).endswith('.jpeg') \
                or str(sys.argv[1]).endswith('.jpg') or str(sys.argv[2]).endswith('.png') \
                or str(sys.argv[2]).endswith('.jpeg') or str(sys.argv[2]).endswith('.jpg'):
            if str(sys.argv[1])[-4:] != str(sys.argv[2])[-4:]:
                sys.exit('Input and output have different extensions')
        else:
            sys.exit('Invalid input')


def adjust_pic():  
    with Image.open('shirt.png') as shirt, Image.open(sys.argv[1]) as before:
        before = ImageOps.fit(before, size = shirt.size)
        before.paste(shirt, shirt)
        before.save(sys.argv[2])


main()
