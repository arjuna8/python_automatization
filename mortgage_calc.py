full_lot_price = int(input("Стоимость объекта недвижимости: "))
first_intake_percent = float(input("ПВ(%): "))
interest = float(input("Ставка по ипотеке: "))
period = float(input('Срок ипотеки (лет): '))
first_intake = full_lot_price * (first_intake_percent / 100)
i = interest / 100 / 12
K = (i + (i)/((1+i)**(period*12) - 1))
mensual_payment = (full_lot_price - first_intake) * K
period = int(period)
print("Расчет ипотеки:")
print("Стоимость лота:", int(full_lot_price), "руб.")
print(f"Первый взнос :", int(first_intake), "руб.")
print('Ставка (%): ', interest)
print("Срок ипотеки (лет):", period)
print(f"Платеж по ипотеке: {round(mensual_payment, 0)} руб.")
print(f"Полная стоимость кредита за {period} лет: ", round((mensual_payment*period*12) - (full_lot_price - first_intake), 0), 'руб.')