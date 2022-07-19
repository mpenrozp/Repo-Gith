lenguajes =["python","java","c#"]
print(lenguajes)
print(lenguajes[0])#devuelve primer elemento
print(len(lenguajes)) #imprime el largo
print(lenguajes[-2]) #devuelve segundo elemento
print(lenguajes[0:2]) #devuelve lo que esta entre el primer y segundo elemento

lista = [lenguajes,"practica","dedicación"]
print(lista) 

print(lista[0][0])#primer elemento de la primera lista
lenguajes[0] = "dart"
print(lenguajes)
lenguajes.append("python")
print(lenguajes)
otros_lenguajes = ["C","C++"]
lenguajes.extend(otros_lenguajes)
print(lenguajes)
lenguajes.append(otros_lenguajes)
print(lenguajes)


