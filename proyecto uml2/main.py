from cafeteria import *

print("---- SISTEMA CAFETERIA ----")


cliente1 = Cliente(1,"Carlos","carlos@email.com",120)
cliente2 = Cliente(2,"Ana","ana@email.com",80)
cliente3 = Cliente(3,"Luis","luis@email.com",50)
cliente4 = Cliente(4,"Maria","maria@email.com",200)
cliente5 = Cliente(5,"Pedro","pedro@email.com",30)
cliente6 = Cliente(6,"Jorge","jorge@email.com",70)
cliente7 = Cliente(7,"Fernanda","fernanda@email.com",150)
cliente8 = Cliente(8,"Diego","diego@email.com",40)
cliente9 = Cliente(9,"Sofia","sofia@email.com",90)
cliente10 = Cliente(10,"Daniel","daniel@email.com",110)

empleado1 = Empleado(2,"Laura","laura@email.com",101,RolEmpleado.Barista)
empleado2 = Empleado(11,"Diego","diego@email.com",102,RolEmpleado.Mesero)
empleado3 = Empleado(12,"Sofia","sofia@email.com",103,RolEmpleado.Gerente)
empleado4 = Empleado(4,"Miguel","miguel@email.com",104,RolEmpleado.Barista)
empleado5 = Empleado(5,"Paola","paola@email.com",105,RolEmpleado.Mesero)
empleado6 = Empleado(6,"Luis","luis@email.com",106,RolEmpleado.Barista)
empleado7 = Empleado(7,"Ana","ana@email.com",107,RolEmpleado.Mesero)
empleado8 = Empleado(8,"Pedro","pedro@email.com",108,RolEmpleado.Barista)
empleado9 = Empleado(9,"Elena","elena@email.com",109,RolEmpleado.Gerente)
empleado10 = Empleado(10,"Ricardo","ricardo@email.com",110,RolEmpleado.Mesero)


bebida1 = Bebida(1,"Latte",50,"Grande",Temperatura.Caliente)
bebida1.agregarExtra("Leche de almendra")
bebida2 = Bebida(2,"Capuccino",55,"Mediano",Temperatura.Caliente)
bebida3 = Bebida(3,"Cafe Americano",40,"Grande",Temperatura.Caliente)
bebida4 = Bebida(4,"Frappe",65,"Grande",Temperatura.Fria)
bebida4.agregarExtra("Crema batida")
bebida5 = Bebida(5,"Chocolate Caliente",60,"Mediano",Temperatura.Caliente)
bebida6 = Bebida(6,"Mocha",58,"Grande",Temperatura.Caliente)
bebida7 = Bebida(7,"Te Verde",35,"Mediano",Temperatura.Caliente)
bebida8 = Bebida(8,"Cafe Helado",45,"Grande",Temperatura.Fria)
bebida9 = Bebida(9,"Matcha Latte",62,"Mediano",Temperatura.Caliente)
bebida10 = Bebida(10,"Smoothie Fresa",70,"Grande",Temperatura.Fria)

postre1 = Postre(2,"Cheesecake",60,False,False)
postre2 = Postre(7,"Brownie",50,False,False)
postre3 = Postre(8,"Galleta",30,False,False)
postre4 = Postre(9,"Pastel de Chocolate",80,False,False)
postre5 = Postre(10,"Panque",45,False,True)
postre5 = Postre(5,"Panque",45,False,True)
postre6 = Postre(6,"Cupcake",35,False,False)
postre7 = Postre(7,"Donut",25,False,False)
postre8 = Postre(8,"Tarta de Manzana",55,False,False)
postre9 = Postre(9,"Flan",40,False,True)
postre10 = Postre(10,"Pastel de Zanahoria",65,False,False)


inventario = Inventario()
inventario.ingredientes["Cafe"] = 20
inventario.ingredientes["Leche"] = 15
inventario.ingredientes["Chocolate"] = 10
inventario.ingredientes["Harina"] = 12
inventario.ingredientes["Azucar"] = 25

pedido1 = Pedido(1001)
pedido1.agregarProducto(bebida1)
pedido1.agregarProducto(postre1)

pedido2 = Pedido(1002)
pedido2.agregarProducto(bebida2)
pedido2.agregarProducto(postre2)

pedido3 = Pedido(1003)
pedido3.agregarProducto(bebida3)

pedido4 = Pedido(1004)
pedido4.agregarProducto(bebida4)
pedido4.agregarProducto(postre3)

