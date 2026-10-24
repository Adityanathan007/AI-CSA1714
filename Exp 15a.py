
def decision_tree(weather):
    if weather == "Sunny":
        return "Play"
    elif weather == "Rainy":
        return "Do not play"
    elif weather == "Cloudy":
        return "Play"
    else:
        return "Invalid input"

weather = input("Enter weather (Sunny/Rainy/Cloudy): ")
result = decision_tree(weather)

print("Decision:", result)
