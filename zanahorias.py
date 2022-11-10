import numpy as np

terreno = np.terreno = [[3, 1, 1], [2, 5, 1], [1, 5, 5], [2, 1, 1]]
robotA = terreno[0][0]
del (terreno[0][0])
robotB = terreno[0][1]
del (terreno[0][1])
totalRobotA = robotA
totalRobotB = robotB

robotA = terreno[1][0]
del (terreno[1][0])
totalRobotA = robotA+totalRobotA

robotB = terreno[1][0]
del (terreno[1][0])
totalRobotB = robotB+totalRobotB

robotA = terreno[2][1]
del (terreno[2][1])
totalRobotA = robotA+totalRobotA

robotB = terreno[2][1]
del (terreno[2][1])
totalRobotB = robotB+totalRobotB

robotA = terreno[3][0]
del (terreno[3][0])
totalRobotA = robotA+totalRobotA

robotB = terreno[3][1]
del (terreno[3][1])
totalRobotB = robotB+totalRobotB

print("El máximo de Zanahorias que puede recolectar el robot A:",
      totalRobotA, "Zanahorias")
print("El máximo de Zanahorias que puede recolectar el robot B:",
      totalRobotB, "Zanahorias")

# Para ejecutar el programa pegar el codigo en https://www.programiz.com/python-programming/online-compiler/
