##0x06. Python - Classes and Objects##


**0-square.py:** Write an empty class Square that defines a square.

**1-square.py:** Write a class Square that defines a square by: (based on 0-square.py)

*Private instance attribute: size.

*Instantiation with size (no type/value verification).

*You are not allowed to import any module.

**Why?**

Why size is private attribute?

The size of a square is crucial for a square, many things depend of it (area computation, etc.), so you, as class builder, must control the type and value of this attribute. One way to have the control is to keep it privately. You will see in next tasks how to get, update and validate the size value.

**2-square.py:** Write a class Square that defines a square by: (based on 1-square.py)

**3-square.py:** Write a class Square that defines a square by: (based on 2-square.py)

**4-square.py:** Write a class Square that defines a square by: (based on 3-square.py)

**Why?**

Why a getter and setter?

Reminder: size is a private attribute. We did that to make sure we control the type and value. Getter and setter methods are not 100% Python, but more OOP. With them, you will be able to validate the assignment of a private attribute and also define how getting the attribute value will be available from outside - by copy? by assignment? etc. Also, adding type/value validation in the setter will centralize the logic, since you will do it in only one place.

**5-square.py:** Write a class Square that defines a square by: (based on 4-square.py)

**6-square.py:** Write a class Square that defines a square by: (based on 5-square.py)
