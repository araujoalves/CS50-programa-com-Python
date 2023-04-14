import sys


def main():
    print(command_line())


def command_line():
    counter = 0
    if len(sys.argv) < 2:  
        return sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:  
        return sys.exit("Too many command-line arguments")
    elif not sys.argv[1].endswith(".py"):  
        return sys.exit("Not a Python File")
    else:
        try:
            file = open(sys.argv[1], "r")  
            lines = file.readlines()  
        except FileNotFoundError:
            return sys.exit("File doesn't exist")
        for line in lines:
            if check_lines(line) is False:
                counter += 1
        return counter


def check_lines(line):
    if line.lstrip().startswith('#') or line.isspace():  
        return True
    return False


main()
