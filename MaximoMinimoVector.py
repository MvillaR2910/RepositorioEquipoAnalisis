def CalcularVector(vector, inicio, fin):
    if inicio == fin:
        return vector[inicio], vector[inicio]
    
    mid =  (inicio + fin) // 2
    max_izq, min_izq = CalcularVector(vector, inicio, mid)
    max_der, min_der = CalcularVector(vector, mid + 1, fin)

    max_val = max(max_izq, max_der)
    min_val = min(min_izq, min_der)

    return max_val, min_val

vector = [2,5,8,-5,10]
max_val, min_val = CalcularVector(vector, 0, len(vector) - 1)

print("Maximo valor:", max_val)
print("Minimo valor:", min_val)

