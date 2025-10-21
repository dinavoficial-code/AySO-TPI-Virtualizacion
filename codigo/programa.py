# Programa por Daniela Velazquez y Cristian Tapia - 2025

#=============================================================================#
#======================== Defino el programa principal =======================#
#=============================================================================#

def programa_principal():
    def NombreArchivo():
        # Guardo el nombre del archivo en variable para reutilizarlo o cambiarlo en todas las coincidencias
        nombre_archivo = "productos.txt"
        return nombre_archivo
    
    def DirArchivo():
        # Importo modulo pathlib para usar metodo Path y verificar si existe el archivo
        from pathlib import Path
        # Guardo el directorio del archivo
        directorio_archivo = Path('./codigo/'+NombreArchivo())
        return directorio_archivo
    
    # Defino metodo para verificar si existe el archivo
    def ExisteArchivo(archivo):
        return archivo.is_file()
    
    # Defino metodo para pedir precio y devolverlo sin tener errores de entrada
    def PedirPrecio():
        while True:
            precio = input("\nIngrese el precio del producto: ").strip()
            import re
            # Expresion regular para validar si la cadena es numero decimal positivo
            chars_permitidos = re.compile(r"^\d+(\.\d+)?$")
            precio_formato = precio.replace(",", ".")
            if chars_permitidos.match(precio_formato): 
                precio_final = float(precio_formato)
            else:
                print("\n ⚠️  Ingrese un precio valido (numero entero mayor a 0).")
                continue
            break
        if precio_final.is_integer():
            return int(precio_final)
        return precio_final
    
    # Defino metodo para pedir el nombre del producto al usuario
    def PedirNombre():
        while True:
            nombre = input("\nIngrese el nombre del producto: ").strip().capitalize()
            if not nombre.isalpha():
                print(f"\n⚠️  El nombre no debe estar vacio y debe estar formado por letras.")
                continue
            if len(nombre) < 2:
                print(f"\n⚠️  El nombre es demasiado corto.")
                continue
            return nombre

    # Defino metodo para pedir la cantidad y devolverla sin errores de entrada
    def PedirCantidad():
        while True:
            cantidad = input("\nIngrese las unidades que desea agregar: ").strip()
            if not cantidad.isdigit():
                print("\n ⚠️  Ingrese una cantidad valida (numero entero mayor a 0).")
                continue
            # Despues de verificar que no hayan signos especiales transformo a entero
            cantidad = int(cantidad)
            if cantidad <= 0:
                print("\n ⚠️  Ingrese una cantidad valida (numero entero mayor a 0).\n")
                continue
            break
        return cantidad

    # Defino metodo para agregar productos al txt sin sobreescribir
    def AgregarNuevoProducto():
            archivo = DirArchivo()
            nombre = PedirNombre()
            precio = PedirPrecio()
            cantidad = PedirCantidad()
            with open(archivo, "a") as productos:
                productos.write(f"\n{nombre},{precio},{cantidad}")
                
    def ProductosListaFormato():
        archivo = DirArchivo()
        # Defino lista con lineas que se van a formatear una vez leidas las del txt
        lineas_formateadas = []
        # Leo archivo productos.txt anteriormente creado
        with open(archivo, "r") as productos:
            lineas = productos.readlines()
            for linea in lineas:
                lineas_formateadas.append(linea.strip().split(","))
            return lineas_formateadas

    def ListaProductosDict():
        # Lista con diccionario de productos
        lista_productos = []
        for nombre,precio,cantidad in ProductosListaFormato():
            lista_productos.append({"Producto": nombre ,"Precio" : precio , "Cantidad": cantidad})
        return lista_productos

    def MostrarTablaProductos():
        archivo = DirArchivo()
        if ExisteArchivo(archivo):
            print("\n"+"="*54)
            print(" "*18+"Tabla de productos"+" "*18)
            print("="*54)
            for producto in ListaProductosDict():
                for clave, valor in producto.items():
                    print(f"{clave}: {valor}")
                print("="*54)
        else:
            print(f"\nError: El archivo '{archivo}' no existe .")
            
    
    # Defino metodo para consultar por un producto en especifico y lo muestro en pantalla
    def MostrarProductoConsulta():
        producto_consulta = PedirNombre()
        encontrado = False
        for producto in ListaProductosDict():
            if producto.get("Producto") == producto_consulta:
                encontrado = True
                print("="*54)
                for clave, valor in producto.items():
                    print(f"{clave}: {valor}")
                print("="*54)
                break
        if not encontrado:
            print("\n ⚠️  El producto ingresado no se encuentra dentro del catalogo.\n")
    
    
    def EditarStock():
        menu_editar_stock = ["1. Agregar stock",
                    "2. Sacar stock",
                    "3. Modificar precios",
                    "4. Salir"]
        while True:
            # Mostramos las opciones del menu al usuario
            print("\n"+"="*54)
            print("Elija la opción deseada")
            print("="*54)
            for opcion in menu_principal:
                print(opcion)
            print("="*54)
            # Pedimos al usuario que seleccione una de las opciones
            seleccion = input("Opción seleccionada: ").strip()
            print("="*54)
            match seleccion:
                # En cada opcion debe permitir agregar 0, como metodo de salir del proceso sin modificaciones
                case "1":
                    # Logica para agregar stock
                    ## Si existe el producto, permitir agregar stock, maximo 100 de cada producto
                    ## Si no existe pass y dar mensaje de que no existe el producto
                    pass
                case "2":
                    # Logica para sacar stock
                    ## Si existe el producto, permitir sacar stock, maximo la cantidad que tenga el stock,el minimo tiene que ser mas que 0
                    pass
                case "3":
                    # Logica para cambiar el precio de un producto:
                    ## Si existe el producto, permitir cambiar el precio, menor a 5 cifras
                    ## Si no existe pass y dar mensaje de que no existe el producto
                    pass
                case "4":
                    print("Saliendo al menu principal...\n")
                    break
                # Opcion inválida
                case _:
                    print("⚠️  Opción inválida. Por favor, elija una opción del 1 al 3.\n")
                    continue            
