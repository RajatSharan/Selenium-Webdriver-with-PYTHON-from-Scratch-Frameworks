file =open("Test.text")
#print(file.read(5))
#print(file.read())


# read line by line using readline method
"""
line=file.readline()
while line!="":
    print(line)
    line=file.readline()
file.close() 

"""

for line in file.readlines():
    print(line)
