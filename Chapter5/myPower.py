def myPowerRec(base, power):
    if power == 0:
        return 1
    elif power % 2 == 0:
        return myPowerRec(base * base, power / 2)
    elif power % 2 == 1:
        return base * myPowerRec(base, power - 1)
    else:
        return base

result = myPowerRec(3, 5)
print(result)