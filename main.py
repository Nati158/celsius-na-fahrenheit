def celsius_na_fahrenheit(celsius):
    return (celsius * 9/5) + 32

celsius = float(input("Podaj temperaturę w stopniach Celsiusza: "))
fahrenheit = celsius_na_fahrenheit(celsius)

print(f"{celsius} stopni Celsiusza to {fahrenheit:.2f} stopni Fahrenheit.")
