titleBuy = "BUY"
titleSell = "Sell"
stars = "*"
nameForDollar = "USD"
nameForEuro = "EUR"
nameForPound = "GBP"



#инициализация переменной (в нашем случае констант)

usd_buy = 40
usd_sell = usd_buy + (usd_buy * 0.05)

eur_buy = 42
eur_sell = eur_buy + (eur_buy * 0.05)

gbp_buy = 46
gbp_sell = gbp_buy + (gbp_buy * 0.05)


#вывод таблички
print(f"{stars:*^24}")
print(f"{titleBuy:^12}{titleSell:^12}")
print(f"{stars:<2}{usd_buy:^6}{nameForDollar:^8}{usd_sell:<6}{stars:>2}")
print(f"{stars:<2}{eur_buy:^6}{nameForEuro:^8}{eur_sell:<6}{stars:>2}")
print(f"{stars:<2}{gbp_buy:^6}{nameForPound:^8}{gbp_sell:<6}{stars:>2}")
print(f"{stars:*^24}")

#покупка - продажа (UAH-USD)
chooseCurrency = int(input("Выберите валюту для операции: 1- UAH 2-USD\n"))
if chooseCurrency == 1:
    method = int(input("1-Покупка 2- продажа\n"))
    if method == 1:
        quantityOfUSD = float(input("Введите cумму долларов для продажи: "))
        result = quantityOfUSD * usd_buy
        print(f'Ваше количество гривен:{result:>18}')
    elif method == 2:
        quantityOfUAH = float(input("Введите cумму гривен для продажи: "))
        result = quantityOfUAH // usd_sell
        remain = quantityOfUAH % usd_sell
        print(f'Ваше количество долларов:{result:>18}')
        print(f'Ваша сдача (грн):{remain:>26}')
elif chooseCurrency == 2:
    method2 = int(input("1-Покупка 2- продажа\n"))
    if method2 == 1:
        quantityOfUSD = float(input("Введите cумму гривен для покупки доллара: "))
        result = quantityOfUSD // usd_sell
        remain = quantityOfUSD % usd_sell
        print(f'Ваше количество долларов:{result:>18}')
        print(f'Ваша сдача (грн):{remain:>26}')

    elif method2 == 2:
        quantityOfUAH = float(input("Введите cумму долларов для покупки гривны: "))
        result = quantityOfUAH * usd_buy
        print(f'Ваше количество гривен:{result:>18}')
