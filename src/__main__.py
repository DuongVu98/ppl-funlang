from src.core import fun

if __name__ == '__main__':
    while True:
        text = input('fun > ')
        result, error = fun.run('<stdin>', text)

        if error:
            print(error.as_string())
        else:
            print(result)
