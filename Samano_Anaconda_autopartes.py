# ANACONDA autopartes
# Diego Kaleb Samano Rodriguez A01114559

class Producto:

    def __init__(self, nombre='', codigo='', costo=0, venta=0, stock=0, reorden=0, proveedor=''):
        """atributos de la clase producto"""
        self.__nombre = nombre
        self.__codigo = codigo
        self.__costo = costo
        self.__venta = venta
        self.__stock = stock
        self.__reorden = reorden
        self.__proveedor = proveedor

    def __str__(self):
        return f'{self.__nombre:<30}{self.__codigo:<10}{self.__costo:<10}{self.__venta:<10}{self.__stock:<10}' \
            f'{self.__reorden:<12}{self.__proveedor}'

    def __lt__(self, other):
        return self.__proveedor < other.__proveedor

    def __add__(self, other):
        return self.__costo + other.__costo

    def getNombre(self):
        return self.__nombre

    def getCodigo(self):
        return self.__codigo

    def getCosto(self):
        return self.__costo

    def getVenta(self):
        return self.__venta

    def getStock(self):
        return self.__stock

    def getReorden(self):
        return self.__reorden

    def getProveedor(self):
        return self.__proveedor

    def setNombre(self, nombre=''):
        self.__nombre = nombre

    def setCodigo(self, codigo=''):
        self.__codigo = codigo

    def setCosto(self, costo=0):
        self.__costo = costo

    def setVenta(self, venta=0):
        self.__venta = venta

    def setStock(self, stock=0):
        self.__stock = stock

    def setReorden(self, reorden=0):
        self.__reorden = reorden

    def setProveedor(self, proveedor=''):
        self.__proveedor = proveedor

    def altaProducto(self):
        archivo = open('ProductosINT.txt', 'a')
        archivo.write(self.__nombre + '*' + self.__codigo + '*' + str(self.__costo) + '*' + str(self.__venta) + '*' +
                      str(self.__stock) + '*' + str(self.__reorden) + '*' + str(self.__proveedor) + '\n')
        archivo.close()


class Factura:

    def __init__(self, numero='', codigo='', cliente='', direccion='', telefono='', pais='',
                 fecha='', saldo=0):
        self.__numero = numero
        self.__codigo = codigo
        self.__cliente = cliente
        self.__direccion = direccion
        self.__telefono = telefono
        self.__pais = pais
        self.__fecha = fecha
        self.__saldo = saldo

    def __str__(self):
        return f'{self.__numero:<15}{self.__codigo:<15}{self.__cliente:<20}{self.__direccion:<50}' \
            f'{self.__telefono:<15}{self.__pais:<12}{self.__fecha:<15}{self.__saldo}'

    def __lt__(self, other):
        return self.__codigo < other.__codigo

    def get_numero(self):
        return self.__numero

    def get_codigo(self):
        return self.__codigo

    def get_cliente(self):
        return self.__cliente

    def get_direccion(self):
        return self.__direccion

    def get_telefono(self):
        return self.__telefono

    def get_pais(self):
        return self.__pais

    def get_fecha(self):
        return self.__fecha

    def get_saldo(self):
        return self.__saldo

    def set_numero(self, numero=''):
        self.__numero = numero

    def set_codigo(self, codigo=''):
        self.__codigo = codigo

    def set_cliente(self, cliente=''):
        self.__cliente = cliente

    def set_direccion(self, direccion=''):
        self.__direccion = direccion

    def set_telefono(self, telefono=''):
        self.__telefono = telefono

    def set_pais(self, pais=''):
        self.__pais = pais

    def set_fecha(self, fecha=''):
        self.__fecha = fecha

    def set_saldo(self, saldo=0):
        self.__saldo = saldo

    def alta_factura(self):
        archivo = open('FacturasINT.txt', 'a')
        archivo.write(self.__numero + '*' + self.__codigo + '*' + self.__cliente + '*' +
                      self.__direccion + '*' + self.__telefono + '*' + self.__pais + '*' +
                      self.__fecha + '*' + str(self.__saldo) + '\n')
        archivo.close()


