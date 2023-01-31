# 0x09. Python - Everything is object
  > ### Mandatory
  - ```0-answer.txt```Function for type of object
  - ```1-answer.txt``` get the variable identifier (which is the memory address in the CPython implementation)
  - ```2-answer.txt```
   - In the following code, do a and b point to the same object? Answer with Yes or No.
```
>>> a = 89
>>> b = 100
```
  - ```3-answer.txt```
   - In the following code, do a and b point to the same object? Answer with Yes or No
```
>>> a = 89
>>> b = 89
```
  - ```4-answer.txt```
   - In the following code, do a and b point to the same object? Answer with Yes or No.
```
>>> a = 89
>>> b = a
```
  - ```5-answer.txt```
   - In the following code, do a and b point to the same object? Answer with Yes or No.
```
>>> a = 89
>>> b = a + 1
```
  - ```6-answer.txt```
   - What do these 3 lines print?
```
>>> s1 = "Best School"
>>> s2 = s1
>>> print(s1 == s2)
```
  - ```7-answer.txt```
   - What do these 3 lines print?.
```
>>> s1 = "Best"
>>> s2 = s1
>>> print(s1 is s2)
```
  - ```8-answer.txt```
   - What do these 3 lines print?
```
>>> s1 = "Best School"
>>> s2 = "Best School"
>>> print(s1 == s2)
```
  - ```9-answer.txt```
   - What do these 3 lines print?
```
>>> s1 = "Best School"
>>> s2 = "Best School"
>>> print(s1 is s2)
```
  - ```10-answer.txt```
   - What do these 3 lines print?
```
>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3] 
>>> print(l1 == l2)
```
  - ```11-answer.txt```
   - What do these 3 lines print?
```
>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3] 
>>> print(l1 is l2)
```
  - ```12-answer.txt```
   - What do these 3 lines print?
```
>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> print(l1 == l2)
```
  - ```13-answer.txt```
   - What do these 3 lines print?
```
>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> print(l1 is l2)
```
  - ```14-answer.txt```
   - What do this script print?
```
l1 = [1, 2, 3]
l2 = l1
l1.append(4)
print(l2)
```
  - ```15-answer.txt```
   - What do this script print?
```
l1 = [1, 2, 3]
l2 = l1
l1 = l1 + [4]
print(l2)
```
  - ```16-answer.txt```
   - What do these 3 lines print?
```
def increment(n):
    n += 1
a = 1
increment(a)
print(a)
```
  - ```17-answer.txt```
   - What do this script print?
```
def increment(n):
    n.append(4)
l = [1, 2, 3]
increment(l)
print(l)
```
  - ```18-answer.txt```
   - What do this script print?
```
def assign_value(n, v):
    n = v
l1 = [1, 2, 3]
l2 = [4, 5, 6]
assign_value(l1, l2)
print(l1)
```

- ```19-copy_list.py```  function `def copy_list(l):` that returns a copy of a list

- ```20-answer.txt```
  ```
a = ()
```
   - Is a a tuple? Answer with Yes or No.

- ```21-answer.txt```
  ```
a = (1, 2)
```
   - Is a a tuple? Answer with Yes or No.
- ```22-answer.txt```
```
a = (1)
```
   - Is a a tuple? Answer with Yes or No.

- ```23-answer.txt```
  ```
a = (1, )
```
   - Is a a tuple? Answer with Yes or No.

- ```24-answer.txt```
   - What do this script print?
```
a = (1)
b = (1)
a is b
```
- ```25-answer.txt```
   - What do this script print?
```
a = (1, 2)
b = (1, 2)
a is b
```
- ```26-answer.txt```
   - What do this script print?
```
a = ()
b = ()
a is b
```
- ```27-answer.txt```
   - What do this script print?
```
>>> id(a)
139926795932424
>>> a
[1, 2, 3, 4]
>>> a = a + [5]
>>> id(a)
```
- ```28-answer.txt```
   - What do this script print?
```
>>> a
[1, 2, 3]
>>> id (a)
139926795932424
>>> a += [4]
>>> id(a)

> ### Advanced 
- ```100-magic_string.py```  function `magic_string()` that returns a string “BestSchool” n times the number of the iteration
- ```101-locked_class.py```  Write a class LockedClass with no class or object attribute, that prevents the user from dynamically creating new instance attributes, except if the new instance attribute is called first_name
- ```102-square.py```  Write a class Square that defines a square by: (based on 4-square.py)
- ```103-line1.txt```, ```103-line2.txt``` How many int objects are created by the execution of the first and second line of the script?
- ```104-line1.txt```, ```104-line2.txt,``` 104-line3.txt```, ```104-line4.txt```, ```104-line5.txt```  How many int objects are created by the execution of all line of the script?
- ```106-line1.txt```, ```106-line2.txt,``` 106-line3.txt```, ```106-line4.txt```, ```106-line5.txt```  



