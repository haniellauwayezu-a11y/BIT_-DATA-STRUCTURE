import array

quantities = [5, 12, 8, 20, 15]

total = sum(quantities)
average = total / len(quantities)
print("Quantities:", quantities)
print("Total =", total, "Average =", round(average, 2), 
      "Min =", min(quantities), "Max =", max(quantities))
print()

print(f"Report: Total items = {total}, Average = {average:.2f}")
print(f"Highest quantity is {max(quantities)} and lowest is {min(quantities)}")
print()

threshold = 10
if average > threshold and max(quantities) > threshold:
    print("Status: Above Standard")
else:
    print("Status: Below Standard")
print()

items = ["milk", "bread", "eggs", "butter"]
print("Items before:", items)
items.append("cheese")
items.remove("bread")
items.sort()
print("Items after:", items)
print()

arr = array.array("i", [5, 12, 8])
print("Array:", arr.tolist())
print("Array sum =", sum(arr), " | List sum =", sum(quantities))
print()

records = [
    {"id": 1, "name": "milk", "value": 5},
    {"id": 2, "name": "eggs", "value": 12},
    {"id": 3, "name": "butter", "value": 8},
]

records[0]["value"] = 10
records = [r for r in records if r["id"] != 2]
value_total = sum(r["value"] for r in records)
print("Records:", records)
print("Total values =", value_total)