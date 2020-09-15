# task 2

Alphabet = []

file = open("python1.txt","rt")
lines = file.readlines()

for line in lines:
    Alphabet.append(line.replace(".", " ").replace(",", " ").replace("?", " ").replace("'", " "))
print (Alphabet)
Alphabet2 =  str(Alphabet).split()
print(Alphabet2)
d = {}
for i in Alphabet2:
    if i not in d.keys():
        d[i] = 0
    d[i] = d[i]+1
print(d)
