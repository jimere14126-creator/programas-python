# p006-conversor-temperatura.py
#convertir temperatura de grados celsius a farenheit

print("convirtiedo grados celcius a grados farenheit  \n")

celcius  = float(input("ingresa la temperatura en grados celcius: "))
fahrenheit = (celcius * 9/5) + 32
print(f"La temperatura en Fahrenheit es: {fahrenheit:.2f}°F")