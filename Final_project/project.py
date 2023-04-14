import datetime
import re

wage = 10.50


class Task:
    def __init__(self, number, deadline, topic, pages, payment):
        self.number = number
        self.deadline = deadline
        self.topic = topic
        self.pages = pages
        self.payment = payment

    def __repr__(self):
        return f"Task {self.number} about {self.topic} is due on {self.deadline}. Write {self.pages} pages and get {self.payment} USD."


def main():
    task = create_task()
    print(str(task))


def create_task():
    number = get_number()
    deadline = get_deadline()
    topic = get_topic()
    pages = get_pages()
    payment = get_payment(pages)
    return Task(number, deadline, topic, pages, payment)


def get_number():
    while True:
        number = input("What's the number of the task: ").strip().lower()
        number_valid = re.search("^[0-9]{3}[a-z]{3}$", number)
        if not number_valid:
            print("Please use valid format '123abc' case insensitive")
        else:
            return number_valid.group()


def get_deadline():
    day, month, year = input("When is the deadline: ").strip().split('.')
    deadline = datetime.datetime(int(year), int(month), int(day))
    return deadline.strftime("%d %b %Y")


def get_topic():
    return input("What's the topic of the task: ").title().strip()


def get_pages():
    pages = input("How many pages do you have to write: ")
    return int(pages)


def get_payment(pages):
    return pages * wage

if __name__ == "__main__":
    main()