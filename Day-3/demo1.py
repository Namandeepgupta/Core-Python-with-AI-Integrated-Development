fobj = open('C:\\Users\\Namandeep\\Downloads\\Python\\Day3\\emp.csv','r')
s = fobj.read()
fobj.close()

print(type(s),len(s))
print("") 
print("Display file content")
print(s)