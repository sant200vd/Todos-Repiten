# Definir las opciones del menú
menu = {
    "a": "Hamburguesas",
    "b": "Hot-Dogs",
    "c": "Papitas",
    "d": "Ver Carrito"
}

# Definir las opciones del menú de hamburguesas con precios
menuham = {
    "a": {"nombre": "Hamburguesa Sencilla", "precio": 1.75},
    "b": {"nombre": "Hamburguesa con huevo", "precio": 2.00},
    "c": {"nombre": "Hamburguesa con queso", "precio": 2.50}
}

# Definir las opciones del menú de hot dogs con precios
menuhotdog = {
    "a": {"nombre": "Hot-Dog Clásico", "precio": 1.50},
    "b": {"nombre": "Hot-Dog con queso", "precio": 2.00},
    "c": {"nombre": "Hot-Dog con chili", "precio": 2.50},
    "d": {"nombre": "Hot-Dog delicioso", "precio": 3.00}
}

# Crear un diccionario para representar el carrito
carrito = {}

# Mensaje de bienvenida
print("¡Bienvenido/a! Por favor, seleccione una opción del menú:")

# Función para mostrar el menú de acuerdo a la sección seleccionada
def mostrar_menu_seccion(opciones_menu):
    for key, value in opciones_menu.items():
        print(f"{key}: {value['nombre']} - ${value['precio']:.2f}")

# Función para imprimir el carrito
def imprimir_carrito(carrito):
    if carrito:
        print("Carrito:")
        for item, cantidad in carrito.items():
            if item in menuham:
                nombre = menuham[item]["nombre"]
                precio_unitario = menuham[item]["precio"]
            elif item in menuhotdog:
                nombre = menuhotdog[item]["nombre"]
                precio_unitario = menuhotdog[item]["precio"]
            precio_total = precio_unitario * cantidad
            print(f"{cantidad} {nombre} - ${precio_total:.2f}")
        total = sum(
            (menuham[item]["precio"] if item in menuham else menuhotdog[item]["precio"]) * cantidad
            for item, cantidad in carrito.items()
        )
        print(f"Total: ${total:.2f}")
    else:
        print("El carrito está vacío.")

# Proceso de selección del cliente
while True:
    cliente = input("¿A cuál de nuestras secciones desea entrar? Hamburguesas (a), Hot-Dogs (b), Papitas (c), Ver Carrito (d): ").lower()

    if cliente in menu:
        if cliente == "a":
            print("Le entregamos nuestro menú de hamburguesas:")
            mostrar_menu_seccion(menuham)  # Mostrar el menú de hamburguesas
            opcion_hamburguesa = input("Por favor, elija una opción (a),(b),(c): ")
            if opcion_hamburguesa in menuham:
                confirmacion = input("¿Cuántas desea agregar al carrito?: ")
                try:
                    cantidad = int(confirmacion)
                    if cantidad > 0:
                        # Agregar la hamburguesa al carrito
                        if opcion_hamburguesa in carrito:
                            carrito[opcion_hamburguesa] += cantidad
                        else:
                            carrito[opcion_hamburguesa] = cantidad
                        print(f"{cantidad} hamburguesa(s) agregada(s) al carrito.")
                    else:
                        print("Por favor, ingrese una cantidad válida.")
                except ValueError:
                    print("Por favor, ingrese un número válido.")
            else:
                print("Opción no válida.")

        # Proceso de selección de hot-dogs
        elif cliente == "b":
            print("Le entregamos nuestro menú de hot dogs:")
            mostrar_menu_seccion(menuhotdog)
            opcion_hotdog = input("Por favor, elija una opción (a),(b),(c),(d): ")
            if opcion_hotdog in menuhotdog:
                confirmacion = input("¿Cuántos desea agregar al carrito?: ")
                try:
                    cantidad = int(confirmacion)
                    if cantidad > 0:
                        # Agregar el hot-dog al carrito
                        if opcion_hotdog in carrito:
                            carrito[opcion_hotdog] += cantidad
                        else:
                            carrito[opcion_hotdog] = cantidad
                        print(f"{cantidad} hot-dog(s) agregado(s) al carrito.")
                    else:
                        print("Por favor, ingrese una cantidad válida.")
                except ValueError:
                    print("Por favor, ingrese un número válido.")
            else:
                print("Opción no válida.")

        # Imprimir el carrito
        elif cliente == "d":
            imprimir_carrito(carrito)

        # Salir del programa
        elif cliente == "F":
            print("¡Gracias por su compra!")
            break

        else:
            print("Opción no válida.")

