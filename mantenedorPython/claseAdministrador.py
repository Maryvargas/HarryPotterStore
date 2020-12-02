class Cliente:
    def __init__(self,rut,nombre_completo,email,region,direccion,ciudad):
        self.rut = rut
        self.nombre_completo = nombre_completo
        self.email = email
        self.region = region
        self.direccion = direccion
        self.ciudad = ciudad

class Producto:
    def __init__(self,id_producto,nombre,precio,descripcion):
        self.id_producto = id_producto
        self.nombre = nombre
        self.precio = precio
        self.descripcion = descripcion

class Administrador:
    def __init__(self,id_administrador,nombre_administrador,contraseña):
        self.id_administrador = id_administrador
        self.nombre_administrador = nombre_administrador
        self.contraseña = contraseña

class Region:
    def __init__(self,nombre_region):
        self.nombre_region = nombre_region

class Usuario:
    def __init__(self,nombre_usuario,contraseña):
        self.nombre_usuario = nombre_usuario
        self.contraseña = contraseña
