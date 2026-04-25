def main():
    coke_price = 50

    print(f"Change owed:{coke_machine(coke_price)}")


def coke_machine(coke_price):
    balance = 0
    while balance < coke_price:
        type_coin = int(input("Insert the coin: "))

        match type_coin:
            case 25 | 10 | 5:
                balance += type_coin

                # being aware of negative amount dues
                if coke_price - balance >= 0:
                    print(f"Amount Due: {coke_price-balance}")
                else:
                    print("Amount Due: 0")
                    return (coke_price - balance) * -1

            case _:
                print("that is not a valid coin try 25|10|5")
    return 0


main()
