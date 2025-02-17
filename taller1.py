# Se usa "while" para verificar que la entrada sea un valor numérico
while True:
    try: 
        valor_producto = float(input("Ingrese el valor del producto: $"))
        valor_descuento = float(input("Ingrese el porcentaje de descuento (EX. 15 para 15%): "))
        break # Acaba el bucle
    except ValueError:
        print("Error:1 Ingresa un número válido")


# Round es para trabajar con valores mas precisos
ahorro = round(valor_producto * (valor_descuento / 100))
descuento_total = round( valor_producto - ahorro)

# Usando "," para miles.
print(f"El ahorro es de: ${ahorro:,} \nEl precio final es: ${descuento_total:,}")
