import constantes
import funciones as fn

vector_mate = [0.0] * constantes.CANTIDAD_ALUMNOS
vector_ingl = [0.0] * constantes.CANTIDAD_ALUMNOS
vector_prog= [0.0] * constantes.CANTIDAD_ALUMNOS
vector_ayso = [0.0] * constantes.CANTIDAD_ALUMNOS

vector_promedio_alumnos = [0.0] * constantes.CANTIDAD_ALUMNOS

for i in range(constantes.CANTIDAD_ALUMNOS):
    prog, mate, ingl, ayso = fn.cargar_notas_alumnos(i)
    vector_prog[i] = prog
    vector_ingl[i] = ingl
    vector_mate[i] = mate
    vector_ayso[i] = ayso

    vector_promedio_alumnos[i] = fn.calcular_promedio_alumno(prog, mate, ingl, ayso) 

fn.mostrar_promedio_alumnos(vector_promedio_alumnos)
