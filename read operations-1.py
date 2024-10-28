file=open('document.rtf' ,'r' )
print(file.read())
file.close()

file =open('document.rtf' ,'r' )
print("\n read in parts \n")
print(file.read(8))
file.close()

file=open('document.rtf' ,'a' )
file.write("hi im penguin im 1 year old")
file.close()
