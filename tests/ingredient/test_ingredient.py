from src.models.ingredient import Ingredient  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    ingredient1 = Ingredient("cebola")
    ingredient2 = Ingredient("pimenta")
    assert ingredient1 != ingredient2
    assert ingredient1 == ingredient1
    assert repr(ingredient1) == "Ingredient('cebola')"
    assert hash(ingredient1) == hash("cebola")
    assert ingredient1.name == "cebola"
    assert ingredient1.restrictions == set()
