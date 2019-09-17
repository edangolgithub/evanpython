a = "Hello, World!"
print(a[1])  # same
b = "Hello, World!"
print(b[2:5])
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"
a = "Hello, World!"
print(len(a))
a = "Hello, World!"
print(a.upper())
a = "Hello, World!"
print(a.replace("H", "J"))
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']
b=a.split(",")
print(b[1])

print("Enter your name:")
x = input()
print("Hello, ", x)