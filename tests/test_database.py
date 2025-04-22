from conftest import *
from data import TestDataBase


class TestDB:

    @pytest.mark.parametrize('index_bun, bun_name, bun_price', TestDataBase.test_data_base_buns)
    def test_available_buns_db_success(self, db, index_bun, bun_name, bun_price):  # проверка метода available_buns получения списка доступных булок из базы (имя и стоимость булки)
        buns_data = db.available_buns()
        assert buns_data[index_bun].get_name() == bun_name and buns_data[index_bun].get_price() == bun_price


    @pytest.mark.parametrize('index_i, type_ingredient, name_ingredient, price_ingredient',
                             TestDataBase.test_data_base_ingredients)
    def test_available_ingredients_db_success(self, db, index_i, type_ingredient, name_ingredient, price_ingredient):  # проверка метода available_ingredients получения списка доступных ингредиентов из базы (имя и стоимость булки)
        ingredients_data = db.available_ingredients()
        assert (ingredients_data[index_i].get_name() == name_ingredient and
                ingredients_data[index_i].get_type() == type_ingredient and
                ingredients_data[index_i].get_price() == price_ingredient)