# extract email from a string
# r"[\w.-]+@[\w.-]+\.\w+"

import re
# text='Contact us at test@gmail.com or admin@yahoo.com'
# pattern=r"[\w.-]+@[\w.-]+\.\w+"
# emails=re.findall(pattern,text)
# print(emails)


'Q order123 price45 quantity'
# text = "order123 price45 quantity"
# result=re.findall(r"\d+",text)
# print(result)

'Q validate a strong password'
    # -At least 8 char
    # -one uppercase
    # -one lowercase
    # -one digit
    # -one special char
text = "!THAGVgb89*"
pattern=r"^(?=.[a-z])(?=.[A-Z])(?=.\d)(?=.[@$!%*?&]).{8,}"
result= re.findall(pattern,text) 
print(result)

