import pytest

from data import Burger1, Burger2
from praktikum.burger import Burger


class TestBurger:
    def test_set_buns(self, mock_bun_1):  # тестируем  метод set_buns добавление булочки в бургер
        burger = Burger()
        burger.set_buns(mock_bun_1)
        assert burger.bun == mock_bun_1


    @pytest.mark.parametrize('ingredient, added_ingredient', [
        (Burger1.sauce_name, Burger1.sauce_name),
        (Burger2.filling_name, Burger2.filling_name),
        (Burger1.filling_name, Burger1.filling_name)
    ]
                             )
    def test_add_ingredient_success(self, ingredient, added_ingredient):  # тестируем метод add_ingredient добавление ингредиентов в бургер
        burger = Burger()
        burger.add_ingredient(ingredient)
        assert burger.ingredients == [added_ingredient] and len(burger.ingredients) == 1

    @pytest.mark.parametrize('ingredient, del_ingredient', [
            (Burger1.sauce_name, Burger1.sauce_name),
            (Burger2.filling_name, Burger2.filling_name),
            (Burger1.filling_name, Burger1.filling_name)
        ])
    def test_del_ingredient(self, ingredient, del_ingredient, mock_filling):  # тестируем метод remove_ingredient удаления ингредиентов из бургера
        burger = Burger()
        burger.add_ingredient(mock_filling)
        burger.add_ingredient(ingredient)
        burger.remove_ingredient(1)
        assert del_ingredient not in burger.ingredients and mock_filling in burger.ingredients


    def test_move_ingredient(self, mock_souse, mock_filling):  # тестируем метод  move_ingredient перемещения ингредиентов в бургере
        burger = Burger()
        burger.add_ingredient(mock_souse)
        burger.add_ingredient(mock_filling)
        burger.move_ingredient(0, 1)
        assert len(burger.ingredients) == 2
        assert burger.ingredients[0] == mock_filling and burger.ingredients[1] == mock_souse

    def test_get_price_burger(self, mock_bun_2, mock_souse_second, mock_filling_second):  # тестируем метод get_price вычисления конечной цены бургера
        burger = Burger()
        burger.set_buns(mock_bun_2)
        burger.add_ingredient(mock_souse_second)
        burger.add_ingredient(mock_filling_second)
        assert burger.get_price() == Burger2.burger_cost_final

    def test_get_receipt(self, mock_bun_1, mock_souse, mock_filling, mock_filling_second):  # тестируем метод get_receipt получения составляющих бургера и его стоимость
        burger = Burger()
        burger.set_buns(mock_bun_1)
        burger.add_ingredient(mock_souse)
        burger.add_ingredient(mock_filling)
        burger.add_ingredient(mock_filling_second)
        assert burger.get_receipt() == ('(==== Краторная булка N-200i ====)\n'
                                        '= sauce Соус традиционный галактический =\n'
                                        '= filling Хрустящие минеральные кольца =\n'
                                        '= filling Говяжий метеорит =\n'
                                        '(==== Краторная булка N-200i ====)\n'
                                        '\n'
                                        f'Price: {burger.get_price()}')
