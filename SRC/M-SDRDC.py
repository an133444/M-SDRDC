estudent = input("ingresa el nombre de el estudiante: ")

cursos = (
    "calculo multivariado",
    "lengua extranjera",
    "fisica III",
    "ingles II",
    "estructuras de informacion",
    "arquitectura de computadoras"

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

print("\n Reporte de Calificaciones")
for curso, nota in zip(cursos, notas):
    if nota is None:
        print(f" - {curso}: Sin calificación")
    else:
        print(f" - {curso}: {nota}")

notas_validas = [n for n in notas if n is not None]
if notas_validas:
    promedio = sum(notas_validas) / len(notas_validas)
else:
    promedio = 0.0

print(f"\n Promedio final: {promedio:.2f}")
