import random
import time
num1=random.randint (1,9)
num2=random.randint (1,9)
num3=random.randint (1,9)

t1=False
t2=False
t3=False
nums=0
print(f"los numeros ganadores son: {num1},{num2},{num3}")
                     
while not t1 or not t2 or not t3:
    n=random.randint(1,9 )
    time.sleep(1)
    if n==num1:
        t1=True
    if n==num2:
        t2=True
    if n==num3:
        t3=True



