from math import sqrt
from math import pow
import matplotlib.pyplot as plt

f = open("trajbola.txt", "r")

trajbola = []
for i in f.readlines():
    i = i.replace("\n", "")
    i = i.replace(",", ".")
    i = i.split("\t")
    trajbola.append(i)
trajbola.pop(0)
tempo = []
PosXBola = []
PosYBola = []
for i in trajbola:
    tempo.append(float(i[0]))
    PosXBola.append(float(i[1]))
    PosYBola.append(float(i[2]))
f.close()

PosXRobo = list(range(1002))
PosYRobo = list(range(1002))
PosXRobo[0] = float(input("Posição inicial X do robo: "))
PosYRobo[0] = float(input("Posição inicial Y do robo: "))
distancia = list(range(1002))
cos = list(range(1002))
sen = list(range(1002))
VelXRobo = list(range(1002))
VelYRobo = list(range(1002))
VelXBola = list(range(1002))
VelYBola = list(range(1002))
AcelXBola = list(range(1002))
AcelYBola = list(range(1002))
AcelRobo = list(range(1002))
AcelMaxRobo = 2.8
rinter = 0.111


for i in range(len(tempo)):
    distancia[i] = sqrt((pow((PosXBola[i] - PosXRobo[i]), 2)) + pow((PosYBola[i] - PosYRobo[i]),2))

    if distancia[i] == 0:
        cos[i] = (PosXBola[i] - PosXRobo[i]) / 1
        sen[i] = (PosYBola[i] - PosYRobo[i]) / 1
    else:
      cos[i] = (PosXBola[i] - PosXRobo[i]) / distancia[i]
      sen[i] = (PosYBola[i] - PosYRobo[i]) / distancia[i]

    VelXRobo[i+1] = AcelMaxRobo*tempo[i] + cos[i]*VelXRobo[i]
    VelYRobo[i+1] = AcelMaxRobo*tempo[i] + sen[i]*VelYRobo[i]
    VelXBola[i] = 0.015*pow(tempo[i],2) - 0.0003*tempo[i] + 0.5
    VelYBola[i] = 0.9004 - (0.04*tempo[i])
    AcelXBola[i] = 0.03*tempo[i] - 0.0006
    AcelYBola[i] = -0.04
    AcelRobo[i] = 2.8

    if i < 1001:
        PosXRobo[i + 1] = (((pow(tempo[i], 2) * AcelMaxRobo)) / 2) + cos[i] * VelXRobo[i] + PosXRobo[i]
        PosYRobo[i + 1] = (((pow(tempo[i], 2) * AcelMaxRobo)) / 2) + sen[i] * VelYRobo[i] + PosYRobo[i]


    if PosXBola[i] - rinter <= PosXRobo[i] <= PosXBola[i] + rinter and PosYBola[i] - rinter <= PosYRobo[i] <= PosYBola[i] + rinter:
        print(f"Posicoes em X: Robo:{PosXRobo[i]}, Bola: {PosXBola[i]}")
        print(f"Posicoes em Y: Robo:{PosYRobo[i]}, Bola:{PosYBola[i]}")
        print(f"Tempo de interceptacao: {tempo[i]}")
        plt.plot(PosXRobo[0:i+1], PosYRobo[0:i+1], label="Robo")
        plt.plot(PosXBola, PosYBola, label="Bola")
        plt.axis([0,PosXBola[500],0,PosYBola[500]])
        plt.legend()
        plt.suptitle('Trajetorias da bola e do robo')
        plt.xlabel("Trajetoria em X")
        plt.ylabel("Trajetoria em Y")
        plt.show()
        plt.plot(tempo[0:i+1], PosXRobo[0:i+1], label="X robo")
        plt.plot(tempo[0:i+1], PosYRobo[0:i+1], label="Y robo")
        plt.plot(tempo[0:i + 1], PosXBola[0:i + 1], label="X bola")
        plt.plot(tempo[0:i + 1], PosYBola[0:i + 1], label="Y bola")
        plt.suptitle('X e Y do robo e da bola em funcao do tempo')
        plt.legend()
        plt.ylabel("Posicao (m)")
        plt.xlabel("Tempo (s)")
        plt.show()
        plt.plot(tempo[0:i + 1], VelXRobo[0:i + 1], label="Vx robo")
        plt.plot(tempo[0:i + 1], VelYRobo[0:i + 1], label="Vy robo")
        plt.plot(tempo[0:i + 1], VelXBola[0:i + 1], label="Vx bola")
        plt.plot(tempo[0:i + 1], VelYBola[0:i + 1], label="Vy bola")
        plt.suptitle('Vx e Vy do robo e da bola em funcao do tempo')
        plt.legend()
        plt.ylabel("Velocidade (m/s)")
        plt.xlabel("Tempo (s)")
        plt.show()
        plt.plot(tempo[0:i + 1], AcelRobo[0:i + 1], label="Ax e Ay robo")
        plt.plot(tempo[0:i + 1], AcelXBola[0:i + 1], label="Ax bola")
        plt.plot(tempo[0:i + 1], AcelYBola[0:i + 1], label="Ay bola")
        plt.suptitle('Ax e Ay do robo e da bola em funcao do tempo')
        plt.legend()
        plt.ylabel("Aceleracao (m/s²)")
        plt.xlabel("Tempo (m)")
        plt.show()
        plt.plot(tempo[0:i + 1], distancia[0:i + 1], label="Distancia relativa")
        plt.suptitle('Distancia relativa')
        plt.legend()
        plt.ylabel("Distancia (m)")
        plt.xlabel("Tempo (s)")
        plt.show()
        break