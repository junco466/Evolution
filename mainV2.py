import numpy as np
from Gen3x3V2 import Gen3x3
from more_itertools import sort_together

def objetivo(geno,coef,inde):
        
        height, width = np.shape(coef)
        fit = 0

        for i in range(height):
            aux = 0
            for j in range(width):
                aux = aux + (geno[j] * coef[i][j])
                #print(f'geno{geno[j]}')
            
            #print(f'auxiliar{aux}')
            #print(f'independiente i{self.independientes[i]}')
            fit = fit + abs((inde[i] - aux))
            
        return fit  


if __name__ == '__main__':
  
   #prueba = np.array([4.643,0.821,2.250])
    #Configuracion del algoritmo
    ecuacion = Gen3x3()
    ecuacion.populationSize = 500
    ecuacion.varSize = 3
    ecuacion.presicion = 0.2
    ecuacion.varRange = [-10,10]
    ecuacion.epocas = 1000
    ecuacion.presicion = 1
    ecuacion.coeficientes = np.array([[3,8,2],[1,-2,4],[-5,3,11]])
    ecuacion.independientes = np.array([25,12,4])
    ecuacion.padres = 2
    ecuacion.pc = 0.9
    ecuacion.pm = 0.2

    ecuacion.initPob()
    ecuacion.objetivo = objetivo
    #ecuacion.fitness(objetivo)
    ecuacion.start()

    print(ecuacion)

    #fitness, initPob = ecuacion.sort(fitness,initPob)
   

    # while fitness[0] > presicion or h > epocas:
    #     tempPob.append(initPob[0])
    #     tempPob.append(initPob[1])
    #     print(tempPob)


    #     h = h+1
    #     break
