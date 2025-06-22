# Calcula el IMC usando la fórmula peso / altura²
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

# Clasifica el IMC según los rangos establecidos por la OMS
def clasificar_imc(imc):
    if imc < 18.5:
        return "Bajo peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    else:
        return "Obesidad"

# Función principal que pide datos, calcula y muestra el resultado
def main():
    print("Calculadora de IMC (Índice de Masa Corporal)")

    try:
        # Solicita el peso y la altura al usuario
        peso = float(input("Ingresá tu peso en kilogramos (kg): "))
        altura = float(input("Ingresá tu altura en metros (m): "))
        
        # Verifica que los valores sean positivos
        if peso <= 0 or altura <= 0:
            print("⚠️ El peso y la altura deben ser mayores a 0.")
            return

        # Calcula el IMC y obtiene la clasificación
        imc = calcular_imc(peso, altura)
        clasificacion = clasificar_imc(imc)

        # Muestra el resultado
        print(f"\nTu IMC es: {imc:.2f}")
        print(f"Clasificación: {clasificacion}")

    except ValueError:
        # Maneja errores si se ingresan valores no numéricos
        print("⚠️ Ingresá solo números válidos.")

# Ejecuta la función principal si se corre el archivo directamente
if __name__ == "__main__":
    main()
