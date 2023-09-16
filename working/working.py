import re

def main():
    print(convert(input("Hours: ").strip()))

def convert(s):
    if matches := re.search(r"(\d{1,2}(?::\d{2})?) (AM|PM) to (\d{1,2}(?::\d{2})?) (AM|PM)", s, re.IGNORECASE):
        start_time = matches.group(1)
        start_period = matches.group(2)
        end_time = matches.group(3)
        end_period = matches.group(4)

        start_hour, start_minute = map(int, start_time.split(":")) if ":" in start_time else (int(start_time), 0)
        end_hour, end_minute = map(int, end_time.split(":")) if ":" in end_time else (int(end_time), 0)

        if (
            start_hour < 1 or start_hour > 12 or
            end_hour < 1 or end_hour > 12 or
            start_minute < 0 or start_minute >= 60 or
            end_minute < 0 or end_minute >= 60
        ):
            raise ValueError

        if start_period == "PM" and start_hour < 12:
            start_hour += 12
        if end_period == "PM" and end_hour < 12:
            end_hour += 12
        if start_period == "AM" and start_hour == 12:
            start_hour -= 12
        if end_period == "AM" and end_hour == 12:
            end_hour -= 12

        new_time = f"{start_hour:02}:{start_minute:02} to {end_hour:02}:{end_minute:02}"
        return new_time
    else:
        raise ValueError

if __name__ == "__main__":
    main()