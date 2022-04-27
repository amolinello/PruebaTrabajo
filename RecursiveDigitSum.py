# Recursive Digit Sum ejecicio

def superDigit(n, k):
    # Write your code here
    n = n.replace(" ", "")
    p = n*k
    
    if len(str(p)) == 1:
        return int(p)
    else:
        while len(str(p)) > 1:
            resultado = 0
            for i in p:
                resultado += int(i)
            p = str(resultado)
            p = superDigit(p, 1)

        return p
              


