#entradas
horas_trabajadas=int(input("número de horas trabajadas"))
precio_hora=int(input("percio por hora"))
#caja negra
salario=horas_trabajadas*precio_hora
salario_neto=salario-(salario*.20)
#salidas
print("el salario neto es de: ", salario_neto)