fobj = open('C:\\Users\\Namandeep\\Downloads\\Python\\Day3\\emp.csv','r')
L = fobj.readlines()
fobj.close()

print(type(L),len(L))
print("")
print("Display file content")
print(L)