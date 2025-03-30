print("Este programa es para gráficar objetos 3D teniendo definiendo los vertices y las caras")
print("By Kuilmer Hernandez")


# Cantidad de vertices y sus coordenadas
while True:
    try:
        vertices_totales = int(input("Ingrese la cantidad de vértices: "))
        break
    except ValueError:
        print("Error: Ingrese un valor numerico entero")
            
        
vertices = [] # Guardar todos los vertices
for i in range(vertices_totales):
    while True:
        coordenadas_vertice = input(f"Ingrese las coordenas del vértice {i+1} (x y z): ")
        try:
            x, y, z = map(int, coordenadas_vertice.split())
            vertices.append((x, y, z))
            break
        except ValueError:
            print("Error: Ingresa unicamente valores numericos enteros separados por un espacio")



# Caras de los vertices y sus uniones

while True:
    try:
        caras_totales = int(input("Ingrese la cantidad de caras: "))
        break
    except ValueError:
        print("Error: Ingrese un valor numerico entero")

caras = []
for i in range(caras_totales):
    while True:
        try:
            caras_vertices = int(input(f"Ingrese la cantidad de vertices para la cara {i+1}: "))
            break
        except ValueError:
            print("Eror: Ingresa un valor numerico entero.")
    
    while True:
        caras_indices = input(f"Ingrese los indices de lo vertices a unir para la cara {i+1}: ")
        try:
            indices_lista = list(map(int, caras_indices.split()))
            caras.append(indices_lista)
            break
        except ValueError:
            print(f"Error: Ingrese {caras_vertices} valores numericos separados por espacios")
    
    #caras.append(indices_lista)



print(f"Se han recolectado {len(vertices)} vértices y {len(caras)} caras. \n")

# Impresión en formato .obj
print("Salida en formato .obj:")
for v in vertices:
    print("v", v[0], v[1], v[2])
    
for cara in caras:
    # Se convierte la lista de índices a cadena
    indices = " ".join(map(str, cara))
    print("f", indices)
    
print(indices)