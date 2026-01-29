s="  python pROgramming   "
print(len(s))
print(s[-1])
print(s.lower)
print(s.upper)
print(s)
print(s.strip())
print(s.replace("python","java"))

word=s.split()
print(word)
a='abc'
print(a.isalpha())
print(a.isdigit())
b="123"
print(b.isdigit())
print(s.count("p"))
print(s)
print(s.startswith("py"))
print(s.endswith("ing"))

print(s[::-1]) # reverse the string from last to first 
print(s.find("o"))



nm = "programming"
count = 0
for i in nm:
    if i in "aeiou":
        count += 1

print(count)