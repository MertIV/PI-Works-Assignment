import math

MIN = 501
MAX = 601

def fixed_interval():
    for num in range(MIN,MAX,2):
        if all(num%i!=0 for i in range(3,int(math.sqrt(num))+1, 2)):
            print(num)

def with_statement():
#having 3 digit
#starting with 5
    num = 0
    while True:
        first_digit = int(str(num)[:1])
        if num < 100:
            num += 1
            continue
        elif first_digit == 5:
            if all(num%i!=0 for i in range(2,int(math.sqrt(num))+1)):
                print(num)
        elif num > 999:
            break
        num += 1

fixed_interval()
with_statement()



