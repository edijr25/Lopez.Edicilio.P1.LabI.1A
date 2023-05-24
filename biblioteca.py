##1. Cargar datos desde archivo: Esta opción permite cargar el contenido
##del archivo "Insumos.csv" en una colección, teniendo en cuenta que
##las características de los insumos deben estar en un tipo de colección
##integrada.

#Def cargar_datos(archivo)->list recibe el nombre de un archivo como parámetro. 
# Su objetivo es cargar los datos contenidos en ese archivo y almacenarlos en una lista de diccionarios.
# Abre el archivo especificado en modo lectura utilizando el nombre de archivo indicado.
# Lee el contenido del archivo utilizando csv.reader y lo asigna a la variable lista_1.
# Se salta la primera línea del archivo utilizando next(lista_1) para omitir los encabezados.
# Inicializa una lista vacía llamada lista_dict para almacenar los datos.
# Verifica si la línea está vacía. Si es así, no realiza ninguna acción.
# Si la línea no está vacía, crea un diccionario con las claves "ID", "NOMBRE", "MARCA", "PRECIO" y "CARACTERISTICAS", utilizando los valores de la línea correspondientes a cada clave.
# Convierte el valor del precio a tipo float, eliminando el símbolo "$" utilizando float(i[3].replace("$","")).
# Agrega el diccionario a la lista lista_dict.
# Finalmente, devuelve la lista lista_dict que contiene los datos cargados desde el archivo.

def cargar_datos (nombre_de_archivo):
    import csv
    with open(nombre_de_archivo, "r", encoding="utf-8") as file:      
        lista_1 = csv.reader(file, delimiter=',')
        global lista_dict
        ##lista_1 = file.readline()
        next(lista_1) 
        lista_dict = []
        for i in lista_1:
            if i == "":
                ""
            else:
                keys = i
                lista_dict.append({"ID": keys[0], "NOMBRE": keys[1], "MARCA":keys[2],"PRECIO":float(i[3].replace("$","")),"CARACTERISTICAS":keys[4]})
        return lista_dict
##2. Listar cantidad por marca: Muestra todas las marcas y la cantidad
##de insumos correspondientes a cada una.
##def listar_cantidad_por_marca(lista:list)->none : recibe una lista de diccionarios como parámetro. 
# Su objetivo es contar la cantidad de elementos por marca 
# y mostrar el resultado por pantalla.Inicializa un diccionario vacío llamado
#  cantidad_por_marca para almacenar las cantidades por marca.
# Itera sobre los elementos de la lista y, para cada elemento:
# Obtiene la marca del elemento accediendo a la clave "MARCA" del diccionario.
# Utiliza cantidad_por_marca.get(marca, 0) para obtener el valor actual de la cantidad correspondiente a la marca.
#  Si la marca aún no está en el diccionario, devuelve 0.
# Incrementa en 1 la cantidad correspondiente a la marca en el diccionario cantidad_por_marca.

def listar_cantidad_por_marca(lista):
    cantidad_por_marca = {}
    for linea in lista:
        marca = linea['MARCA']
        cantidad_por_marca[marca] = cantidad_por_marca.get(marca, 0) + 1
    print("Cantidad de insumos por marca:")
    for marca, cantidad in cantidad_por_marca.items():
        print(f"|Marca: {marca} | Cantidad: {cantidad}|")

# 3. Listar insumos por marca: Muestra, para cada marca, el nombre y
# precio de los insumos correspondientes.
##def listar_innsumos_por_marca(lista:list):  recibe una lista de diccionarios como parámetro. 
# Su objetivo es agrupar los insumos por marca y mostrar los resultados por pantalla.
def listar_insumos_por_marca(lista):
    insumos_por_marca = {}
    for insumo in lista:
        marca = insumo['MARCA']
        if marca not in insumos_por_marca:
            insumos_por_marca[marca] = []
        insumos_por_marca[marca].append({'nombre': insumo['NOMBRE'],'precio':(insumo['PRECIO'])})
    print("Insumos por marca:")
    for marca, lista in insumos_por_marca.items():
        for insumo in lista:
            print(f"|Marca: {marca}| Nombre: {insumo['nombre']}| - Precio:${insumo['precio']}|")

