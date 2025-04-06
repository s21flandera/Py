def repeat_deco(n=1):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = None
            for _ in range(n):
                result = func(*args, **kwargs)
            return result

        return wrapper

    return decorator

code = []
while data := input():
   code.append(data)
code = "\n".join(code)
exec(code)



# Напишите декоратор, который будет принимать натуральное число n – число повторений
# – и будет повторять вызов декорированной функции n раз, а также возвращать значение
# из последнего вызова.
# Входные данные
#
# @repeat_deco(4)
# def hello():
#     print("hello")
# hello()
# Выходные данные
#
# hello
# hello
# hello
# hello