def main():
    word = input("Enter the word: ")
    print(f"the new word is: {delete_vowels(word)}")


def delete_vowels(word):
    new_word = ""
    for letter in word:
        if not letter.lower() in "aeiou":
            new_word += letter

    return new_word


main()
