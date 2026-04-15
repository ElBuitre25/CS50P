def main():
    number=int(input("Input the number"))

    if (is_even(number)):
        print("The number is even")
    else:
        print("Is odd")



def is_even(number):  
    return number%2==0
        
   


main()