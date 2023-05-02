#Test python env

def print_hello():
    animals = ['dogs', 'cat', 'hamster']
    foods = [
            'Spagetti',
            'Pizza',
            'bibimbob'
            ] # w/p trailing comma
    names = [
            'John',
            'Jane',
            'Gil-dong',
            'Dong',
            'You',
            ] # w/ trailing comma
    for f_name in names:
        print(f'hello, {f_name}')

if __name__ == '__main__':

    print_hello()
