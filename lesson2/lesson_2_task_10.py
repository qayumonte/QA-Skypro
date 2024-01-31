def bank(X, Y):
    procent = 0.10
    amount = X * (1 + procent) ** Y
    return amount



deposit = 1000
years = 5

result = bank(deposit, years)
print('Сумма на счету спустя', years, 'лет:', int(result), 'рублей.')