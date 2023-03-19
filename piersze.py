
var1 = "Python 2023"
var2 = var1
var3 = var1

#a
print(var1 == var2)
print(var2 == var3)

#b
print(type(var1), hex(id(var1)))
print(type(var2), hex(id(var2)))
print(type(var3), hex(id(var3)))

var3 = "Java 11"

print(var2 == var3)

print(type(var1), hex(id(var1)))
print(type(var2), hex(id(var2)))
print(type(var3), hex(id(var3)))