#===================================================================================#

    def CrearTXT():
        # Defino lista lineas con las lineas con productos que va a contener el txt
        lineas = ["Remera,1500,15\n",
                "Pantalon,2000,15\n",
                "Campera,2500,20"]
        # Creo archivo txt con productos
        with open(DirArchivo(), "w") as productos_w:
            productos_w.writelines(lineas)
            
    menu_principal = ["1. Crear o sobreescribir archivo con lista de productos nuevos",
                    "2. Mostrar tabla de productos disponibles",
                    "3. Consultar precio y stock de un producto",
                    "4. Agregar producto",
                    "5. Modificar stock (Cantidad disponible, precios)",
                    "6. Salir"]
    while True:
        # Mostramos las opciones del menu al usuario
        print("\n"+"="*54)
        print("Bienvenido al catálogo de productos, elija una opción")
        print("="*54)
        for opcion in menu_principal:
            print(opcion)
        print("="*54)
        # Pedimos al usuario que seleccione una de las opciones
        seleccion = input("Opción seleccionada: ").strip()
        print("="*54)
        match seleccion:
            case "1":
                CrearTXT()
            case "2":
                MostrarTablaProductos()
            case "3":
                MostrarProductoConsulta()
            case "4":
                AgregarNuevoProducto()
            case "5":
                pass
            case "6":
                print("Saliendo del programa... ¡Hasta luego!\n")
                break
            # Opcion inválida
            case _:
                print("⚠️  Opción inválida. Por favor, elija una opción del 1 al 7.\n")
                continue            
    
#=========================================================================================#
#                              Ejecuto el programa principal                              #
#=========================================================================================#
programa_principal()
#=========================================================================================#