import socket

#para trabajar con el socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#indicamos que puerto debe escuchar
s.bind (('', 5000))
#numero de conexiones entrantes que aceptara la aplicacion
s.listen(2)
#recibe datos, devuelve un objeto que representa una tupla con los datos: IP y 
#puerto
ip, direc = s.accept()

#pide su nombre al usuario nuevo y lo agrega a la red
print("Esperando...")
ip.send("Cual es tu nombre? ")
recibido = ip.recv(1024)
nombre = recibido
print("Se ha unido el cliente " + recibido)
ip.send("Estas conectado")

while True:
   nuevo_comando = raw_input()

   if (nuevo_comando == "close"):
      ip.send(nuevo_comando)
      break;

   if ("lejano" in nuevo_comando):
      ip.send(nuevo_comando)
      recibido = ip.recv(1024)
      print("El mas lejano es " + recibido + ". Encontrado por " + nombre)
      continue

   if ("cercano" in nuevo_comando):
      ip.send(nuevo_comando)
      recibido = ip.recv(1024)
      print("El mas cercano es " + recibido + ". Encontrado por " + nombre)
      continue

ip.close()
s.close()