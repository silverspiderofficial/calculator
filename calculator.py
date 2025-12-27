print("=" * 40)
print(">> HI, THIS IS A CALCULATOR.")
print("=" * 40)
print(">> CHOOSE :")

def CALCULATOR():
    while True:
        print("\n>> 1) Addition\n>> 2) Multiplication\n>> 3) Subtraction\n>> 4) Division")
        x = input(">> Enter your choice (1-4): ")
        
        if x in ['1', '2', '3', '4']:
            try:
                a = float(input("Write your first number: "))
                b = float(input("Write your second number: "))
                
                if x == '1':
                    print(f">> Result: {a} + {b} = {a + b}")
                elif x == '2':
                    print(f">> Result: {a} × {b} = {a * b}")
                elif x == '3':
                    print(f">> Result: {a} - {b} = {a - b}")
                elif x == '4':
                    if b != 0:
                        print(f">> Result: {a} ÷ {b} = {a / b}")
                    else:
                        print(">> ERROR: Cannot divide by zero!")
                
                again = input("\n>> Do you want another calculation? (yes/no): ")
                if again.lower() != 'yes':
                    print(">> Goodbye!")
                    break
                    
            except ValueError:
                print(">> ERROR: Please enter valid numbers!")
        else:
            print(">> WRONG CHOICE -- Please try again!")

CALCULATOR()