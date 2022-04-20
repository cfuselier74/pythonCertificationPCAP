sentence = "this is a sentence"
num = "9824"
fl = "3.54"
alphanum = '234JKLDIRN'
sum = "The sum of {0} + {1} is {2}".format(10, 15, 25)

print(sentence.upper())
print(sentence.capitalize())
print(sentence.title())
print(sentence.isalpha())
print(sentence.isdigit())
print(num.isdigit())
print(fl.isdecimal())
print(alphanum.isalnum())
print(sum)

# strings are immutable and cannot be changed and only be overwritten
