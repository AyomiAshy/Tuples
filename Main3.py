weather = (1, 0, 0, 0, 1, 1, 0)
rainy = weather.count(1)
sunny = weather.count(0)
print("Rainy days:", rainy)
print("Sunny days:", sunny)
if rainy > sunny:
    print("Predicted weather: Rainy")
elif sunny > rainy:
    print("Predicted weather: Sunny")
else:
    print("Predicted weather: Uncertain")