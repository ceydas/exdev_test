

import requests
import json
import random

# A python function that returns 5 random food facts from Food Facts API 
# https://www.programmableweb.com/api/food-facts
def food_name_extractor():
    # Get the food facts from the API
    food_facts = requests.get('https://api.nal.usda.gov/fdc/v1/foods/list?api_key=DEMO_KEY')
    food_facts = food_facts.json()
    
    # Get the food names from the food facts list
    food_names = []
    for food in food_facts[:20]:
        description = food.get('description') # use .get() to handle cases where 'description' key is missing
        if description:
            food_names.append(description)

    # Get 5 random food names from the food names list
    random_food_names = random.sample(food_names, 5)
    return random_food_names

# Prints food names as a pretty list.
def print_food_names():
    food_names = food_name_extractor()
    for food in food_names:
        print(food)

# Returns a random rating for each element in the given food names array.
def food_rating():
    food_ratings = {}
    food_names = food_name_extractor()

    for food in food_names:
        food_rating[food] = random.randint(0,5)
    
    return food_ratings


if __name__ == '__main__':
    print(food_name_extractor())
