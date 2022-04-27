# Complete the 'maxSubarray' function below.

def maxSubarray(arr):
    # Write your code here

    resultado = [0,0]
    sumaSubsec = 0

    numMayor = max(arr[:])
    menor = min(arr[:])
    sumaPresente = 0
    sumaPasado = 0

    for l in range(0,len(arr)):
        sumaPresente = 0
        for k in range(0+l,len(arr)):
            sumaPresente += arr[k]
            if(sumaPresente > sumaPasado):
                sumaPasado = sumaPresente
    if sumaPasado != 0 or numMayor == 0:
        resultado[0] = sumaPasado
    else:
        resultado[0] = numMayor


    for j in arr[:]:
        if sumaSubsec+j > sumaSubsec:
            sumaSubsec += j
        else:
            if j > menor and j < 0:
                menor = j
    if sumaSubsec != 0 or numMayor == 0:
        resultado[1] = sumaSubsec
    else:
        resultado[1] = numMayor

    return resultado
