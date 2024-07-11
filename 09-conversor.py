temperatura = float (input("Ingrese temperatura"))
escala = input ("es Faherenheit(F) o es celsius(C)?:").lower()

if escala == "f":
    celsius = (temperatura - 32) * 5/9
    print(celsius)
elif escala == "c":
    Faherenheit = temperatura * 1.8 + 32
    print(Faherenheit)
else:
    print("Escala incorrecta")