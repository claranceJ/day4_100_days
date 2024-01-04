elements = {"hydrogen": 1, "helium": 2, "carbon": 6}
elements["lithium"] = 3
print(elements)

#use .get method
print("Oxygen" in elements)
print(elements.get("oxygen"))

#identity operators- is and is not
n = elements.get("nitrogen")
print(n is None)
print(n is not None)