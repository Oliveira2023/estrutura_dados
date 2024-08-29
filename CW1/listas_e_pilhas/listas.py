from collections import deque # usa deque para criar uma fila

# usa deque para criar uma fila

fila = deque(["banana", "chocolate", "morango"])

print(fila)

fila.append("abacaxi")

print(fila)

fila.popleft()
print(fila)