# 4. Buscar insumo por característica: El usuario ingresa una
# característica (por ejemplo, "Sin Granos") y se listarán todos los
# insumos que poseen dicha característica.

#def mostrar_caracteristica (lista:list)-> caracteristica:str:  extrae las características de los 
# insumos presentes en la lista y las muestra al usuario, 
# permitiendo elegir una de ellas. 
# El valor de la característica seleccionada se retorna al final de la función.

def mostrar_caracteristica (lista):
    caracteristicas = set()
    for insumo in lista:
        insumo_caracteristicas = insumo['CARACTERISTICAS'].split ('~')
        caracteristicas.update (insumo_caracteristicas)
    print ("----CARACTERISTICAS DISPONIBLES----")
    for caracteristica in caracteristicas:
        print(f"-{caracteristica}")
    print("--------------------------------------------------")

    caracteristicaFiltrada = input("Ingrese una caracteristica: ")

    return caracteristicaFiltrada
##def filtrar_insumos_por_caracteristica(lista:list, caracteristica:str): los insumos de la lista
#  que tienen la característica especificada y muestra su información al usuario. 
#No retorna ningún valor, solo imprime la información en la consola.
def filtrar_insumos_por_caracteristica(lista, caracteristica):
    print("--------------------------------------------------")
    print("\nPRODUCTOS CON ESA CARACTERISTICA ")
    for insumo in lista:
        insumo_caracteristicas = insumo['CARACTERISTICAS'].split('~')
        if caracteristica in insumo_caracteristicas:
            print(f"ID: {insumo['ID']}")
            print(f"NOMBRE: {insumo['NOMBRE']}")
            print(f"MARCA: {insumo['MARCA']}")
            print(f"PRECIO: {insumo['PRECIO']}$")
            print(f"CARACTERISTICAS: {insumo['CARACTERISTICAS'].replace('~', ', ')}")
            print("--------------------------------------------------")

#5. Listar insumos ordenados: Muestra el ID, descripción, precio, marca
# y la primera característica de todos los productos, ordenados por
# marca de forma ascendente (A-Z) y, ante marcas iguales, por precio
# descendente.

##def listar_insumos_ordenados(lista:list):  ordena los insumos de la lista en base a la marca y
#  al precio de forma descendente, y luego imprime la información de cada insumo en el orden establecido. 
# Utiliza la función sorted para ordenar la lista de insumos. Se utiliza una función lambda como clave de
# ordenamiento,que compara primero la marca y luego el precio 
# (en orden descendente, indicado por el signo menos -)
# No retorna ningún valor, solo imprime la información en la consola.
def listar_insumos_ordenados(lista):

    insumos_ordenados = sorted(lista, key=lambda x: (x["MARCA"], -x["PRECIO"]))

    for insumo in insumos_ordenados:
        id_insumo = insumo["ID"]
        descripcion = insumo["NOMBRE"]
        precio = insumo["PRECIO"]
        marca = insumo["MARCA"]
        caracteristicas = insumo["CARACTERISTICAS"].split("~")[0] 

        print(f" ID: {id_insumo}| Descripción: {descripcion}| Precio: {precio}|Marca: {marca}| Característica: {caracteristicas}|")

# 6. Realizar compras: Permite realizar compras de productos. El usuario ingresa una marca 
# y se muestran todos los productos disponibles de esa marca. Luego, el usuario elige un producto 
# y la cantidad deseada. Esta acción se repite hasta que el usuario decida finalizar la compra.
# Al finalizar, se muestra el total de la compra y se genera un archivo TXT con la factura de la compra
# , incluyendo cantidad, producto, subtotal y el total de la compra.

def mostrar_productos_por_marca(lista, marca):
    productos_disponibles = []
    
    # Buscar productos de la marca especificada
    for insumo in lista:
        if insumo["MARCA"].lower() == marca.lower():
            productos_disponibles.append(insumo)
    
    if productos_disponibles:
        print(f"Productos disponibles de la marca '{marca}':")
        for i, producto in enumerate(productos_disponibles, 1):
            print(f"{i}. {producto['NOMBRE']} - Precio: {producto['PRECIO']}$")
        
        return productos_disponibles
    else:
        print(f"No se encontraron productos de la marca '{marca}'.")
        return []


