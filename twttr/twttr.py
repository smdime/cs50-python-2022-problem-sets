txt = input("Input: ").strip()
print("Output: ",end="")
vowels = ("aeiouAEIOU")
for c in txt:
    if c not in vowels:
        print(c,end="")
print()