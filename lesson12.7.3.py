per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input())
bank1 = per_cent.get('ТКБ') * money // 100
bank2 = per_cent.get('СКБ')* money // 100
bank3 = per_cent.get('ВТБ')* money // 100
bank4 = per_cent.get('СБЕР')* money // 100
deposit = [int(bank1),int(bank2),int(bank3),int(bank4)]
print(deposit)


print(f'Максимальная сумма, которую вы можете заработать -{max(deposit)}')
