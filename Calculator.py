n1 = int(input("Enter number 1: "))
n2 = int(input("Enter number 2: "))
operator = input("Enter Operator: ")
match operator:
    case "+":
        print("Sum of these no. will be : ", n1+n2)
    case "-":
        print("Difference of these no. will be : ", n1-n2)
    case "*":
        print("Product of these no. will be : ", n1*n2)
    case "/":
        print("Division of these no. will be : ", n1/n2)
    case _ :
        print("Invalid Operator")