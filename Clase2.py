#Notas Escolares

def obtener_notas_estudiante():
    notas = []
    materias = ["Matematicas", "Ciencias", "Historia"]
    
    for materia in materias:
        nota = float(input(f"Ingrese la nota de {materia} del estudiante: "))
        notas.append(nota)
    
    return notas

def calcular_promedio(notas):
    return sum(notas) / len(notas)

def ingresar_notas_estudiantes(num_estudiantes):
    estudiantes = []
    promedios = []
    
    for _ in range(num_estudiantes):
        nombre = input("Ingrese el nombre del estudiante: ")
        notas = obtener_notas_estudiante()
        promedio = calcular_promedio(notas)
        
        estudiantes.append({"nombre": nombre, "notas": notas, "promedio": promedio})
        promedios.append(promedio)
    
    return estudiantes, promedios

def imprimir_resultados(estudiantes, promedios):
    print("\nResultados:")
    
    for estudiante in estudiantes:
        print(f"Estudiante: {estudiante['nombre']}, Promedio: {estudiante['promedio']:.2f}")
    
    promedio_maximo = max(promedios)
    promedio_minimo = min(promedios)
    
    print(f'\nEl promedio más alto es: {promedio_maximo:.2f}')
    print(f'El promedio más bajo es: {promedio_minimo:.2f}')

# Ingresar datos
numero_estudiantes = 5
estudiantes, promedios = ingresar_notas_estudiantes(numero_estudiantes)

# Imprimir resultados
imprimir_resultados(estudiantes, promedios)

