from math import sqrt

def square_eq_solver(a, b, c):
    result = []
    discriminant = b * b - 4 * a * c
    if discriminant == 0:
        result.append(-b / (2 * a))
    else:
        result.append((-b + sqrt(discriminant)) / (2 * a))
        result.append((-b - sqrt(discriminant)) / (2 * a))
    return result
    
def show_result(data):
    if len(data) > 0:
        for index, value in enumerate(data):
            print(f'Корень номер {index+1} дорівнює {value:.02f}')
    else:
        print('Рівняння із заданими параметрами не має коренів')

def main():
    a, b, c = map(int, input('Будь ласка, введіть три числа через пробіл: ').split())
    result = square_eq_solver(a, b, c)
    show_result(result)

if __name__ == '__main__':
    main()