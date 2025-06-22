def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

def clasificar_imc(imc):
    if imc < 18.5:
        return "Bajo peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    else:
        return "Obesidad"

def main():
    print("Calculadora de IMC (Índice de Masa Corporal)")

    try:
        peso = float(input("Ingresá tu peso en kilogramos (kg): "))
        altura = float(input("Ingresá tu altura en metros (m): "))
        
        if peso <= 0 or altura <= 0:
            print("⚠️ El peso y la altura deben ser mayores a 0.")
            return

        imc = calcular_imc(peso, altura)
        clasificacion = clasificar_imc(imc)

        print(f"\nTu IMC es: {imc:.2f}")
        print(f"Clasificación: {clasificacion}")

    except ValueError:
        print("⚠️ Ingresá solo números válidos.")

if __name__ == "__main__":
    main()
