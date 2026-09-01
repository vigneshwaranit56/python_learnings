import json;

expenses = [
    {
        "id": 1,
        "category": "Food",
        "description": "Lunch",
        "amount": 500
    },
    {
        "id": 2,
        "category": "Travel",
        "description": "Cab fare",
        "amount": 300
    },
    {
        "id": 3,
        "category": "Food",
        "description": "Dinner",
        "amount": 600
    }
]


with open("expenses.json","w") as file:
    json.dump(expenses,file)

print("Saved Successfully")


with open("expenses.json","r") as file:
    expenses = json.load(file)

print(expenses)