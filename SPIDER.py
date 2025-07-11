producto = {
    "8475HD":["HP",15.6,"8GB","DD","1T","Intel Core i5","Nvidia","GTX1050"],
    '2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
   'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
    'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
   'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
  '123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
  '342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
  'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'],
}

#stock = {modelo: [precio, stock],]
stock = {'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0],
}

#funciones para el stock 
def stock_marca(marca):
    total =0
    for claves, datos in producto.items():
        if (datos[0].lower() == marca.lower()) :
            total+= stock[claves][1]
    print(f"EL stock es de  {total}")
    
#Funcion del precio 
def precio(precio_min,precio_max) :
    resultados=[]
    for codigo, datos in stock.items():
        precio = datos[0]
        
        if precio >= precio_min and precio <= precio_max and stock[codigo][1] > 0 :
            resultados.append(producto[codigo][0] + "--" + codigo)
            
    if resultados :
        resultados.sort()
        print(f"Los notebooks entre los precios consultas son:{resultados}")
    else: 
        print ("No hay notebook disponibles para mostrar")
        
# funcion para actualizar el stock 
def actualizar_stock(codigo,nuevo_stock):
    if (codigo in producto):
        producto [codigo][1] =nuevo_stock
        return True
    return False

#base de menu()
def main ():
    try:
        while True:
            print("------------------------")
            print("-----MENU PRINCIPAL-----")
            print("------------------------")
            print("1.Stock marca           ")
            print("2.busqueda por precio   ")
            print("3.actualizar precio     ")
            print("4.salir")
            opc = int(input("ingrese su opcion: "))
            if opc == 1 :
                marca =input("Ingrese marca a consultar:")
                stock_marca(marca)
            elif opc == 2 :
                try :
                    precio_min=int(input("Ingrese el precio minimo : ").strip())
                    precio_max=int(input("Ingrese el precio maximo :").strip())
                    precio(precio_min,precio_max) 
                except ValueError :
                    print("Debe de ingresar numeros enteros ")
    
            elif opc == 3 :
                while True:
                    codigo = input("ingrese codigo de producto:")
                    try:
                        nuevo_stock =int(input("ingrese nuevo producto: "))
                        if actualizar_stock(codigo,nuevo_stock):
                            print("stock actualizado!")
                        else:
                            print("el codigo no existe!")
                    except ValueError:
                        print("debe ingresar un numero entero para el stock")
                    repetir = input("desea actualizar otro producto (s/n)?:").lower()
                    if (repetir != "s"):
                        break 
            elif opc == 4 :
                print("Programa Finalizado...")
                break
            else:
               print("Opcion no valida!!!")
               
    except ValueError :
        print("ingrese una opcion valida !!")
#Ejecutar programa 
if __name__ == "__main__" :
    main()
            
            
            
