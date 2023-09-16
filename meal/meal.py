def main():
    time = input("What time is it? ").strip()
    if 18.00 <= convert(time) <= 19.00:
        print("dinner time")
    elif 12.00 <= convert(time) <= 13.00:
        print("lunch time")
    elif 7.00 <= convert(time) <= 8.00:
        print("breakfast time")

def convert(time):
    h,m = time.split(":")
    dec = float(h)+(float(m)/60)
    return dec

if __name__ == "__main__":
    main()