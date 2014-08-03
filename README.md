Project1
========
This is a small package, with some modules.
The purpose is to fetch webpages and converting them to form a structured book.
* * *

Problem statement :
----------------- 
To create a script which can generate a pdf book from its web based version.
So that it can be read offline.
While it has individual module also to generate pdf from a single web page.

Instructions:
------------
The script is convinient to run from command prompt.
It requires standard input.
First input is the url of the book/any page.
Second input is the path of directory, where to save the ouput.

Standard modules used:
---------------------
*OS*, *urllib*, *fpdf* modules are used.
OS provides a portable way of using operating system dependent functionality, such as executing commands.
In the script, it is used for creating in directories, and checking existence of directories.
For more information on OS, read the [documentation of OS][]

urllib provides a high level interface for fetching data across the world wide web.
For more information on OS, read the [documentation of urllib][]

fpdf is a library for generating pdf documents under python, ported from php. 
for more info visit [pyfpdf][]

Rest and required information is provided in the script itself.

[documentation of OS]:https://docs.python.org/2/library/os.html
[documentation of urllib]:https://docs.python.org/2/library/urllib.html
[pyfpdf]:https://code.google.com/p/pyfpdf/wiki/ReferenceManual

This is a just a test project and not for any commercial use.
-------------------------------------------------------------