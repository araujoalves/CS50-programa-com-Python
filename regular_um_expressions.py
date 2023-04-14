import re


def main():
    print(count(input("Text: ")))


def count(s):
    ums_count = 0
    if um := re.findall(r"\b\W*(um)\W?", s, re.IGNORECASE):
        ums_count = int(len(um))

    if ums_count is None:
        ums_count = 0

    return ums_count


if __name__ == "__main__":
    main()