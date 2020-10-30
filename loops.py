colors = ["red", "blue", "green", "orange"]
for color in colors:
    print(f"The color is {color}")

# Scoping applies on the last indexed "color"
print("outside of the loop", color)

# The color is red
# The color is blue
# The color is green
# The color is orange
# outside of the loop orange