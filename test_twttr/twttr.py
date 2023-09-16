def main():
    word = input("Input: ").strip()
    no_vowels = shorten(word)
    print(f"Output: {no_vowels}")

def shorten(word):
    vowels = ("aeiouAEIOU")
    no_vowels = ""
    for n in word:
        if n not in vowels:
            no_vowels = n
    return no_vowels

if __name__ == "__main__":
    main()