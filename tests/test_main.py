# Імпортуємо функції для тестування
from app.main import add, multiply

# Тестова функція: перевіряє, що add(2, 3) == 5
def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

# Тестова функція: перевіряє, що multiply(2, 3) == 6
def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(-2, 3) == -6
    assert multiply(0, 5) == 0