def main():
    print(convert(input("Hours: ")))


def convert(s):
    try:  
        if '-' in s:
            raise ValueError

        if not ' to ' in s.lower():
            raise ValueError

        
        s = s.upper().split('TO')
        times = [elem.strip() for elem in s]
        hours = []

        for period in times:
            if ':' in period:  
                h, m = period.split(':')
                if int(h) > 12:  
                    raise ValueError
                else:
                    if m.endswith(' PM'):  
                        if h == '12':  
                            h = int(h)
                        else:
                            h = int(h) + 12
                        m = m.strip(' PM')

                    else:
                        if h == '12':  
                            h = 00
                        else:
                            h = int(h)  
                        m = m.strip(' AM')
                    if int(m) >= 60:  
                        raise ValueError
            else:
                if ' PM' in period:
                    h = period.strip(' PM')  
                    if int(h) > 12:  
                        raise ValueError
                    else:
                        if h == '12':  
                            h = 12
                        else:
                            h = int(h) + 12
                else:
                    h = period.strip(' AM')
                    if h == '12':  
                        h = 00
                    else:
                        h = int(h)
                m = '00'  

            a = f'{int(h):02d}:{m}'  
            hours.append(a)

        return f'{hours[0]} to {hours[1]}'

    except ValueError:
        raise ValueError



if __name__ == "__main__":
    main()
