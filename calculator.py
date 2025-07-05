def calculator(): 
    print("✨Welcome to my Pyth.Calc✨")
    print("Choose your function:") 
    print("1. Addition (+)")
    print("2. Subtraction (-)") 
    print("3. Multiplication (x)") 
    print("4. Division (/)")

    choice= input("\nEnter function: ")

    if choice not in ['1','2','3','4']: 
     print("\nBro that's not even a valid option 💀") 
     return 

    n1= float(input("Enter first number: "))
    n2= float(input("Enter second number: "))

    if choice=="1":
     ans= n1 + n2 
    elif choice=="2":
     ans= n1 - n2
    elif choice=="3":
     ans= n1 * n2
    elif choice=="4":
     if n2 == 0:
        print("we both know that's invalid, who you foolin' bruh?")
        return
     ans= n1/n2 

    print(f"\nResult: {ans}")
calculator()
