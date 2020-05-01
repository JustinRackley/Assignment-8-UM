fname = input("Enter file name: ")
fhand = open(fname)
x = list()
for line in fhand:
    line = line.split()
    for word in line:
        if word not in x:
            x.append(word)
x.sort()
print(x)