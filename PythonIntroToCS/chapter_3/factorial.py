# x! = x * (x-1) * (x-2)... * 1
# Combination when the order dos not matter, set of x items:
# C(t,s)=t!/(s!*(t-s)!); t = total items; s = set of items/group of items
import math
x = math.factorial(5)
# print(x)

# 5!
# 1) 5(4)=20
# 2) 20(3)=60
# 3) 60(2)=120
# 4) 120(1)=120

# In this case, I had 4 cycles. In each cycle, the result was used to compute a new value, and the entered values were decremented by one with each cycle.
x = 5

def find_factorial(f):
    x=f
    for i in range(f):
        y = (f-(i+1))
        if y!=0:
            x = x*y # 5 * (5-1) = 20
        # print(x,'\n','-'*10)

    print(x)

find_factorial(6)

# for i in range(x):
#     y=x
#     x = x * (y-1) # 1 cycle: x = 5 *  (5-1); x = 20
#                   # 2 cycle: x = 20 * (20-1)
#     y-=1
