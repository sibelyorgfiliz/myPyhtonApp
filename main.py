print("Hey Wereld! Hey World!")
name ="England"
age = 125
year, month, day = 2021, "october", 4
isTrue = True
array = [345, 314, 51213, 42]
PI = 3.14
piNu = 3.14


print("name:", name, age)
print(array)
print(year, month, day)
print(PI)
print(piNu)

print(type(name))
print(type(PI))
print(type(isTrue))
print(type(day))
print(type(piNu))

####
isFull : bool = True
print("isFull--> ", isFull)

def hello(number) :
    return number+5
print(hello(5))

#
"""
multiline
comment
"""
print("Has name minder than 5 letters? :", len(name)>=5)
print(name.replace("E", "_"))
print (name.count("n"))
print("\"land\" in name? ", "land" in name)
#####
#myName = "Sibel"
#message = """
#Hello, how are you?
#Your name was {}, right?
#Do you remember me {} ?
#"""
#print(message.format(myName, myName))

myName = "Sibel"
message = f"""
Hello, how are you? 
Your name was {myName}, right?
Do you remember me {myName} ?
"""
print(message)


