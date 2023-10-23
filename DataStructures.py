# Python has its own in built data structures. They are mutable data types.
# 1.list

fruits=["Mangoes", "Oranges", "Banana", "Watermelon", 54]

print(f"I love eating {fruits[0]}")
fruits[3]="Bananas"
print(f"I dont love eating {fruits[1]}")
print(f"Eating {fruits[3]} is healthy.")

num=[11,2,5,4,-3,5,4,80]
num.sort()
num[4]=9
print(num)
# print(sorted(num))

rep=num*2
print(rep)
print(len(num))

# 2.Tuple-Behave the same as list. They are immutable data types.
cars=("Toyota","Nissan","Vitz","Mercedes")
print(cars)
tup=cars*3
print(tup)
print(tup.count("Nissan"))


# 3.Sets-unordered, not ordered
days={"Monday", "Tuesday", "Wednesday", "Thusday", "Friday"}
print(days)

# 4. Dictionary

staff_details={"Name": "Irene", "Age": 30, "Company" : "eMobilis"}
print(staff_details)
print(f"Name %s" %staff_details["Name"])