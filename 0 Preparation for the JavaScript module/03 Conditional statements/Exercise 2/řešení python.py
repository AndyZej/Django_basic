# Grade variable
grade = 6

# Conditional statement (switch equivalent)
match grade:
    case 6:
        print("excellent")
    case 5:
        print("very good")
    case 4:
        print("good")
    case 3:
        print("sufficient")
    case 2:
        print("passing")
    case 1:
        print("fail")
    case _:
        print("Invalid grade")