from unittest.mock import Mock
import pytest
from data import Burger1, Burger2


@pytest.fixture
def mock_bun_1():
    mock_bun_bun = Mock()
    """Создает мок-объект 1 для тестирования бургера."""
    mock_bun_bun.get_name.return_value = Burger1.name_bun
    mock_bun_bun.get_price.return_value = Burger1.price_bun
    return mock_bun_bun

@pytest.fixture
def mock_bun_2():
    mock_bun_bun_2 = Mock()
    """Создает мок-объект 2 для тестирования бургера."""
    mock_bun_bun_2.get_name.return_value = Burger2.name_bun
    mock_bun_bun_2.get_price.return_value = Burger2.price_bun
    return mock_bun_bun_2

@pytest.fixture
def mock_filling():
    mock_filling_1 = Mock()
    """Создает мок-объект 1 для добавления начинки в бургер."""
    mock_filling_1.get_name.return_value = Burger1.filling_name
    mock_filling_1.get_price.return_value = Burger1.filling_price
    mock_filling_1.get_type.return_value = Burger1.filling_type
    return mock_filling_1

@pytest.fixture
def mock_souse():
    mock_souse_1 = Mock()
    """Создает мок-объект 1 для добавления соуса в бургер."""
    mock_souse_1.get_name.return_value = Burger1.sauce_name
    mock_souse_1.get_price.return_value = Burger1.sauce_price
    mock_souse_1.get_type.return_value = Burger1.sauce_type
    return mock_souse_1

@pytest.fixture
def mock_filling_second():
    mock_filling_2 = Mock()
    """Создает мок-объект 2 для добавления начинки в бургер."""
    mock_filling_2.get_name.return_value = Burger2.filling_name
    mock_filling_2.get_price.return_value = Burger2.filling_price
    mock_filling_2.get_type.return_value = Burger2.filling_type
    return mock_filling_2

@pytest.fixture
def mock_souse_second():
    mock_souse_2 = Mock()
    """Создает мок-объект 2 для добавления соуса в бургер."""
    mock_souse_2.get_name.return_value = Burger2.sauce_name
    mock_souse_2.get_price.return_value = Burger2.sauce_price
    mock_souse_2.get_type.return_value = Burger2.sauce_type
    return mock_souse_2



