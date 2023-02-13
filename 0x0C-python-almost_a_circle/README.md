# 0x0C. Python - Almost a circle

  1. `tests/` All your files, classes and methods must be unit tested and be PEP 8 validated.
  ```
  guillaume@ubuntu:~/$ python3 -m unittest discover tests
...................................................................................
...................................................................................
.......................
----------------------------------------------------------------------
Ran 189 tests in 13.135s
OK
guillaume@ubuntu:~/$
  ```

  2. `models/base.py, models/__init__.py` This class will be the “base” of all other classes in this project. The goal of it is to manage id attribute in all your future classes and to avoid duplicating the same code (by extension, same bugs)
```
  guillaume@ubuntu:~/$ cat 0-main.py
#!/usr/bin/python3
""" 0-main """
from models.base import Base
if __name__ == "__main__":

    b1 = Base()
    print(b1.id)
    b2 = Base()
    print(b2.id)
    b3 = Base()
    print(b3.id)
    b4 = Base(12)
    print(b4.id)
    b5 = Base()
    print(b5.id)
guillaume@ubuntu:~/$ ./0-main.py
1
2
3
12
4
guillaume@ubuntu:~/$ 
  ```
  3. `models/rectangle.py` Because we want to protect attributes of our class. With a setter, you are able to validate what a developer is trying to assign to a variable. So after, in your class you can “trust” these attributes.
  ```
  guillaume@ubuntu:~/$ cat 1-main.py
  #!/usr/bin/python3
  """ 1-main """
  from models.rectangle import Rectangle

  if __name__ == "__main__":

      r1 = Rectangle(10, 2)
      print(r1.id)

      r2 = Rectangle(2, 10)
      print(r2.id)

      r3 = Rectangle(10, 2, 0, 0, 12)
      print(r3.id)

  guillaume@ubuntu:~/$ ./1-main.py
  1
  2
  12
  guillaume@ubuntu:~/$ 
  ```
  4. `models/rectangle.py` Update the class Rectangle by adding validation of all setter methods and instantiation (id excluded)

  ```
      guillaume@ubuntu:~/$ cat 2-main.py
      #!/usr/bin/python3
      """ 2-main """
      from models.rectangle import Rectangle

      if __name__ == "__main__":

          try:
              Rectangle(10, "2")
          except Exception as e:
              print("[{}] {}".format(e.__class__.__name__, e))

          try:
              r = Rectangle(10, 2)
              r.width = -10
          except Exception as e:
              print("[{}] {}".format(e.__class__.__name__, e))

          try:
              r = Rectangle(10, 2)
              r.x = {}
          except Exception as e:
              print("[{}] {}".format(e.__class__.__name__, e))

          try:
              Rectangle(10, 2, 3, -1)
          except Exception as e:
              print("[{}] {}".format(e.__class__.__name__, e))

      guillaume@ubuntu:~/$ ./2-main.py
      [TypeError] height must be an integer
      [ValueError] width must be > 0
      [TypeError] x must be an integer
      [ValueError] y must be >= 0
      guillaume@ubuntu:~/$ 
  ```
  5. `models/rectangle.py` Update the class Rectangle by adding the public method def area(self): that returns the area value of the Rectangle instance.

  ```
  guillaume@ubuntu:~/$ cat 3-main.py
  #!/usr/bin/python3
  """ 3-main """
  from models.rectangle import Rectangle

  if __name__ == "__main__":

      r1 = Rectangle(3, 2)
      print(r1.area())

      r2 = Rectangle(2, 10)
      print(r2.area())

      r3 = Rectangle(8, 7, 0, 0, 12)
      print(r3.area())

  guillaume@ubuntu:~/$ ./3-main.py
  6
  20
  56
  guillaume@ubuntu:~/$ 
  ```
  6. __str__ `models/rectangle.py` Update the class Rectangle by overriding the __str__ method so that it returns `[Rectangle] (<id>) <x>/<y> - <width>/<height> `
  ```
    guillaume@ubuntu:~/$ cat 5-main.py
    #!/usr/bin/python3
    """ 5-main """
    from models.rectangle import Rectangle

    if __name__ == "__main__":

        r1 = Rectangle(4, 6, 2, 1, 12)
        print(r1)

        r2 = Rectangle(5, 5, 1)
        print(r2)

    guillaume@ubuntu:~/$ ./5-main.py
    [Rectangle] (12) 2/1 - 4/6
    [Rectangle] (1) 1/0 - 5/5
    guillaume@ubuntu:~/$ 
  ```
  7. Update the class Rectangle by improving the public method def display(self): to print in stdout the Rectangle instance with the character # by taking care of x and y
  ```
    guillaume@ubuntu:~/$ cat 6-main.py
    #!/usr/bin/python3
    """ 6-main """
    from models.rectangle import Rectangle

    if __name__ == "__main__":

        r1 = Rectangle(2, 3, 2, 2)
        r1.display()

        print("---")

        r2 = Rectangle(3, 2, 1, 0)
        r2.display()

    guillaume@ubuntu:~/$ ./6-main.py | cat -e
    $
    $
      ##$
      ##$
      ##$
    ---$
    ###$
    ###$
    guillaume@ubuntu:~/$ 
  ```
  8. Update #0 Update the class Rectangle by adding the public method def update(self, *args)
