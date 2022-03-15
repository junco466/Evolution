import numpy as np
#import random

class Gen3x3:

    def __init__(self):
        
        self.coeficientes = np.array([[3,8,2],[1,-2,4],[-5,3,11]])
        #self.i,self.j = np.shape(self.coeficientes)
        self.independientes = np.array([25,12,4])
        #self.fitnees = []
        #np.random.seed(0)
        self.populationSize = 0
        self.varSize = 0 
        self.varRange = []
        self.presicion = 0
        self.poblacion = None
        self.pm = 0 #porcentaje de murtacion
        self.pc = 0 #porcentaje de cruce
        #self.genotipo = np.random.rand(10,3)*100
        #self.epocas = epocas
        
    def initPob(self):

        np.random.seed(0)
        if len(self.varRange == 2) and self.varSize > 0 and self.populationSize > 0:
            self.poblacion = self.varRange[0] +(self.varRange[1]-self.varRange[0]) * np.random.rand(self.populationSize,self.varsize)
        else:
            print("Error: Bad configuration, please check: populationSize, varSize, varRange")
    
    def objetivo(self,geno):
        
        height, width = np.shape(self.coeficientes)
        fit = 0

        for i in range(height):
            aux = 0
            for j in range(width):
                aux = aux + (geno[j] * self.coeficientes[i][j])
                #print(f'geno{geno[j]}')
            
            #print(f'auxiliar{aux}')
            #print(f'independiente i{self.independientes[i]}')
            fit = fit + abs((self.independientes[i] - aux))
            
        return fit     
    
    def sort(self,fit,geno):
        
        fit = np.array(fit)
        ind = fit.argsort()
        fitnessOrd = fit[ind]
        genoOrd = geno[ind]

        return fitnessOrd, genoOrd

    def tounament(self,initPob,fitness):
        
        P=[]
        tempArray = zip(initPob, fitness)
        
        P.append(np.random.choice(tempArray))
        P.append(np.random.choice(tempArray))

        P.sort()


    def __str__(self):

        cadena = f'coeficientes: \n{self.coeficientes}, \nindependientes: \n{self.independientes}'
        return cadena 