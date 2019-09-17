thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x, y in thisdict.items():
  print(x, y)


thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if 1964 in thisdict.values():
  print("Yes, '1' is one of the keys in the thisdict dictionary")

print(len(thisdict))
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")

x=thisdict["brand"]
print(thisdict["brand"])
print(thisdict)
print(thisdict.items())


