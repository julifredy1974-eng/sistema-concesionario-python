import json
class Vehiculo:
    def __init__(self, marca, modelo, precio):
        self.marca = marca
        self.modelo = modelo
        self.precio = precio

    def a_diccionario(self):
      
        return {
            "marca": self.marca,
            "modelo": self.modelo,
            "precio": self.precio
        }

class Moto(Vehiculo):
  
    def __init__(self, marca, modelo, precio, cilindrada):
        super().__init__(marca, modelo, precio)
        self.cilindrada = cilindrada

    def a_diccionario(self):
        datos = super().a_diccionario() 
        datos["cilindrada"] = self.cilindrada
        datos["tipo"] = "Moto"
        return datos

class Carro(Vehiculo):
   
    def __init__(self, marca, modelo, precio, puerta):
        super().__init__(marca, modelo, precio)
        self.puerta = puerta

    def a_diccionario(self):
        datos = super().a_diccionario() 
        datos["puerta"] = self.puerta
        datos["tipo"] = "Carro"
        return datos
def guardar_vehiculos(lista_vehiculos, archivo="vehiculos.json"):
    with open(archivo, "w", encoding="utf-8") as f:
        json.dump(lista_vehiculos, f, indent=4)
    print("Guardado con exito")
def cargar_vehiculos(archivo="vehiculos.json"):
    try:
        with open(archivo, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError,json.JSONDecodeError):
        return []


#Menu
nuevo = cargar_vehiculos()
while True:
  print ("\n---Concesionario---")
  print("1. Moto")
  print("2. Carro")
  print("3. Mirar")
  print("4. Salir")
  opcion=int(input("Que opcion escoges?"))
  if opcion==1:
    marca=input("Marca de la moto")
    modelo=input("Modelo de la moto")
    precio=int(input("Precio de la moto"))
    cilindrada=int(input("Cilindrada de la moto"))
    moto1=Moto(marca,modelo,precio,cilindrada)
    nuevo.append(moto1.a_diccionario())
    guardar_vehiculos(nuevo)
  if opcion==2:
    marca=input("Marca del carro")
    modelo=input("Modelo del carro")
    precio=int(input("Precio del carro"))
    puerta=int(input("Numero de puertas"))
    carro1=Carro(marca,modelo,precio,puerta)
    nuevo.append(carro1.a_diccionario())
    guardar_vehiculos(nuevo)
  if opcion==3:
    for i in nuevo:
      print(i)
  if opcion==4:
    break