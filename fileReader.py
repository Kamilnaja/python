import os
mystr = {'name': 'janusz', 'lastName': 'naja'}


def openFile(file):
    u""" zwraca otwarty plik podany w parametrze funkcji"""
    return open('./' + file + '.md', 'r')


file = input('Enter file name: ')

if os.path.exists('./' + file + '.md'):
    print(openFile(file).read())
else:
    print("File not found!")
