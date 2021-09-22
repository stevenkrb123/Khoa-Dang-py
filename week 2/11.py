def convert(kilograms):
    result = []
    for i in kilograms:
        pounds = float(i) * 2.2
        result.append(pounds)
    return result

kg = input("Type weight in kilograms \n")
kilograms = kg.split()
pounds = convert(kilograms)
print('Weight in kilograms {}. '\
      ' Pounds {} '.format(kilograms, pounds))
