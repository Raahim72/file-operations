file = open('document.rtf' , 'r')
print("reading first line...")
print(file.readline())
file.close()

file = open('document.rtf' , 'r')
print("reading multiple line...")
print(file.readline())
print(file.readline())
print(file.readline())
file.close()

file = open('document.rtf' , 'r')
print("looping through thr lines")
for line in file:
 print(line)
file.close()