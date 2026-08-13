"""

q3.3. yek machine hesab besazid , 
yek adade (number1) yek adade number2
yechizi begire operation (jam , tafrigh,taghsim,zarb)
anjam bede print kone
 

"""

number1 = float(input("please enter your first number:"))
operation = input("please enter your operation just between (+ - / *) :")
number2 = float(input("please enter your second number:"))

if operation == "+" :
    print("jam :", number1 + number2)
    
elif operation == "-" :
    print("tafrigh :", number1 - number2)
    
elif operation == "/" :
    print("taghsim :" , number1 / number2)
    
elif operation == "*" :
    print("zarb:", number1 * number2 )
    
else :
    print("ERROR")
