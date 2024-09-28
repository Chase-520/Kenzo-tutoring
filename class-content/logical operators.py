"""
In python, we have operator when using if statements.
"""

a = True  # boolean
b = False # boolean
c = 5     # int
d = 7     # int

"""
comparing numbers
"""
result1 = 5<7    # 5<7 this expression returns a boolean value -> True/ False
print(result1)

result2 = "Car"=="Car"    # we use == to check whether two variables are the same
print(result2)

result3 = 11>=7
print(result3)




var1 = ((5<7) and (50>7))
print(var1)

var2 = ((5<7) or (7<10))
print(var2)

var3 = ((5<10) and (10>=8))or (True)
"""
() or ()
|
((5<10)and(10>=8))  -> True
|
(True) or (True)    -> True

1> (something) or (something)
2> (5<10) -> True
3> (10>=8) -> True
4> (5<10) and (10>=8) -> True
5> True or True   -> True
"""
print(var3)



"""
if(boolean):
    **content**
elif(boolean):
    **content**
else:
    **content**
"""
if ("Car"=="car"):
    print("True")
else:
    print("False")