pedido5 = Pedido(1005)
pedido5.agregarProducto(bebida5)
pedido5.agregarProducto(postre4)

pedido6 = Pedido(1006)
pedido6.agregarProducto(bebida6)

pedido7 = Pedido(1007)
pedido7.agregarProducto(bebida7)
pedido7.agregarProducto(postre6)

pedido8 = Pedido(1008)
pedido8.agregarProducto(bebida8)

pedido9 = Pedido(1009)
pedido9.agregarProducto(bebida9)
pedido9.agregarProducto(postre7)

pedido10 = Pedido(1010)
pedido10.agregarProducto(bebida10)
pedido10.agregarProducto(postre8)

pedido1.calcularTotal()

clientes = [cliente1,cliente2,cliente3,cliente4,cliente5,cliente6,cliente7,cliente8,cliente9,cliente10]

empleados = [empleado1,empleado2,empleado3,empleado4,empleado5,empleado6,empleado7,empleado8,empleado9,empleado10]

bebidas = [bebida1,bebida2,bebida3,bebida4,bebida5,bebida6,bebida7,bebida8,bebida9,bebida10]

postres = [postre1,postre2,postre3,postre4,postre5,postre6,postre7,postre8,postre9,postre10]

pedidos = [pedido1,pedido2,pedido3,pedido4,pedido5,pedido6,pedido7,pedido8,pedido9,pedido10]


opcion = 0

while opcion != 7:

    print("\n----- MENU -----")
    print("1. Ver productos")
    print("2. Crear pedido")
    print("3. Ver total del pedido")
    print("4. Cambiar estado del pedido")
    print("5. Ver inventario")
    print("6. Ver todos los objetos del sistema")
    print("7. Salir")

    opcion = int(input("Seleccione una opcion: "))




    if opcion == 1:

        print("\n--- PRODUCTOS DISPONIBLES ---")
        print("1.", bebida1.nombre, bebida1.precioBase)
        print("2.", postre1.nombre, postre1.precioBase)




    elif opcion == 2:

        print("\nAgregar producto al pedido")

        print("1. Latte")
        print("2. Cheesecake")

        producto = int(input("Seleccione producto: "))

        if producto == 1:
            pedido1.agregarProducto(bebida1)

        elif producto == 2:
            pedido1.agregarProducto(postre1)

        print("Producto agregado")




    elif opcion == 3:

        total = pedido1.calcularTotal()
        print("Total del pedido:", total)




    elif opcion == 4:

        empleado1.cambiarEstadoPedido(pedido1,EstadoPedido.Preparando)
        print("Pedido ahora está:", pedido1.estado.value)



    elif opcion == 5:

        print("\n--- INVENTARIO ---")

        for ingrediente,cantidad in inventario.ingredientes.items():
            print(ingrediente,"-",cantidad)




    elif opcion == 7:

        print("Sistema finalizado")


    elif opcion == 6:

        print("\n----- CLIENTES -----")
        for c in clientes:
            print(c.nombre, "-", c.email, "- puntos:", c.puntosFidelidad)

        print("\n----- EMPLEADOS -----")
        for e in empleados:
            print(e.nombre, "-", e.rol.value)

        print("\n----- BEBIDAS -----")
        for b in bebidas:
            print(b.nombre, "-", b.precioBase)

        print("\n----- POSTRES -----")
        for p in postres:
            print(p.nombre, "-", p.precioBase)

        print("\n----- PEDIDOS -----")
        for p in pedidos:
            print("Pedido:", p.idPedido, "Total:", p.calcularTotal())






    else:

        print("Opcion no valida")

print("\n---- TOTALES DE PEDIDOS ----")

print("Pedido 1:", pedido1.calcularTotal())
print("Pedido 2:", pedido2.calcularTotal())
print("Pedido 3:", pedido3.calcularTotal())
print("Pedido 4:", pedido4.calcularTotal())
print("Pedido 5:", pedido5.calcularTotal())

cliente1.realizarPedido(pedido1)
cliente2.realizarPedido(pedido2)
cliente3.realizarPedido(pedido3)

empleado1.cambiarEstadoPedido(pedido1,EstadoPedido.Preparando)
empleado3.cambiarEstadoPedido(pedido1,EstadoPedido.Entregado)

inventario.reducirStock("Cafe",2)
inventario.reducirStock("Leche",1)

inventario.notificarFaltante()

cliente1.canjearPuntos()
cliente3.canjearPuntos()

print("\n---- SISTEMA FINALIZADO ----")