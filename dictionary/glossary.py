"""Using OrderedDict a python standary libary to make a dictionary."""
from collections import OrderedDict


glossary = OrderedDict()

glossary['numbers'] = 'A sum or total quantity of units or individuals.'
glossary['loop'] = 'repeat or go through a line of code.'
glossary['strings'] = 'A series of characters. eg'
glossary['if-statements'] = 'This introduces a conditional a clause.'
glossary['variable'] = 'a word or an alphabet that holds a value.'
glossary['list'] = 'A collection of items in a particular order.'
glossary['dictionary'] = 'This is a Python collection of key-value pairs.'


for term, meaning in glossary.items():
    print(term.title() + ": " + meaning)

