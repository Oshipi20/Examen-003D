productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
             '2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
             'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
             'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
             'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
             '123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
             '342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
             'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050']}

stock = {'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
        'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
        'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0]}

def stock_marca():
    codigo = input("Ingrese el codigo de la marca:")
    if codigo in productos:
        print(f"Precio: {stock_marca[codigo][0]}CLP")
        print(f"Cantidad disponible:{productos[codigo][1]}")


def busqueda_precio():
   codigo: input
              
              
            

def actualizar_precio():
   nombre = input("Ingrese el nombre del producto:")
   encontrado = False
   for codigo, datos in stock_marca():
      if datos[0].lower() == nombre.lower():
         try:
            nuevo_precio = int(input("Nuevo precio (CLP)"))
            stock_marca[codigo][0] = nuevo_precio
            print("Precio actualizado correctamente")
            encontrado = True
         except: print("Precio invalido")
         break
      if not encontrado:
         print("El producto que desea buscar no se encuentra.")




while True:
   print("MENU DE TIENDA")
   print ("1. Stock marca")
   print ("2. Busqueda por precio")
   print ("3. Actualizar precio")

   opcion = input("Seleccione una opción:")
   if opcion == "1": stock_marca()
   elif opcion == "2": busqueda_precio()
   elif opcion == "3": actualizar_precio()
   elif opcion == "4": print("Programa Finalizado")
   break
else:
   print("Opción no valida, intente nuevamente")