```
      guillaume@ubuntu:~/$ cat 7-main.py
      #!/usr/bin/python3
      """ Doc """
      from models.rectangle import Rectangle

      if __name__ == "__main__":

          r1 = Rectangle(10, 10, 10, 10)
          print(r1)

          r1.update(89)
          print(r1)

          r1.update(89, 2)
          print(r1)

          r1.update(89, 2, 3)
          print(r1)

          r1.update(89, 2, 3, 4)
          print(r1)

          r1.update(89, 2, 3, 4, 5)
          print(r1)

      guillaume@ubuntu:~/$ ./7-main.py
      [Rectangle] (1) 10/10 - 10/10
      [Rectangle] (89) 10/10 - 10/10
      [Rectangle] (89) 10/10 - 2/10
      [Rectangle] (89) 10/10 - 2/3
      [Rectangle] (89) 4/10 - 2/3
      [Rectangle] (89) 4/5 - 2/3
      guillaume@ubuntu:~/$ 
```
  9. Update #1 Update the class Rectangle by updating the public method def update(self, *args): by changing the prototype to update(self, *args, **kwargs) that assigns a key/value argument to attributes

  ```
    guillaume@ubuntu:~/$ cat 8-main.py
    #!/usr/bin/python3
    """ 8-main """
    from models.rectangle import Rectangle

    if __name__ == "__main__":

        r1 = Rectangle(10, 10, 10, 10)
        print(r1)

        r1.update(height=1)
        print(r1)

        r1.update(width=1, x=2)
        print(r1)

        r1.update(y=1, width=2, x=3, id=89)
        print(r1)

        r1.update(x=1, height=2, y=3, width=4)
        print(r1)

    guillaume@ubuntu:~/$ ./8-main.py
    [Rectangle] (1) 10/10 - 10/10
    [Rectangle] (1) 10/10 - 10/1
    [Rectangle] (1) 2/10 - 1/1
    [Rectangle] (89) 3/1 - 2/1
    [Rectangle] (89) 1/3 - 4/2
    guillaume@ubuntu:~/$ 
  ```
  10. And now, the Square!
mandatory
Write the class Square that inherits from Rectangle
```
    guillaume@ubuntu:~/$ cat 9-main.py
    #!/usr/bin/python3
    """ 9-main """
    from models.square import Square

    if __name__ == "__main__":

        s1 = Square(5)
        print(s1)
        print(s1.area())
        s1.display()

        print("---")

        s2 = Square(2, 2)
        print(s2)
        print(s2.area())
        s2.display()

        print("---")

        s3 = Square(3, 1, 3)
        print(s3)
        print(s3.area())
        s3.display()

    guillaume@ubuntu:~/$ ./9-main.py
    [Square] (1) 0/0 - 5
    25
    #####
    #####
    #####
    #####
    #####
    ---
    [Square] (2) 2/0 - 2
    4
      ##
      ##
    ---
    [Square] (3) 1/3 - 3
    9

    ###
    ###
    ###
    guillaume@ubuntu:~/$ 
```
11. Square size
mandatory
Update the class Square by adding the public getter and setter size
  ```
        guillaume@ubuntu:~/$ cat 10-main.py
        #!/usr/bin/python3
        """ 10-main """
        from models.square import Square

        if __name__ == "__main__":

            s1 = Square(5)
            print(s1)
            print(s1.size)
            s1.size = 10
            print(s1)

            try:
                s1.size = "9"
            except Exception as e:
                print("[{}] {}".format(e.__class__.__name__, e))

        guillaume@ubuntu:~/$ ./10-main.py
        [Square] (1) 0/0 - 5
        5
        [Square] (1) 0/0 - 10
        [TypeError] width must be an integer
        guillaume@ubuntu:~/$ 
  ```
  124. Square update
mandatory
Update the class Square by adding the public method def update(self, *args, **kwargs) that assigns attributes
```
      guillaume@ubuntu:~/$ cat 11-main.py
      #!/usr/bin/python3
      """ 11-main """
      from models.square import Square

      if __name__ == "__main__":

          s1 = Square(5)
          print(s1)

          s1.update(10)
          print(s1)

          s1.update(1, 2)
          print(s1)

          s1.update(1, 2, 3)
          print(s1)

          s1.update(1, 2, 3, 4)
          print(s1)

          s1.update(x=12)
          print(s1)

          s1.update(size=7, y=1)
          print(s1)

          s1.update(size=7, id=89, y=1)
          print(s1)

      guillaume@ubuntu:~/$ ./11-main.py
      [Square] (1) 0/0 - 5
      [Square] (10) 0/0 - 5
      [Square] (1) 0/0 - 2
      [Square] (1) 3/0 - 2
      [Square] (1) 3/4 - 2
      [Square] (1) 12/4 - 2
      [Square] (1) 12/1 - 7
      [Square] (89) 12/1 - 7
      guillaume@ubuntu:~/$ 
```
13. Rectangle instance to dictionary representation
mandatory
Update the class Rectangle by adding the public method def to_dictionary(self): that returns the dictionary representation of a Rectangle
```
        guillaume@ubuntu:~/$ cat 12-main.py
        #!/usr/bin/python3
        """ 12-main """
        from models.rectangle import Rectangle

        if __name__ == "__main__":

            r1 = Rectangle(10, 2, 1, 9)
            print(r1)
            r1_dictionary = r1.to_dictionary()
            print(r1_dictionary)
            print(type(r1_dictionary))

            r2 = Rectangle(1, 1)
            print(r2)
            r2.update(**r1_dictionary)
            print(r2)
            print(r1 == r2)

        guillaume@ubuntu:~/$ ./12-main.py
        [Rectangle] (1) 1/9 - 10/2
        {'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10}
        <class 'dict'>
        [Rectangle] (2) 0/0 - 1/1
        [Rectangle] (1) 1/9 - 10/2
        False
        guillaume@ubuntu:~/$ 
```
