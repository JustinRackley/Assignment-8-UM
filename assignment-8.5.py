fname = input("Enter file name: ")
fhand = open(fname)
count = 0
for email in fhand:
    email = email.rstrip()
    if not email.startswith('From ') : continue
    words = email.split()
    count += 1
    print(words[1])
print("There were", count, "lines in the file with From as the first word")
