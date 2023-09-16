answer = input("What is the Answer to the Great question of \
Life, the Universe, and Everything? ").strip().lower().replace("-", " ")

if answer == "forty two" or answer == "42":
    print("Yes")
else:
    print("No")