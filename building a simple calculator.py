try:
    num1=int(input("enter the first number:  "))
    num2=int(input("enter the second number: "))

    print( "enter the operation which you wanna perform : (+, - , / , *)  ")
    op= input("enter the operation: ")

    match op:
       case '+':
             print(f" the result is { num1 + num2}")
       
       case '-':
            print(f" the result is { num1 - num2}")
       
       case '*':
            print(f" the result is { num1 * num2}")
       
       case '/':
            print(f" the result is { num1 / num2}")
        
       case default:
              print("an error occured ")
              
        

except Exception as e:
     print("enter the valid value of a and b")











