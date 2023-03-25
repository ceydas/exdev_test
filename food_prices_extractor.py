import food_name_extractor
import random


# Returns a random price dictionary for each element in the food names array.
def food_price_extractor():
    food_names = food_name_extractor.food_name_extractor()

    food_prices = {}

    for food in food_names:
        food_prices[food] = round(random.uniform(5, 25), 2)
    
    return food_prices



food_price_extractor()
