estudent = input("ingresa el nombre de el estudiante: ")

cursos = (
    "calculo multivariado",
    "lengua extranjera",
    "fisca III",
    "ingles II",
    "estructuras de informacion",
    "arqutectura de computadoras"

)

nota_maxima = 5.0

notas = [None] * len(cursos)  

print(" Registro de calificaciones")
print(f"Estudiante: {estudent}\n")

for i, curso in enumerate(cursos):
    entrada = input(f"Ingrese la nota de {curso} (o presione Enter si no tiene): ")
    if entrada.strip() != "":
        nota = float(entrada)
        if 0.0 <= nota <= nota_maxima:
            notas[i] = nota
        else:
            print(" Error: La nota debe estar entre 0.0 y 5.0")