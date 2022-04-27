def climbingLeaderboard(ranked, player):
    # Write your code here
    
    ranked = list(set(ranked)) # Lista de datos aleatorios sin repetir ningun dato
                                # Permite ordenar mejor los jugadores
    n = len(ranked) # n: Numero de jugadores - ranked: puntaje en la tabla decreciente
    m = len(player) # m: Numero de juegos jugados - player: puntaje del juego
    ranked = sorted(ranked, reverse = True) # Puntaje tabla ordenada decreciente
    player = sorted(player, reverse = True) # Puntaje tabla ordenada creciente
    result = [] # Tabla de resultados
    i = 0
    j = 0

    for i in player:
        k = 1
        for j in ranked:
            if i>=j:
                result.append(k)
                break
            else:
                k+=1
    if player[-1] < ranked[-1]:
        result.append(k)

    return result[::-1] # Toda la tabla de resultados ordenada