def realizar_compra(lista):
    productos_comprados = []
    total_compra = 0.0
    
    continuar_comprando = True
    
    while continuar_comprando:
        marca_ingresada = input("Ingrese el nombre de la marca ('fin' para finalizar la compra): ")
        
        if marca_ingresada.lower() == "fin":
            continuar_comprando = False
        else:
            productos_disponibles = mostrar_productos_por_marca(lista, marca_ingresada)
            
            if productos_disponibles:
                seleccion = input("Seleccione un número de producto ('fin' para finalizar la compra): ")
                
                if seleccion.lower() == "fin":
                    continuar_comprando = False
                else:
                    if seleccion.isdigit() and int(seleccion) >= 1 and int(seleccion) <= len(productos_disponibles):
                        producto_seleccionado = productos_disponibles[int(seleccion) - 1]
                        cantidad = input("Ingrese la cantidad deseada: ")
                        
                        if cantidad.isdigit() and int(cantidad) > 0:
                            subtotal = producto_seleccionado['PRECIO'] * float(cantidad)
                            productos_comprados.append({
                                'Producto': producto_seleccionado['NOMBRE'],
                                'Cantidad': cantidad,
                                'Subtotal': subtotal
                            })
                            total_compra += subtotal
                            print(f"Producto agregado a la compra: {producto_seleccionado['NOMBRE']} - Cantidad: {cantidad}")
                        else:
                            print("Cantidad inválida. Por favor, ingrese un número válido.")
                    else:
                        print("Selección inválida. Por favor, elija un número de producto válido.")
            else:
                print(f"No se encontraron productos de la marca '{marca_ingresada}'.")

    with open("factura.txt", "w") as archivo_factura:
        archivo_factura.write("Factura de Compra\n")
        archivo_factura.write("-----------------\n")
        
        for producto in productos_comprados:
            archivo_factura.write(f"Producto: {producto['Producto']}\n")
            archivo_factura.write(f"Cantidad: {producto['Cantidad']}\n")
            archivo_factura.write(f"Subtotal: {producto['Subtotal']}$\n")
            archivo_factura.write("-----------------\n")
        
        archivo_factura.write(f"Total de la compra: {total_compra:.2f}$")
    
    print("Compra finalizada. Se ha generado la factura de la compra.")

    
# 7. Guardar en formato JSON: Genera un archivo JSON con todos los
# productos cuyo nombre contiene la palabra "Alimento".

##def guardar_productos_en_json(lista:list, nombre_archivo:str): filtra los elementos de la lista que contengan
#  la palabra "Alimento" en el valor de la clave "NOMBRE" y los guarda en un archivo JSON. 
# No retorna ningún valor, solo imprime un mensaje en la consola.
# La función lambda verifica si la palabra "Alimento" está presente en el valor de la clave "NOMBRE" 
# de cada diccionario.
# Convierte el resultado filtrado en una lista utilizando la función list.
def guardar_productos_en_json(lista, nombre_archivo):
    import json
    alimento_filtrado = list(filter(lambda insumo:'Alimento' in insumo["NOMBRE"], lista))
    
    with open(nombre_archivo, "w", encoding="UTF-8") as archivo:
        json.dump(alimento_filtrado, archivo, indent=2, ensure_ascii=False)

    print("Se han guardado los productos que contienen la palabra 'Alimento' en formato JSON.")


# 8. Leer desde formato JSON: Permite mostrar un listado de los insumos
# guardados en el archivo JSON generado en la opción anterior.

#def leer_archivo_jso(nombre_archivo:strig):cibe el nombre de un archivo como parámetro y
#  se encarga de leer y mostrar los insumos almacenados en ese archivo en formato JSON.
def leer_archivo_jso(nombre_archivo):
    import json

    # Leer insumos desde el archivo JSON
    with open(nombre_archivo, 'r',encoding="UTF-8") as archivo:
        insumos = json.load(archivo)
    if insumos:
        print("Listado de insumos:")
        for insumo in insumos:
            print(f" {insumo}\n")
            
    else:
        print("No se encontraron insumos.")

# 9. Actualizar precios: Aplica un aumento del 8.4% a todos los
# productos, utilizando la función map. Los productos actualizados se
# guardan en el archivo "Insumos.csv".

