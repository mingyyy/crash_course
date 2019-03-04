'''
10-10. Common Words: Visit Project Gutenberg (http://gutenberg.org/ ) and find a few texts you’d like to analyze .
Download the text files for these works, or copy the raw text from your browser into a text file on your computer .
You can use the count() method to find out how many times a word or phrase appears in a string .
For example, the following code counts the number of times 'row' appears in a string:
$ line = "Row, row, row your boat" >>> line.count('row')
2
$ line.lower().count('row')
3
Notice that converting the string to lowercase using lower() catches all appearances of the word you’re looking for,
regardless of how it’s formatted .
Write a program that reads the files you found at Project Gutenberg and determines
how many times the word 'the' appears in each text .
'''

from os import listdir
mypath = "/Users/Ming/Documents/CodingNomads/2019_crashcourse/week3/lunes"

for i in listdir(mypath):
    if i[:2] == "gp":
        n = 0
        book = ""
        filename = i
        with open(i, "r") as f:
            book = f.read()
            n = book.lower().count('the')

        print(f"There are {n} 'the' in text file '{i}'.")


