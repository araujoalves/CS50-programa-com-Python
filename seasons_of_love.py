from datetime import date
import sys
import inflect  
p = inflect.engine()  

def main():
    valid_date = validate(input('Date of Birth: '))
    delta = (date.today() - valid_date).days * 24 * 60  
    print(get_words(delta))  


def validate(date_of_birth):
    try:
        return date.fromisoformat(date_of_birth)  
    except ValueError:
        sys.exit('Invalid date')


def get_words(delta):
    in_words = p.number_to_words(delta, andword = '')  
    return in_words.capitalize() + ' minutes'


if __name__ == "__main__":
    main()
