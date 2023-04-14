import sys
import csv  


def main():
    check_command_line()
    read_write()


def check_command_line():
    if len(sys.argv) < 3:  
        sys.exit('Too few command-line arguments')
    elif len(sys.argv) > 3:
        sys.exit('Too many command-line arguments')
    elif '.csv' not in sys.argv[1] or '.csv' not in sys.argv[2]:  
        sys.exit('Not a CSV file')


def read_write():
    firstName_lastName_house = []  
    try:
        with open(sys.argv[1], 'r') as b_file:
            reader = csv.DictReader(b_file)  
            for row in reader:
                first_name, last_name = row['name'].split(',')
                firstName_lastName_house.append({
                    'first': first_name, 'last': last_name, 'house': row['house']
                })

    except FileNotFoundError:
        sys.exit(f'Could not read {sys.argv[1]}')

    fieldnames = ['first', 'last', 'house']
    with open(sys.argv[2], 'w') as a_file:
        writer = csv.DictWriter(a_file, fieldnames=fieldnames)  
        writer.writeheader()
        writer.writerows(firstName_lastName_house)


if __name__ == "__main__":
    main()
