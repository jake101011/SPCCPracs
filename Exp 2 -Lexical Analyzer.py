import re

keyword =['break', 'case', 'char', 'const', 'countinue', 'deafult', 'do', 'int', 'else', 'enum', 'extern', 'float', 'for',
'goto', 'if', 'long','register','return ','short','signed','sizeof','static','switch','typedef','union','unsigned','void','volatile','while ','range']

built_in_functions = ['clrscr()', 'printf(', 'scanf(', 'getch()', 'main()']

header_file_func = ['<stdio.h>', '<conio.h>', '<stdlib.h>']

operators = ['+', '-', '*', '/', '%', '==', '!=', '>', '<', '>=', '<=', '&&', '||', '!', '&', '|', '^', '~', '>>', '<<',
            '=', '+=', '-=', '*=']

specialsymbol = ['@', '#', '$', '_', '!']

separator = [',', ':', ';', '\n', '\t', '{', '}', '(', ')', '[', ']']

file = open('lexical.c', 'r+')

contents = file.read()

splitCode = contents.split()  # split program in word based on space

print(splitCode)

length = len(splitCode)  # count the number of word in program

identifiers, separators, operatorss, keywords, headers, numerals = [], [], [], [], [], []

k = 0
bi = 0
h = 0
o = 0
ss = 0
s = 0
for i in range(0, length):
   if splitCode[i] in keyword:
       keywords.append(splitCode[i])
       k = k + 1
       continue
   if splitCode[i] in operators:

       operatorss.append(splitCode[i])
       o = o + 1
       continue
   if splitCode[i] in specialsymbol:

        operatorss.append(splitCode[i])
        ss = ss + 1
        continue
   if splitCode[i] in header_file_func:

       headers.append(splitCode[i])
       h = h + 1
       continue
   if splitCode[i] in built_in_functions:

       headers.append(splitCode[i])
       bi = bi + 1
       continue
   if splitCode[i] in separator:

       separators.append(splitCode[i])
       s = s + 1
       continue
   if re.match(r'(#include*).*', splitCode[i]):

       headers.append(splitCode[i])
       continue
   if re.match(r'^[-+]?[0-9]+$', splitCode[i]):

       numerals.append(splitCode[i])
       continue
   if re.match(r"^[^\d\W]\w*\Z", splitCode[i]):

       identifiers.append(splitCode[i])

print("\nNumber of keywords: ", keywords)

print("Number of operators: ", operatorss)

print("Number of seperators: ", separators)

print("Number of header functions: ", headers)

print("number of identifiers: ", identifiers)

