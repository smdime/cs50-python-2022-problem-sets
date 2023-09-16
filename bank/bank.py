greet = input("Greeting: ").strip().lower()
x = greet.startswith("hello")
y = greet.startswith("h")
if x == True:
    print("$0")
elif y == True:
    print("$20")
else:
    print("$100")