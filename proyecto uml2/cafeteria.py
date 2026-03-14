from enum import Enum

class RolEmpleado(Enum):
    Barista = "Barista"
    Mesero = "Mesero"
    Gerente = "Gerente"


class EstadoPedido(Enum):
    Pendiente = "Pendiente"
    Preparando = "Preparando"
    Entregado = "Entregado"

class Temperatura(Enum):
    Fria = "Fria"
    Caliente = "Caliente"



class Persona:

    def __init__(self, idPersona, nombre, email):
        self.idPersona = idPersona
        self.nombre = nombre
        self.email = email

    def login(self):
        print(self.nombre, "Inicio Sesión")

    def actualizarPerfil(self, nuevoEmail):
        self.email = nuevoEmail
        print("Perfil ha sido actualizado")


class Cliente(Persona):
    
    def __init__(self, idPersona, nombre, email, puntosFidelidad):
        super().__init__(idPersona, nombre, email)
        self.puntosFidelidad = puntosFidelidad
        self.historialPedidos = []

    def realizarPedido(self, pedido):
        self.historialPedidos.append(pedido)
        print("Pedido realizado por", self.nombre)
    
    def consutarHistorial(self):
        for pedido in self.historialPedidos:
            print("Pedido", pedido.idPedido)

    def canjearPuntos(self):
        if self.puntosFidelidad >=100:
            print("Descuento aplicado por puntos")
            self.puntosFidelidad -=100
        else:
            print("No tiene suficientes putnos")
    
class Empleado(Persona):

    def __init__(self, idPersona, nombre, email, idEmpleado, rol):
        super().__init__(idPersona, nombre, email)
        self.idEmpleado = idEmpleado
        self.rol = rol

    def actualizarInventario(self, inventario, ingrediente, cantidad):
        inventario.ingredientes[ingrediente] = cantidad
        print("Invetario actualizado:", ingrediente)

    def cambiarEstadoPedido(self, pedido, nuevoEstado):
        pedido.estado = nuevoEstado
        print("Estado del pedido cambiado a", nuevoEstado.value)


class ProductoBase:

    def __init__(self, idProducto, nombre, precioBase):
        self.idProducto = idProducto
        self.nombre = nombre
        self.precioBase = precioBase

class Bebida(ProductoBase):

    def __init__(self, idProducto, nombre, precioBase, tamaño, temperatura):
        super().__init__(idProducto, nombre, precioBase)
        self.tamaño = tamaño
        self.temperatura = temperatura
        self.modificadores = []

    def agregarExtra(self, extra):
        self.modificadores.append(extra)

    def calcularPrecioFinal(self):
        extra = len(self.modificadores) * 5
        return self.precioBase + extra
    
class Postre(ProductoBase):

    def __init__(self, idProducto, nombre, precioBase, esVegano, sinGluten):
        super().__init__(idProducto, nombre, precioBase)
        self.esVegano = esVegano
        self.sinGluten = sinGluten


class Inventario:

    def __init__(self):
        self.ingredientes = {}


    def reducirStock(self, ingrediente, cantidad):
        
        if ingrediente in self.ingredientes:

            if self.ingredientes[ingrediente] >= cantidad:

                self.ingredientes[ingrediente] -= cantidad
                print("Stock reducido", ingrediente)
            
            else:
                print("No hay suficiente stock")
        
        else:
            print("ingrediente no registrado")

    def notificarFaltante(self):

        for ingrediente, cantidad in self.ingredientes.items():

            if cantidad < 5:
                print("Faltan ingredientes:", ingrediente)

class Pedido:

    def __init__(self, idPedido):
        self.idPedido = idPedido
        self.productos = []
        self.estado = EstadoPedido.Pendiente
        self.total = 0

    def agregarProducto(self, producto):
        self.productos.append(producto)

    def calcularTotal(self):

        total= 0 

        for producto in self.productos:
            
            if isinstance(producto, Bebida):
                total += producto.calcularPrecioFinal()

        else:
            total += producto.precioBase
        
        self.total = total
        return total

def validarStock(self,inventario):

    if len(inventario.ingredientes) > 0:
        print("Stock verificado")
        return True
    else:
        print("Inventario vacio")
        return False