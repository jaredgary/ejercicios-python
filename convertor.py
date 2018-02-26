# -*- coding: utf-8 -*-

def foreign_exchange_calculator(amount):
    mex_to_col_rate = 145.97

    return mex_to_col_rate * amount

def run():
    print('CONVERTOR DE DIVISAS')
    print('Convierte pesos mexicanos a colombianos.')
    print('')

    amount = float(raw_input('Ingresa la cantidad de pesos mexicanos: '))

    result = foreign_exchange_calculator(amount)

    print('${} pesos mexicanos son ${} pesos colombianos'.format(amount, result))
    print('')

if __name__ == '__main__':
    run()