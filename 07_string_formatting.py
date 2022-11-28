name = "John"
age = 56

"%s's age is %d" % ('John', 56)
"{}'s age is {}".format('John', 56)
f"{name}'s age is {age}"
# John's age is 56

"{name}'s age is {age}".format(name='John', age=56)

"Reuse the same values {x}, {y} in different places {x} and here {y}".format(x=10, y=4)

"{0} == {1} or {1} != {0}".format(1, 2)

