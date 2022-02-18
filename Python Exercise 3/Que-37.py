import re

def isValidPinCode(pinCode):

    regex = "^[1-9]{1}[0-9]{2}\\s{0,1}[0-9]{3}$"
    p = re.compile(regex)
    if (pinCode == ''):
        return False
    m = p.match(pinCode)
    if m is None:
        return False
    else:
        return True


num1 ="384355"
print(num1, ": ", isValidPinCode(num1))
num2 = "201 305"
print(num2, ": ", isValidPinCode(num2))
num3 = "014205"
print(num3, ": ", isValidPinCode(num3))
num4 = "1473598"
print(num4, ": ", isValidPinCode(num4))
