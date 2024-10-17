# Entradas
salario_base = int(input("Ingrese su salario $"))
cargo = input("Ingrese su cargo de empleado: ")
desempeno = input("Ingrese su nivel de desempeño: ")

# Validar datos ingresados y mostrar el resumen
def validar_datos(salario_base, cargo, desempeno):
    # Calcular bonificación y total
    bonificacion, total_a_recibir = calcular_bonificacion(salario_base, cargo, desempeno)
    # Mostrar resumen
    resumen = generar_resumen(cargo, desempeno, salario_base, bonificacion, total_a_recibir)
    print(resumen)

# Función para calcular bonificación
def calcular_bonificacion(salario_base, cargo, desempeno):
    # Convertimos a minúsculas
    cargo = cargo.lower()
    desempeno = desempeno.lower()

    # Tipo de bonificación dependiendo el cargo y desempeño
    if cargo == "directivo":
        if desempeno == "alto":
            porcentaje_bonificacion = 0.20
        elif desempeno == "medio":
            porcentaje_bonificacion = 0.10
        else:
            porcentaje_bonificacion = 0.0
    elif cargo == "operativo":
        if desempeno == "alto":
            porcentaje_bonificacion = 0.15
        elif desempeno == "medio":
            porcentaje_bonificacion = 0.05
        else:
            porcentaje_bonificacion = 0.0
    else:
        porcentaje_bonificacion = 0.0

    # Calcular bonificación y total
    bonificacion = round(salario_base * porcentaje_bonificacion)
    total = salario_base + bonificacion

    return bonificacion, total


# Funcion salida
def generar_resumen(cargo, desempeno, salario_base, bonificacion, total):
    return (f"-----Resumen del Pago-----\n"
            f"Cargo: {cargo.capitalize()}\n"
            f"Nivel de Desempeño: {desempeno.capitalize()}\n"
            f"Salario Base: ${salario_base}\n"
            f"Bonificación: ${bonificacion}\n"
            f"Total a Recibir: ${total}\n"
            f"------------------------------------\n")

# Validar y mostrar los resultados
validar_datos(salario_base, cargo, desempeno)