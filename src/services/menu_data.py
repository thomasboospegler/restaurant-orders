from models.ingredient import Ingredient
from models.dish import Dish
import pandas as pd


# Req 3
class MenuData:
    def __init__(self, source_path):
        self.dishes = set()
        self.csv_data = pd.read_csv(source_path)
        dishes_list = {}
        for data in self.csv_data.itertuples(index=False):
            name, ingredient, amount, price = data
            if name not in dishes_list:
                new_dish = Dish(name, price)
                dishes_list[name] = new_dish
                self.dishes.add(new_dish)
            ingredient = Ingredient(ingredient)
            dishes_list[name].add_ingredient_dependency(
                ingredient, amount
            )
