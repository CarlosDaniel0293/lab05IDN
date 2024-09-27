from river import anomaly
#Crear detector de anomalías
model = anomaly. HalfSpaceTrees()
#Añadir observaciones al modelo
observations = [
    {'feature': 0.5},
    {'feature': 0.7},
    {'feature': 0.6},
    {'feature': 0.8},
    {'feature': 1.0},
    {'feature': 1.2},
    {'feature': 1.1}
]
for obs in observations:
    model.Learn_one(obs)
#Evaluar una nueva observación
new_observation = {'feature': 0.9}
score = model.score_one (new_observation)
print (f"Puntuación de anomalía para {new_observation}: {score}")