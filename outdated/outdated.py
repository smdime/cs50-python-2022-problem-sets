month = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    date = input("Date: ").strip()
    if "/" in date:
        m,d,y = date.split("/")
        if m.isnumeric() and int(m) <= 12 and int(d) <= 31:
            break
        else:
            continue
    if "," not in date:
        continue
    if "," in date:
        date = date.replace(",","")
        m,d,y = date.split(" ")
        m = m.title()
        if m.isalpha():
            if m in month:
                m = month.index(m) +1
                d = int(d)
                if m <= 12 and d <= 31:
                    break
                else:
                    continue
        else:
            continue
    break

print(f"{y}-{int(m):02}-{int(d):02}")
