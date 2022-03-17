import numpy as np
from Genetico import Gen

def objetivo(geno):
        
        coef = np.array([[3,8,2],[1,-2,4],[-5,3,11]])
        inde = np.array([25,12,4])
        height, width = np.shape(coef)
        fit = 0

        for i in range(height):
            aux = 0
            for j in range(width):
                aux = aux + (geno[j] * coef[i][j])
            fit = fit + abs((inde[i] - aux))
            
        return fit  


if __name__ == '__main__':
  
    ecuacion = Gen() #Objeto del algoritmo genetico
    ecuacion.populationSize = 500
    ecuacion.varSize = 3
    ecuacion.varRange = [-10,10]
    ecuacion.epocas = 1000
    ecuacion.presicion = 0.5
    ecuacion.padres = 2
    ecuacion.pc = 0.9
    ecuacion.pm = 0.2

    ecuacion.initPob()
    ecuacion.objetivo = objetivo
    ecuacion.start()

    print(ecuacion)