##def actualizar_precios(lista:list, key)->list: recorre una lista de insumos
#  y actualiza el precio de cada insumo multiplicándolo por 1.084,
#  lo que representa un aumento del 8.4%. Luego, retorna la lista con los insumos actualizados.
#Utiliza la función map para aplicar una función lambda a cada insumo.

def actualizar_precios(lista, key)->list:
    for insumo in lista:
        datos_actualizados = list(map(lambda insumo: {**insumo,"PRECIO": insumo[key] * 1.084}, lista))
    return datos_actualizados


## def actualizar_csv (lista)->list: recibe una lista de insumos y actualiza el archivo CSV
#  "Insumos2.csv" con los datos actualizados y muestra un mensaje.

def actualizar_csv (lista)->list:
    import csv
    with open("Insumos2.csv", "w", newline="",encoding="utf-8-sig") as file:
        fieldnames= ["ID", "NOMBRE","MARCA","PRECIO","CARACTERISTICAS"]
        contenido = csv.DictWriter(file, fieldnames=fieldnames)
        contenido.writeheader()
        for insumo in lista:
            insumo["PRECIO"] = "{:.2f}$".format(insumo["PRECIO"])
        contenido.writerows(lista)

    print("Los precios se han actualizado y guardado en el archivo 'Insumos.csv'.")

# 10. Salir del programa

#def menu ():
# representa el menú principal del programa, donde se presentan varias opciones al usuario
#  y se ejecutan las funciones correspondientes según la opción seleccionada.
def mostrar_menu ():
    import os
    flag_json = False
    flag_cargar_datos = False
    while True:
        menu = '''
╔════════════════════════════════════╗
║             MENÚ PRINCIPAL           ║
╠════════════════════════════════════╣
║ 1. Cargar datos desde archivo        ║
║ 2. Listar cantidad por marca         ║
║ 3. Listar insumos por marca          ║
║ 4. Buscar insumo por característica  ║
║ 5. Listar insumos ordenados          ║
║ 6. Realizar compras                  ║
║ 7. Guardar en formato JSON           ║
║ 8. Leer desde formato JSON           ║
║ 9. Actualizar precios                ║
║ 10. Salir del programa               ║
╚════════════════════════════════════╝
'''
        print(menu)
        opción= (int(input("Ingrese una opción: ")))

        if opción == 1:
            print("Datos cargados correctamente")
            cargar_datos("insumos.csv")
            flag_cargar_datos = True
        elif opción == 2:
            if flag_cargar_datos== False:
                print("Primero debes cargar los datos.")
            else:
                listar_cantidad_por_marca(lista_dict)
        elif opción == 3:
            if flag_cargar_datos== False:
                print("Primero debes cargar los datos.")
            else:
                listar_insumos_por_marca(lista_dict)
        elif opción == 4:
            if flag_cargar_datos== False:
                print("Primero debes cargar los datos.")
            else:
                caracteristica = mostrar_caracteristica (lista_dict)
                filtrar_insumos_por_caracteristica (lista_dict , caracteristica)
        
        elif opción == 5:
            if flag_cargar_datos== False:
                print("Primero debes cargar los datos.")
            else:
                listar_insumos_ordenados(lista_dict)

        elif opción == 6:
            if flag_cargar_datos== False:
                print("Primero debes cargar los datos.")
            else:
                listar_cantidad_por_marca(lista_dict)
                realizar_compra(lista_dict)
                

        elif opción == 7:
            if flag_cargar_datos== False:
                print("Primero debes cargar los datos.")
            else:
                insumos = (lista_dict)
                guardar_productos_en_json (insumos, "alimentos.json")
                flag_json = True
            
        elif opción == 8:
            if flag_cargar_datos== False:
                print("Primero debes cargar los datos.")
            elif flag_json == False:
                print("ERROR. Generar la lista JSON")
            else:   
                leer_archivo_jso ("alimentos.json")

        elif opción == 9:    
            datos = cargar_datos ("insumos.csv")
            precios_actualizados = actualizar_precios (datos, 'PRECIO')
            actualizar_csv (precios_actualizados)

        elif opción == 10:
            salida = input("Confirma salida (s/n):")
            if (salida == "s"):
                print("¡Hasta luego!")
                break 

        else:
            print("¡¡¡OPCION INVALIDA POR FAVOR INGRESE UNA OPCIÓN VALIDA!!!")
        os.system("pause")
        os.system("cls")


