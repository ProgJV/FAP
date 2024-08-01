temp_celsius = float(
    input('Digite a temperatura em Celsius:')
    )
print(temp_celsius)
print(type(temp_celsius))

temp_fahren = temp_celsius * 1.8 + 32
print("A temperatura em Celsius de",
      temp_celsius, "é de",temp_fahren, 
      "Fahrenheit")


