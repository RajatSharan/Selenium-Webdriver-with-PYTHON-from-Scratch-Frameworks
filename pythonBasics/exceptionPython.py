ItemInCart =0
"""
if ItemInCart != 2:
    raise Exception("Product cart count not match")

"""
if ItemInCart !=2:
    pass

assert(ItemInCart==0)

# Try-Catch block
#Customise
"""
try:
    with open("Filelog.text", 'r') as reader:
        reader.read()

except:
    print("Somehow try block got failed,Please check")

"""
# Python default message
try:
    with open("Filelog.text", 'r') as reader:
        reader.read()

except Exception as e:
    print(e)

finally:
    print("Clearing up resources")

