Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

================= RESTART: C:/Python311/python101/writefile.py =================
Traceback (most recent call last):
  File "C:/Python311/python101/writefile.py", line 2, in <module>
    file.write('hello world')
NameError: name 'file' is not defined. Did you mean: 'myfile'?

================= RESTART: C:/Python311/python101/writefile.py =================

================= RESTART: C:/Python311/python101/writefile.py =================

================= RESTART: C:/Python311/python101/writefile.py =================

================= RESTART: C:/Python311/python101/writefile.py =================
Traceback (most recent call last):
  File "C:/Python311/python101/writefile.py", line 9, in <module>
    adddata('pencil 10 baht')
  File "C:/Python311/python101/writefile.py", line 7, in adddata
    myfile.writeline(text)
AttributeError: '_io.TextIOWrapper' object has no attribute 'writeline'. Did you mean: 'writelines'?

================= RESTART: C:/Python311/python101/writefile.py =================

================= RESTART: C:/Python311/python101/writefile.py =================
>>> 
================= RESTART: C:/Python311/python101/writefile.py =================
>>> 
================= RESTART: C:/Python311/python101/writefile.py =================
>>> 
================= RESTART: C:/Python311/python101/writefile.py =================
['namtaohu 8 bahtcandy 5 bahtpencil 10 bahtpencil 10 baht\n', 'eraser 10 baht\n', 'guay teaw 10 baht\n', 'kao mun chicken 10 baht\n', 'foi thong 10 baht\n']
>>> 
================= RESTART: C:/Python311/python101/writefile.py =================
<built-in method read of _io.TextIOWrapper object at 0x000001CCFE55AF60>
>>> 
================= RESTART: C:/Python311/python101/writefile.py =================
namtaohu 8 bahtcandy 5 bahtpencil 10 bahtpencil 10 baht
eraser 10 baht
guay teaw 10 baht
kao mun chicken 10 baht
foi thong 10 baht

>>> box = []
>>> box.append('pen')
>>> box.append('eraser')
>>> box
['pen', 'eraser']
>>> print(box)
['pen', 'eraser']
>>> print(box(1))
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    print(box(1))
TypeError: 'list' object is not callable
>>> print(box[0])
pen
>>> shop = {'pen':['pentel','nokgaew','lulu']}
>>> shop = {'pen':['pentel','nokgaew','lulu'],'eraser':['horse','stetler','gaijae']}
>>> print(brand['pen'])
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    print(brand['pen'])
NameError: name 'brand' is not defined
print(shop['pen'])
['pentel', 'nokgaew', 'lulu']
print(shop['pen'][1])
nokgaew
