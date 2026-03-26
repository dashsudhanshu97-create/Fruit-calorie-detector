calories = {
    "banana": 89,
    "apple": 95,
    "orange": 62,
    "mango": 60
}

def calculate_calories(count_dict):
    total = 0
    details = {}

    for fruit, qty in count_dict.items():
        cal = calories.get(fruit, 0) * qty
        details[fruit] = cal
        total += cal

    return total, details