import random 
import numpy as np
import matplotlib.pyplot as plt

users_name = ["John", "Jane", "Mike", "Sarah", "David", "Emily"]
films = ["The Shawshank Redemption", "Pulp Fiction", "The Godfather", "The Dark Knight", "Inception"]

users_films = np.zeros((len(users_name), len(films)))


print( users_films)

for i in range(len(users_name)):
    for j in range(len(films)):
        users_films[i][j] = random.randint(0, 5)
print( users_films)

#mean for each row
mean_users_films = np.mean(users_films, axis=1)

for i in range(len(users_name)):
    for j in range(len(films)):
        if users_films[i][j] == 0:
            continue
        else:
            users_films[i][j] -= mean_users_films[i]

sim_matrix = np.zeros((len(users_name), len(users_name)))
for i in range(len(users_name)):
    for j in range( len(users_name)):
        user_i = users_films[i]
        user_j = users_films[j]

        mask = (user_i != 0) & (user_j != 0)
        if np.sum(mask) == 0:
            sim_matrix[i, j] = 0
            continue
        a = user_i[mask]
        b = user_j[mask]
        dot = np.dot(a, b)
        norm_a = np.linalg.norm(a)
        norm_b = np.linalg.norm(b)

        if norm_a == 0 or norm_b == 0:
            sim = 0
        else:
            sim = dot / (norm_a * norm_b)

        # 4. guardar
        sim_matrix[i, j] = sim


print( sim_matrix)

user_to_recommend = random.randint(1,6)
print("user = " , user_to_recommend)
row = sim_matrix[user_to_recommend]
row.copy()
row[user_to_recommend] = -1

indices_ordenados = np.argsort(row)[::-1]
vecinos = indices_ordenados[:2]
sims= sim_matrix[user_to_recommend,vecinos]
ratings_vecinos = users_films[vecinos]

numerador = np.dot(sims, ratings_vecinos)
denominador = np.sum(sims)

    # si denominador es 0 -> no hay similitud usable
if denominador == 0:
    print("No hay similitud usable")
else:
    scores = numerador / denominador
 # 5. No recomendar películas ya vistas por el usuario objetiv
    ya_vistas = users_films[user_to_recommend] != 0
    scores[ya_vistas] = -1  # marcar como no recomendables

    # 6. Ordenar las mejores películas
    recomendaciones = np.argsort(scores)[::-1]
    print("Recomendaciones: ", recomendaciones)


    plt.figure(figsize=(8, 6))
    plt.imshow(users_films, cmap='viridis', aspect='auto')
    plt.colorbar(label="Calificación")
    plt.title("Heatmap de Calificaciones (0 = no visto)")
    plt.xlabel("Películas")
    plt.ylabel("Usuarios")
    plt.show()
