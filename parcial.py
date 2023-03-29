import pandas as pd

data = pd.read_csv('resultados.csv')

nacional_math = data['PUNT_MATEMATICAS'].mean()
print("Promedio nacional: ",nacional_math)
print('___________________________________________________________________')

barrMat = data[['PUNT_MATEMATICAS', 'ESTU_MCPIO_PRESENTACION']] 

MatBarr = barrMat[barrMat.ESTU_MCPIO_PRESENTACION == 'BARRANQUILLA']
promMatBarr = MatBarr.PUNT_MATEMATICAS.mean()
print("Promedio local: ",promMatBarr)
print('___________________________________________________________________')

promColeTabla = data[['COLE_NATURALEZA', 'PUNT_MATEMATICAS']]
ColeNoOf = promColeTabla[promColeTabla.COLE_NATURALEZA =='NO OFICIAL']
promColeNoOf = ColeNoOf.PUNT_MATEMATICAS.mean()
print("Promedio No oficial: ",promColeNoOf)
print('___________________________________________________________________')


ColeOf = promColeTabla[promColeTabla.COLE_NATURALEZA =='OFICIAL']
promColeOf = ColeOf.PUNT_MATEMATICAS.mean()
print("Promedio oficial: ",promColeOf)
print('___________________________________________________________________')

if promMatBarr > nacional_math:
    performance_math = (promMatBarr, 'Local')
    print(performance_math)
else:
    performance_math = (nacional_math, 'Nacional')
    print(performance_math)
print('___________________________________________________________________')
if promColeNoOf > promColeOf:
    mejor_resultado = (promColeNoOf, 'No Oficial')
    
else:
    mejor_resultado = (promColeOf, 'Oficial')
print('___________________________________________________________________')
dicData = {
    'performance_math': performance_math,
    'nacional_math': nacional_math,
    'mejor_resultado': mejor_resultado

}
print(dicData)


