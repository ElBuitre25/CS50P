def main():
    greeting=input("Greeting: ").lower()
    print(dollar_by_greeting(greeting))


def dollar_by_greeting(greeting):
    if greeting.startswith("hello"):
        return "$0"
    elif greeting.startswith("h"):
        return "$20"
    else:
        return "$100"


main()