from ast import literal_eval
import socket
import math


def lector(cadena):
   lista = []
   archivo = open(cadena)
   for linea in archivo:
      if linea[-1] == '\n':
         linea = linea[:-1]
      triada = literal_eval(linea)
      lista.append(triada)
   return lista;


def getMasLejano(punto):
   puntos = lector("puntos.txt")
   p1 = literal_eval(punto)
   mayor = puntos[0]
   dista = distancia(p1[0],p1[1],p1[2],puntos[0][0],puntos[0][1],puntos[0][2])
   for i in range (1, len(puntos)-1):
      distb = distancia(p1[0],p1[1],p1[2],puntos[i][0],puntos[i][1],puntos[i][2])
      if distb > dista:
         dista = distb
         mayor = p2
   a = mayor[0]
   b = mayor[1]
   c = mayor[2]
   respuesta = '({0}, {1}, {2})'.format(a,b,c)
   return respuesta

def getMasCercano(punto):
   puntos = lector("puntos.txt")
   p1 = literal_eval(punto)
   menor = puntos[0]
   dista = distancia(p1[0],p1[1],p1[2],puntos[0][0],puntos[0][1],puntos[0][2])
   for i in range (1, len(puntos)-1):
      distb = distancia(p1[0],p1[1],p1[2],puntos[i][0],puntos[i][1],puntos[i][2])
      if distb < dista:
         dista = distb
         menor = p2
   a = menor[0]
   b = menor[1]
   c = menor[2]
   respuesta = '({0}, {1}, {2})'.format(a,b,c)
   return respuesta

def distancia(x1,y1,z1,x2,y2,z2):
   return math.sqrt((x2-x1)*(x2-x1) + (y2-y1)*(y2-y1) + (z2-z1)*(z2-z1))


s = socket.socket()
s.connect(("localhost", 5000))

while True:
   respuesta = s.recv(5000)

   if (respuesta == "Estas conectado"):
      print("servidor >> " + str(respuesta))

      while True:
         respuesta = s.recv(5000)

         if("cercano" in respuesta):
            comando = respuesta.split(" | ")
            cercano = getMasCercano(comando[0])
            s.send(cercano)
            continue

         if("lejano" in respuesta):
            comando = respuesta.split(" | ")
            lejano = getMasLejano(comando[0])
            s.send(lejano)
            continue

         if(respuesta == "close"):
            s.close()
            break
   else:
      print("servidor >> " + str(respuesta))
      mensaje = raw_input("cliente  >> ")
      s.send(mensaje)

s.close()
