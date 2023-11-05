from colorama import init, Fore

init()
r = Fore.RED
w = Fore.WHITE
b = Fore.BLUE


def shift(line=30, side=3, el='#'):
    print('Rus')
    c = ['', b, r]
    for i in range(side):
        for e in range(side):
            print(c[i] + el * line)
    print(w + '_#_')

shift(el='W')
