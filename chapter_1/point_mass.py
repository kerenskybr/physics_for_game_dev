import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Codigo de exemplo pra o calculo do centro de gravidade de 3 ou mais objetos combinados
# Por exemplo, um aviao: corpo e asas, cada um com peso e centro gravidades
# o resultado final deve ser o centro de gravidade do objeto como todo

# por que so me interesso por coisa dificil -_-


class PointMass:
    def __init__(self, mass, designPosition, correctedPosition):
        self.mass = mass # Kg
        self.designPosition = designPosition # metros
        self.correctedPosition = correctedPosition

PointMassElements = []

_NUMELEMENTS = 3  

# for i in range(_NUMELEMENTS):
#     mass = 10.0  # massa de cada objeto
#     design_position = [i, i, i]  # coordenadas X, Y e Z desejadas
#     corrected_position = [0, 0, 0]  

#     point_mass = PointMass(mass, design_position, corrected_position)
#     PointMassElements.append(point_mass)

# Objeto 1
point_mass = PointMass(10.0, [2, 0, 0], [0, 0, 0])
PointMassElements.append(point_mass)

# Objeto 2
point_mass = PointMass(5.0, [0, 3, 0], [0, 0, 0])
PointMassElements.append(point_mass)

# Objeto 3
point_mass = PointMass(8.0, [0, 0, 1], [0, 0, 0])
PointMassElements.append(point_mass)


TotalMass = 0
CombinedCG = [0, 0, 0]
FirstMoment = [0, 0, 0]

for i in range(_NUMELEMENTS):
    TotalMass += PointMassElements[i].mass

for i in range(_NUMELEMENTS):
    FirstMoment[0] += PointMassElements[i].mass * PointMassElements[i].designPosition[0]
    FirstMoment[1] += PointMassElements[i].mass * PointMassElements[i].designPosition[1]
    FirstMoment[2] += PointMassElements[i].mass * PointMassElements[i].designPosition[2]

CombinedCG = [FirstMoment[0] / TotalMass, FirstMoment[1] / TotalMass, FirstMoment[2] / TotalMass]

print(CombinedCG)

# Agora que a localização do centro de gravidade combinado foi encontrada,
# você pode calcular a posição relativa de cada ponto de massa da seguinte forma:
for i in range(_NUMELEMENTS):
    PointMassElements[i].correctedPosition = [
        PointMassElements[i].designPosition[0] - CombinedCG[0],
        PointMassElements[i].designPosition[1] - CombinedCG[1],
        PointMassElements[i].designPosition[2] - CombinedCG[2]
    ]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x = [point.correctedPosition[0] for point in PointMassElements]
y = [point.correctedPosition[1] for point in PointMassElements]
z = [point.correctedPosition[2] for point in PointMassElements]

ax.scatter(x, y, z)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()