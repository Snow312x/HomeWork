# Работа с переменными
# Задачи:
# - Создай переменную с именем str_variable типа str со значением "Hello, world!"
# - Создай переменную с именем int_variable типа int со значением 100
# - Создай переменную с именем float_variable типа float со значением 1.55


### Твой код вместо ...
...

### Чтобы проверить свой код нужно запустить этот файл:
### python task.py
if __name__ == "__main__":
    # Это код для проверки решения.
    assert str_variable == "Hello, world!", f"Wrong value of 'str_variable', given: '{str_variable}', expected: 'Hello, world!'"
    assert int_variable == 100, f"Wrong value of 'int_variable', given: {int_variable}, expected: 100'"
    assert float_variable == 1.55, f"Wrong value of 'float_variable', given: {float_variable}, expected: 1.55"
    print("All tests passed! Great job!")