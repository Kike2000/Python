animal = "  Pedro Enrique  "

# Resultado:  PEDRO ENRIQUE
print(animal.upper())

# Resultado:  pedro enrique
print(animal.lower())

# Resultado:Pedro enrique
print(animal.strip().capitalize())

# Resultado:  Pedro Enrique
print(animal.title())

# Resultado:Pedro Enrique
print(animal.strip())

# Resultado:Pedro Enrique
print(animal.lstrip())

# Resultado:  Pedro Enrique
print(animal.rstrip())

# Resultado:  2 (Regresa el índice)
print(animal.find("P"))

# Resultado:  -1(no lo encontró)(Regresa el índice)
print(animal.find("Pso"))

# Resultado:  False o True (depende de lo que busques)
print("pedro" in animal)

# Resultado:  False o True (depende de lo que busques)
print("pedro" not in animal)
