while True:
    print("\n--- numbers operation ---")
    print("1. Add numbers")
    print("2. check even odd")
    print("3. count vowels")
    print("4. find factorial")
    print("5. reverse string")
    print("6. check palindrome")
    print("7. exit")

    choice = int(input('enter option: '))

    if choice == 1:
        num1 = int(input('enter number1:')) 
        num2 = int(input('enter number2:')) 

        print("addition is:", num1 + num2)

    elif choice == 2:
        n = int(input('enter number:'))
        if n % 2 == 0 :
            print('even')
        else:
            print('odd')

    elif choice == 3:
        string1 = input("Enter string: ")
        vowels = 'aeiouAEIOU'
        count = 0
        
        for ch in string1:
            if ch in vowels:  
                count += 1
        
        print("Vowel count:", count)

