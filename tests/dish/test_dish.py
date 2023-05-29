from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient, Restriction
import pytest


# Req 2
def test_dish():
    dish1 = Dish("feijoada", 10.00)
    dish2 = Dish("feijoada", 10.00)
    dish3 = Dish("strogonoff", 15.00)
    rice = Ingredient("arroz")
    meat = Ingredient("carne")
    dish1.add_ingredient_dependency(rice, 2)
    dish1.add_ingredient_dependency(meat, 3)
    assert dish1.name == "feijoada"
    assert dish1.__eq__(dish3) is False
    assert dish1.__eq__(dish2) is True
    assert repr(dish1) == "Dish('feijoada', R$10.00)"
    assert hash(dish1) == hash(dish2)
    assert hash(dish1) != hash(dish3)
    assert dish1.get_ingredients() == {
        Ingredient("arroz"), Ingredient("carne")}
    assert dish1.get_restrictions() == {
        Restriction.ANIMAL_MEAT, Restriction.ANIMAL_DERIVED}
    with pytest.raises(ValueError):
        Dish("feijoada", 0)
    with pytest.raises(TypeError):
        Dish("feijoada", "value")
