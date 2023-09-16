def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    null_d = d.replace("$","")
    float_d = round(float(null_d),1)
    return float_d

def percent_to_float(p):
    null_p = p.replace("%","")
    float_p = float(null_p)
    dec_p = round(float_p/100,2)
    return dec_p

main()