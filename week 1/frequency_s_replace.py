# count charecter frequency of a string 


s  = "apple"

for ch in s:
    print(ch , ":" , s.count(ch))


# replace vowels with star 

s = "python"
result = ""

for ch in s:
    if ch in "aeiou":
        result = result + "*"
    else:
        result +=ch
print(result)