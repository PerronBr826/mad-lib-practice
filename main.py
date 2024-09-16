# Inputs

adjective1 = input('Adjective: ')
noun1 = input('Plural Noun: ')
noun2 = input('Plural Noun: ')
verb1 = input('Verb: ')
noun3 = input('Plural Noun: ')
verb2 = input('Verb: ')
symbol = input('Symbol: ')
adjective2 = input('Adjective: ')

# Story

story = f'F-Strings are a {adjective1.lower()} way to work with {noun1.lower()}.\n{noun1.title()} are what programmers use to refer to {noun2.lower()}.\nUsing F-Strings, you can {verb1.lower()} pieces of text, or {noun1.lower()}, with other strings or {noun3.lower()}.\nBut {verb2.upper()}! You can also use concatenation.\nConcatenation is (a/an) {adjective2.lower()} way to combine {noun1.lower()} that uses the "{symbol}" symbol.'

print(story)

