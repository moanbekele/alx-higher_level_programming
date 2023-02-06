# 0x0A. Python - Inheritance
  > ### Mandatory
  - ```0-lookup.py``` Function that returns the list of available attributes and methods of an objec
  - ```1-my_list.py, tests/1-my_list.txt``` A class MyList that inherits from list
  - ```2-is_same_class.py``` unction that returns True if the object is exactly an instance of the specified class ; otherwise False
  - ```3-is_kind_of_class.py```Function that returns True if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class ; otherwise False
  - ```4-inherits_from.py```Function that returns True if the object is an instance of a class that inherited (directly or indirectly) from the specified class ; otherwise False.
  - ```5-base_geometry.py```Write an empty class BaseGeometry.
  - ```6-base_geometry.py``` Write a class BaseGeometry (based on 5-base_geometry.py)
  - ```7-base_geometry.py, tests/7-base_geometry.txt``` Write a class BaseGeometry (based on 6-base_geometry.py)
  - ```8-rectangle.py``` Write a class Rectangle that inherits from BaseGeometry (7-base_geometry.py).
  - ```9-rectangle.py``` Write a class Rectangle that inherits from BaseGeometry (7-base_geometry.py). (task based on 8-rectangle.py)
  - ```10-square.py``` Write a class Square that inherits from Rectangle (9-rectangle.py):5-base_geometry.py)
  - ```11-square.py``` Write a class Square that inherits from Rectangle (9-rectangle.py). (task based on 10-square.py).
  - ```6-base_geometry.py``` Write a class BaseGeometry (based on 5-base_geometry.py)

> ### Advanced 
  - ```100-sorted_hash_table.c```  
  Write a class MyInt that inherits from int
  - MyInt is a rebel. MyInt has == and != operators inverted
  ```
guillaume@ubuntu:~/0x0A$ cat 100-main.py
#!/usr/bin/python3
MyInt = __import__('100-my_int').MyInt
my_i = MyInt(3)
print(my_i)
print(my_i == 3)
print(my_i != 3)
guillaume@ubuntu:~/0x0A$ ./100-main.py
3
False
True
guillaume@ubuntu:~/0x0A$ 
  ```

- ```101-add_attribute.py```  
  Function that adds a new attribute to an object if it’s possible
  - Raise a TypeError exception, with the message can't add new attribute if the object can’t have new attribute
  ```
  guillaume@ubuntu:~/0x0A$ cat 101-main.py
#!/usr/bin/python3
add_attribute = __import__('101-add_attribute').add_attribute
class MyClass():
    pass
mc = MyClass()
add_attribute(mc, "name", "John")
print(mc.name)
try:
    a = "My String"
    add_attribute(a, "name", "Bob")
    print(a.name)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
guillaume@ubuntu:~/0x0A$ ./101-main.py
John
[TypeError] can't add new attribute
guillaume@ubuntu:~/0x0A$ 
  ```



