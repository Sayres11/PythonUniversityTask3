print('''please Select the Operation you  want to Perfom
      + = Add
      - = Subtract
      * = Multiply
      / = Divide''')

opt = str(input("Choose Operation = "))

n1 = int(input("First Number  = "))
n2 = int(input("Second Number = "))

if opt == "+":
    print(n1, ' + ', n2, '  =  ', n1 + n2)
elif opt == "-":
    print(n1, ' - ', n2, '  =  ', n1 - n2)
elif opt == "*":
    print(n1, ' * ', n2, '  =  ', n1 * n2)
elif opt == "/":
    print(n1, ' / ', n2, '  =  ', n1 / n2)
else:
    print('Invalid Input')
