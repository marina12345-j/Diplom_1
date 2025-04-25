from data import Burger1, Burger2


class TestIngredient:
    #Проверка работы метода get_name, получающего название соуса
    def test_get_name_sauce_success(self, mock_souse):
        assert mock_souse.get_name() == Burger1.sauce_name

    #Проверка работы метода get_name, получающего название начинки
    def test_get_name_filling_success(self, mock_filling):
        assert mock_filling.get_name() == Burger1.filling_name

    #Проверка работы метода get_price, получающего стоимость соуса
    def test_get_price_sauce_success(self, mock_souse_second):
        assert mock_souse_second.get_price() == Burger2.sauce_price

    #Проверка работы метода get_price, получающего стоимость начинки
    def test_get_price_filling_success(self, mock_filling_second):
        assert mock_filling_second.get_price() == Burger2.filling_price

    #Проверка работы метода get_type, получающего тип ингредиента для соуса
    def test_get_type_sauce_success(self, mock_souse):
        assert mock_souse.get_type() == Burger1.sauce_type

    #Проверка работы метода get_type, получающего тип ингредиента для начинки
    def test_get_type_filling_success(self, mock_filling):
        assert mock_filling.get_type() == Burger1.filling_type