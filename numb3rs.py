import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    
    if ip_validated := re.search("^(.+)\\.(.+)\\.(.+)\\.(.+)$", ip):
        
        if int(ip_validated.group(1)) <= 255 and int(ip_validated.group(2)) <= 255 \
                and int(ip_validated.group(3)) <= 255 and int(ip_validated.group(4)) <= 255:
            return True

    return False


if __name__ == "__main__":
    main()
