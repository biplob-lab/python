#my_dictionary = {'key1':'value1','key2':'value 2'}
"""#Question 1 = Create a dictionary called student with keys name, age, and grade. Print each value.

student = {"name":"Alvin","age":16,"grade":"a"}
for key, value in student.items():
    print(f"{key}:{value}") """


"""# Question 2 = Given d = {"a": 1, "b": 2, "c": 3}, write code to add a new key "d" with value 4. 
d = {"a": 1, "b": 2, "c": 3}
d["d"] = 4
print(d)"""

""" #Write code to check if the key "email" exists in a dictionary, and print a message either way.

info = {"name":"Biplob", "number":188888888 , "email": "biplobmojumder@gmail.com"}
if "email" in info:
    print("email is in the dictionary")
else:
    print("email is not in the dictionary") """

""" #Given a dictionary of fruit prices, write code to remove one fruit from it.
fruits = {"apple":20 , "bluberry": 50, "banana": 5}
del fruits["banana"]
print(fruits)
 
fruits = {"apple":20 , "bluberry": 50, "banana": 5}
avoid_keyerror = fruits.pop("mango", "not found")
print(f"mango is {avoid_keyerror}")
print(fruits) """

""" car = {"brand": "Toyota", "model": "Corolla", "year": 2022, "price": 25000}
for key,value in car.items():
    print(f"{key}: {value}") """

