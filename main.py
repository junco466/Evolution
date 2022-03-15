import numpy as np
from Gen3x3 import Gen3x3
from more_itertools import sort_together

if __name__ == '__main__':
  
   #prueba = np.array([4.643,0.821,2.250])


    #Definicion de variables, y objetos
    fitness = []
    np.random.seed(0)
    initPob = 10 + (-20) * np.random.rand(10,3)
    tempPob = []
    print(f'genotipo {initPob}')
    epocas = 10
    h = 0
    ecuacion = Gen3x3(0.10,0.02,0.02)
    presicion = 20
    init = True

    for genotipo in initPob:
        fitness.append(ecuacion.objetivo(genotipo))

    print(fitness)
    fitness, initPob = ecuacion.sort(fitness,initPob)
    print(fitness)
    print(initPob)
    print(ecuacion)
    print(f'\nfitness: {fitness}')

    while fitness[0] > presicion or h > epocas:
        tempPob.append(initPob[0])
        tempPob.append(initPob[1])
        print(tempPob)


        h = h+1
        break
