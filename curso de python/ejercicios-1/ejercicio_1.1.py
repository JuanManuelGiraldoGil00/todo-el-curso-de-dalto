#promedio de duracion
otros_cursos_min= 2.5
otros_cursos_max= 7
otros_cursos_promedio= 4
dalto_curso= 1.5

#duracion de crudos 
crudo_promedio= 5 
crudo_curso_dalto= 3.5

#diferencias de duracion
diferencias_con_min= round((100 - dalto_curso * 1000 / otros_cursos_min /10),1)
diferencias_con_max= round((100 - dalto_curso * 1000 / otros_cursos_max / 10),2)
diferencias_con_promedio= round((100 - dalto_curso / otros_cursos_promedio * 100),2)

# # #mostrando diferencias de duracion (ejercici A)
print(f"el curso de dalto dura un {diferencias_con_min}% menos que el mas rapido  ")
print(f"el curso de dalto dura un {diferencias_con_max}% menos que el lento ")
print(f"el curso de dalto dura un {diferencias_con_promedio}% menos que el promedio ")
print("------------------")

# #calculando el porcentaje de tiempo vacio removido
tiempo_vacio_promedio= round(( 100 - otros_cursos_promedio * 1000 / crudo_promedio / 10),2)
tiempo_vacio_dalto= round(( 100-dalto_curso * 1000 / crudo_curso_dalto/ 10),2)

# #mostrando mostrando la cantidad de espacios que se remueven   (ejercicio B)
print(f"un curso promedio elimina un  {tiempo_vacio_promedio}% menos de tiempo vacio")
print(f"este curso elimino el  {tiempo_vacio_dalto}% de tiempo vacio")
# print("------------------")

# #mostrando diferencias si los cursos  duraran 10 horas 
print(f"ver 10 horas de este curso   equivale a ver {otros_cursos_promedio *100 // dalto_curso/ 10} horas de otros cursos ")
print(f"ver 10 horas de otros cursos equivale a ver {dalto_curso *100 // otros_cursos_promedio/ 10} horas de este curso ")
print("------------------")