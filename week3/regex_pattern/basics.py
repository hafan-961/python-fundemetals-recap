import re
# text = "cat cot cut c&t c8t"
# result = re.findall("c.t" ,text)
# print(result)

'checking starting of a string '
# text = "Hello World"
# print(bool(re.search("^Hello", text)))
# print(bool(re.search("^World", text)))

'checking ending of a string '
# text  = "Hello World"
# print(bool(re.search("World$", text)))
# print(bool(re.search("Hello$" ,text)))


'0 or more (*)'
# text = "heloooo"
# result = re.findall("lo*" , text)
# print(result)

'one or more (+)'
# text = "heloooo"
# result = re.findall("lo+" , text)
# print(result)

'zero or one time'
# text  = "color colour"
# result = re.findall("colou?r", text)
# print(result)

'charecter set []'
# text = "apple ball cat"
# result = re.findall("[abc]" , text)
# print(result)

'Digits [0-9]'
# text = 'My age is 30'
# result = re.findall("[0-9]" , text)
# print(result)

'[a-z]'
# text = 'My age is 30'
# result = re.findall("[a-z]" , text)
# print(result)

'[A-Z]'
# text = 'My age is 30'
# result = re.findall("[A-Z]" , text)
# print(result)

'[A-Za-z]'
# text = "My age is 40"
# result = re.findall("[A-Za-z]",text)         
# print(result)


'only digits (\d)'
# text = "Marks: 90"
# result  = re.findall("\d" , text)
# print(result)

'non digits (\D)'
text = "Marks: 90"
result  = re.findall("\D" , text)
print(result)


'words (\w)'
# text = "Marks: 90"
# result  = re.findall("\w" , text)
# print(result)

'not words (\W)'
# text = "Marks: 90"
# result  = re.findall("\W" , text)
# print(result)


'space(\s)'
# text = "Marks: 90"
# result  = re.findall("\s" , text)
# print(result)

'not space (\S)'
# text = "Marks: 90"
# result  = re.findall("\S" , text)
# print(result)


'repetitioin count {}'
# text = "phone: 8739391923"
# result = re.findall("\d{10}" , text)
# print(result)


 
'OR operator'
# text = "I have a cat and a dog"
# result = re.findall("cat|dog" , text)
# print(result)

'grouping ()'

text = "abab ab"
result = re.findall("(ab)+" , text)
print(result)