def main():

    def menu_principal():
        print('\n1. Inventarios')
        print('2. Clientes')
        print('3. Salir')
        return lee_int('Teclea la opcion: ')

    def menu_inventarios():
        print('\n1. Crear un producto')
        print('2. Metodos Get')
        print('3. Metodos Set')
        print('4. Desplegar información')
        print('5. Reporte de productos')
        print('6. Reporte reorden')
        print('7. Salir\n')
        return lee_int('Teclea la opcion: ')

    def menu_gets():
        print('\n1. Get nombre')
        print('2. Get codigo')
        print('3. Get costo')
        print('4. Get precio venta')
        print('5. Get cantidad en stock')
        print('6. Get punto de reorden')
        print('7. Get proveedor')
        print('8. Salir\n')
        return lee_int('Teclea la opcion: ')

    def menu_sets():
        print('\n1. Set nombre')
        print('2. Set codigo')
        print('3. Set costo')
        print('4. Set precio venta')
        print('5. Set cantidad en stock')
        print('6. Set punto de reorden')
        print('7. Set proveedor')
        print('8. Salir\n')
        return lee_int('Teclea la opcion: ')

    def menu_clientes():
        print('\n1. Crear factura')
        print('2. Metodos Get factura')
        print('3. Metodos Set factura')
        print('4. Reporte de facturas')
        print('5. Salir\n')
        return lee_int('Teclea la opcion: ')

    def facturas_gets():
        print('\n1. Get numero de factura')
        print('2. Get numero de cliente')
        print('3. Get nombre')
        print('4. Get direccion')
        print('5. Get telefono')
        print('6. Get pais')
        print('7. Get fecha')
        print('8. Get saldo')
        print('9. Salir\n')
        return lee_int('Teclea la opcion: ')

    def facturas_sets():
        print('\n1. Set numero de factura')
        print('2. Set numero de cliente')
        print('3. Set nombre')
        print('4. Set direccion')
        print('5. Set telefono')
        print('6. Set pais')
        print('7. Set fecha')
        print('8. Set saldo')
        print('9. Salir\n')
        return lee_int('Teclea la opcion: ')

    def lee_string(mensaje):
        svalor = ''
        while svalor == '':
            try:
                svalor = input(mensaje)
            except Exception as e:
                print('Error: ', type(e).__name__, e)
            else:
                if svalor == '':
                    print('Ingresa lo que se te indica -')
        return svalor

    def lee_int(mensaje):
        while True:
            try:
                svalor = int(input(mensaje))
            except Exception as e:
                print('Error: ', type(e).__name__, e)
                print('Teclea un entero')
            else:
                print('Valor valido')
                break
        return svalor

    def reporte_productos():
        import matplotlib.pyplot as plt
        from datetime import date
        fecha = str(date.today())
        lista = []
        acumulador_venta = 0
        acumulador_costo = 0
        total_costo = 0
        total_venta = 0
        print(200 * '_')
        print(f'{"Reporte de productos":^110}')
        print(f'{fecha:^107}')
        print(200 * '_')
        # rutina de validacion para abrir el archivo
        try:
            archivo = open('ProductosINT.txt')
        except Exception as e:
            print('Error: ', type(e).__name__, e)
            print('No se pudo abrir el archivo "ProductosINT.txt')
        else:
            for linea in archivo:
                prod = linea.split('*')
                nombre, codigo, costo, venta, stock, reorden, proveedor = prod
                producto = Producto(nombre, codigo, int(costo), int(venta),
                    int(stock), int(reorden), proveedor)
                lista.append(producto)
            # cerramos el archivo
            archivo.close()
            # ordenamos elementos dentro de la lista
            lista.sort()
            print(f'{"Producto":<30}{"Codigo":<10}{"Costo":<10}{"PVP":<10}{"Stock":<10}{"Reorden":<12}{"Proveedor"}')
            print(200 * '_')
            # arreglos para las graficas
            # lista de los proveedores
            lista_proveedores = []
            # lista de los costos de cada producto
            costo_proveedor = []
            cant_existencia = []
            codigo_producto = []
            stock_proveedor = []
            count_stock = 0
            # se inicializa al proveedor anterior como el primer elemento de la lista
            proveedor_anterior = lista[0].getProveedor()

            for elemento in lista:
                # se agrega cada producto y su cantidad a las listas siguientes
                cant_existencia.append(elemento.getStock())
                codigo_producto.append(elemento.getCodigo())
                # cual es el proveedor actual
                proveedor_actual = elemento.getProveedor()

                if proveedor_anterior == proveedor_actual:
                    # acumular al proveedor actual
                    acumulador_costo += (elemento.getStock() * elemento.getCosto())
                    acumulador_venta += (elemento.getStock() * elemento.getVenta())
                    count_stock += elemento.getStock()
                else:
                    # se agregan los elementos a los arreglos
                    lista_proveedores.append(proveedor_anterior)
                    costo_proveedor.append(acumulador_costo)
                    stock_proveedor.append(count_stock)
                    # actualizar proveedor anterior
                    proveedor_anterior = elemento.getProveedor()
                    # cambio de proveedor, entonces imprimir totales de proveedor
                    total_costo += acumulador_costo
                    total_venta += acumulador_venta
                    # totales proveedor anterior
                    print(f'\nCosto total ${acumulador_costo:<15}Total venta ${acumulador_venta}')
                    print(200 * '_')
                    print(input('Pulsa <enter> para continuar'))
                    print(200 * '_')
                    # inicia acumulacion del nuevo proveedor
                    acumulador_costo = (elemento.getStock() * elemento.getCosto())
                    acumulador_venta = (elemento.getStock() * elemento.getVenta())
                    count_stock = elemento.getStock()
                # se imprime cada elemento
                print(elemento, end='')

            lista_proveedores.append(proveedor_anterior)
            costo_proveedor.append(acumulador_costo)
            stock_proveedor.append(count_stock)

            print(f'\nCosto total ${acumulador_costo:<15}Total venta ${acumulador_venta}')
            total_costo += acumulador_costo
            total_venta += acumulador_venta
            ganancia_neta = total_venta - total_costo
            print(200 * '_')
            print(f'Gran total costo: ${total_costo:<15}Gran total venta: ${total_venta:<15}'
                  f'Ganancia neta: ${ganancia_neta}\n')
            print(200 * '_')

            # grafica de barras: proveedores y pvp
            plt.bar(lista_proveedores, costo_proveedor, label='pvp', color='y')
            plt.xlabel('Proveedores')
            plt.ylabel('pvp proveedor')
            plt.title('Inventario por proveedor de acuerdo al pvp')
            plt.legend()
            plt.show()

            # grafica de barras: productos y cantidad en stock
            plt.bar(codigo_producto, cant_existencia, label='En stock', color='r')
            plt.xlabel('Producto')
            plt.ylabel('Stock')
            plt.title('Cantidad en stock por producto')
            plt.legend()
            plt.show()

            # grafica de pie
            explode = []
            maximo = max(stock_proveedor)
            for valor in stock_proveedor:
                if valor == maximo:
                    explode.append(.2)
                else:
                    explode.append(0)
            plt.pie(stock_proveedor, labels=lista_proveedores, radius=1.5,
                autopct='%1.2f%%', shadow=True, startangle=0,
                    explode=explode)
            plt.axis('equal')
            plt.title('Porcentaje de productos por proveedor')
            plt.show()

    def reporte_reorden():
        from datetime import date
        fecha = str(date.today())
        print(f'\n{"Productos en punto de reorden":^110}')
        print(f'{fecha:^107}')
        print(200 * '_')
        lista = []
        contador = 0

        # se abre el archivo y se lee
        try:
            archivo = open('ProductosINT.txt')
        except Exception as e:
            print('Error: ', type(e).__name__, e)
            print('No se pudo abrir el archivo "ProductosINT.txt')
        else:
            for linea in archivo:
                # se añaden y separan los elementos a la lista
                prod = linea.split('*')
                nombre, codigo, costo, venta, stock, reorden, proveedor = prod
                producto = Producto(nombre, codigo, costo, venta, stock, reorden, proveedor)
                if int(stock) <= int(reorden):
                    lista.append(producto)
                    contador += 1
            archivo.close()
            # se ordenan los objetos de la lista haciendo uso de __lt__
            lista.sort()
            proveedor_anterior = lista[0].getProveedor()

            print(f'{"Producto":<30}{"Codigo":<10}{"Costo":<10}{"PVP":<10}{"Stock":<10}'
                  f'{"Reorden":<10}{"Proveedor"}')
            print('_' * 200)
            for p in lista:
                proveedor_actual = p.getProveedor()
                if proveedor_actual != proveedor_anterior:
                    enter = input('Pulsa <enter> para continuar')
                    print('_' * 200)
                    proveedor_anterior = p.getProveedor()

                print(f'{p.getNombre():<30}{p.getCodigo():<10} {p.getCosto():<10}{p.getVenta():<10}'
                      f'{p.getStock():<10}{p.getReorden():<10}{p.getProveedor()}')

    def reporte_facturas():
        import matplotlib.pyplot as plt
        from datetime import date
        fecha = str(date.today())
        print(200 * '_')
        print(f'{"Reporte de facturas":^110}')
        print(f'{fecha:^107}')
        print(200 * '_')
        lista = []
        lista_clientes = []
        lista_saldos = []
        lista_acumulados = []
        acumulador = 0
        total_facturas = 0

        try:
            archivo = open('FacturasINT.txt')
        except Exception as e:
            print('Error: ', type(e).__name__, e)
            print('No se pudo abrir el archivo "FacturasINT.txt')
        else:
            for linea in archivo:
                fac = linea.split('*')
                numero, codigo, cliente, direccion, telefono, pais, fecha, saldo = fac
                factura = Factura(numero, codigo, cliente, direccion,
                    telefono, pais, fecha, saldo)
                lista.append(factura)
            archivo.close()
            lista.sort()
            print(f'{"# Factura":<15}{"# Cliente":<15}{"Nombre":<20}{"Direccion":<50}{"Telefono":<15}{"Pais":<12}'
                  f'{"Fecha":<15}{"Saldo"}')
            print(200 * '_')
            codigo_anterior = lista[0].get_codigo()

            for elemento in lista:
                lista_clientes.append(elemento.get_codigo())
                lista_saldos.append(int(elemento.get_saldo()))
                codigo_actual = elemento.get_codigo()
                if codigo_anterior == codigo_actual:
                    acumulador += int(elemento.get_saldo())
                    lista_acumulados.append(acumulador)
                else:
                    codigo_anterior = elemento.get_codigo()
                    total_facturas += int(acumulador)
                    print(f'\nMonto por cobrar: ${acumulador}')
                    total_facturas += acumulador
                    print(200 * '_')
                    acumulador = int(elemento.get_saldo())
                    lista_acumulados.append(acumulador)
                print(elemento, end='')
            acumulador + int(elemento.get_saldo())
            print(f'\nMonto por cobrar: ${acumulador}')
            print(200 * '_')
            print(f'Total a cobrar: ${sum(lista_saldos)}')
            print(200 * '_')

            # grafica del reporte de facturas
            plt.bar(lista_clientes, lista_acumulados, label='Total por cliente', color='b')
            plt.xlabel('Clientes')
            plt.ylabel('Total a cobrar a cada cliente')
            plt.title('Total de facturas a cobrar por cliente')
            plt.legend()
            plt.show()



    print(f'\n{"ANACONDA autopartes":^56}\n')
    opcion = menu_principal()

    while opcion != 3:

        if opcion == 1:
            opcion_i = menu_inventarios()

            while opcion_i != 7:

                if opcion_i == 1:
                    nombre = lee_string('Nombre del prodcuto: ')
                    codigo = lee_string('Codigo del producto: ')
                    costo = lee_int('Costo: ')
                    venta = lee_int('Precio de venta: ')
                    stock = lee_int('Cantidad en stock: ')
                    reorden = lee_int('Punto de reorden: ')
                    proveedor = lee_string('Proveedor: ')
                    nuevo = Producto(nombre, codigo, costo, venta, stock, reorden, proveedor)
                    nuevo.altaProducto()

                elif opcion_i == 2:
                    opcion_i2 = menu_gets()
                    while opcion_i2 != 8:
                        if opcion_i2 == 1:
                            print('Nombre: ', nuevo.getNombre())
                        elif opcion_i2 == 2:
                            print('Codigo: ', nuevo.getCodigo())
                        elif opcion_i2 == 3:
                            print('Costo: ', nuevo.getCosto())
                        elif opcion_i2 == 4:
                            print('Precio de venta: ', nuevo.getVenta())
                        elif opcion_i2 == 5:
                            print('Cantidad en stock: ', nuevo.getStock())
                        elif opcion_i2 == 6:
                            print('Punto de reorden: ', nuevo.getReorden())
                        elif opcion_i2 == 7:
                            print('Proveedor: ', nuevo.getProveedor())
                        opcion_i2 = menu_gets()

                elif opcion_i == 3:
                    opcion_i3 = menu_sets()
                    while opcion_i3 != 8:
                        if opcion_i3 == 1:
                            nuevo.setNombre(lee_string('Nuevo nombre: '))
                        elif opcion_i3 == 2:
                            nuevo.setCodigo(lee_string('Nuevo codigo: '))
                        elif opcion_i3 == 3:
                            nuevo.setCosto(lee_int('Nuevo costo: '))
                        elif opcion_i3 == 4:
                            nuevo.setVenta(lee_int('Nuevo precio de venta: '))
                        elif opcion_i3 == 5:
                            nuevo.setStock(lee_int('Nueva cantidad en stock: '))
                        elif opcion_i3 == 6:
                            nuevo.setReorden(lee_int('Nuevo punto de reorden: '))
                        elif opcion_i3 == 7:
                            nuevo.setProveedor(lee_string('Nuevo proveedor: '))
                        opcion_i3 = menu_sets()

                elif opcion_i == 4:
                    print(nuevo)

                elif opcion_i == 5:
                    reporte_productos()

                elif opcion_i == 6:
                    reporte_reorden()

                opcion_i = menu_inventarios()

        elif opcion == 2:
            opcion_c = menu_clientes()

            while opcion_c != 5:

                if opcion_c == 1:
                    numero = lee_string('Numero de factura: ')
                    codigo = lee_string('Codigo de cliente: ')
                    cliente = lee_string('Nombre del cliente: ')
                    direccion = lee_string('Direccion: ')
                    telefono = lee_string('Telefono: ')
                    pais = lee_string('Pais: ')
                    fecha = lee_string('Fecha: ')
                    saldo = lee_int('Saldo: ')
                    nueva = Factura(numero, codigo, cliente, direccion, telefono, pais,
                                    fecha, saldo)
                    nueva.alta_factura()

                elif opcion_c == 2:
                    opcion_c2 = facturas_gets()
                    while opcion_c2 != 9:
                        if opcion_c2 == 1:
                            print('Numero de factura: ', nueva.get_numero())
                        elif opcion_c2 == 2:
                            print('Numero de cliente: ', nueva.get_codigo())
                        elif opcion_c2 == 3:
                            print('Nombre cliente: ', nueva.get_cliente())
                        elif opcion_c2 == 4:
                            print('Direccion: ', nueva.get_direccion())
                        elif opcion_c2 == 5:
                            print('Telefono: ', nueva.get_telefono())
                        elif opcion_c2 == 6:
                            print('Pais: ', nueva.get_pais())
                        elif opcion_c2 == 7:
                            print('Fecha: ', nueva.get_fecha())
                        elif opcion_c2 == 8:
                            print('Saldo: ', nueva.get_saldo())
                        opcion_c2 = facturas_gets()

                elif opcion_c == 3:
                    opcion_c3 = facturas_sets()
                    while opcion_c3 != 9:
                        if opcion_c3 == 1:
                            nueva.set_numero(input('Nuevo numero de factura: '))
                        elif opcion_c3 == 2:
                            nueva.set_codigo(input('Nuevo numero de cliente: '))
                        elif opcion_c3 == 3:
                            nueva.set_cliente(lee_string('Nuevo nombre: '))
                        elif opcion_c3 == 4:
                            nueva.set_direccion(lee_string('Nueva direccion: '))
                        elif opcion_c3 == 5:
                            nueva.set_telefono(input('Nuevo telefono: '))
                        elif opcion_c3 == 6:
                            nueva.set_pais(lee_string('Nuevo pais: '))
                        elif opcion_c3 == 7:
                            nueva.set_fecha(lee_string('Nueva fecha: '))
                        elif opcion_c3 == 8:
                            nueva.set_saldo(lee_int('Nuevo saldo: '))
                        opcion_c3 = facturas_sets()

                elif opcion_c == 4:
                    reporte_facturas()

                opcion_c = menu_clientes()
        opcion = menu_principal()


main()
