def main():
    came_case_word = input("Enter the camel case word: ")
    print(to_snake_case(came_case_word))


def to_snake_case(camel_word):
    snake_case_word = ""
    for letter in camel_word:
        if letter.isupper():
            snake_case_word = snake_case_word + "_" + letter.lower()
        else:
            snake_case_word = snake_case_word + letter
    return snake_case_word

main()
