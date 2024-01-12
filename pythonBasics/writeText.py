"""

file=open("Test.text")
file.close()
"""
# read the file and store all the list and reverse the list write the list
with open("Test.text",'r') as reader:
    content=reader.readlines()
    reversed(content)
    with open("Test.text",'w') as writer:
        for line in reversed(content):
            writer.write(line)

