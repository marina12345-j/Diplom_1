from data import Burger1


class TestBun:
    def test_get_name_bun(self, mock_bun_1): #Проверка метода get_name - получение названия булки
        assert mock_bun_1.get_name() == Burger1.name_bun

    def test_get_price_bun(self, mock_bun_1): #Проверка метода get_price - получения стоимости булки'
        assert mock_bun_1.get_price() == Burger1.price_bun
