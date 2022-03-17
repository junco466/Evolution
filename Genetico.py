import numpy as np
import random


class Gen:

    #---constructor de la clase Gen---
    def __init__(self):
        
        self.populationSize = 0
        self.varSize = 0 
        self.varRange = []
        self.presicion = 0
        self.poblacion = None
        self.pm = 0 #porcentaje de murtacion
        self.pc = 0 #porcentaje de cruce
        self.fitList = []
        self.tempPob = []
        self.tempFitList = []
        self.epocas = 0
        self.padres = 0
        self.objetivo = None
        self.h = 0 #conteo de epocas

        
#-------------------------------------------------------------------------------------------------------------------------------------        
    
    #---Inicializar poblacion inicial con valores random---
    def initPob(self):

        if len(self.varRange) == 2 and self.varSize > 0 and self.populationSize > 0:
            self.poblacion = self.varRange[0] +(self.varRange[1]-self.varRange[0]) * np.random.rand(self.populationSize,self.varSize)
        else:
            print("Error: Bad configuration, please check: populationSize, varSize, varRange")
    
#-------------------------------------------------------------------------------------------------------------------------------------           
    
    #---Ordenar una matriz o lista, con dependiendo de otra matriz---
    def sort(self,independentList,dependentList):
        
        independentList = np.array(independentList)
        dependentList = np.array(dependentList)
        ind = independentList.argsort()
        independentList = independentList[ind]
        dependentList = dependentList[ind]

        return independentList,dependentList

#-------------------------------------------------------------------------------------------------------------------------------------        

    #---Seleccion por torneo, organizados de mayor a menor---
    def tounament(self):
        
        individuo = []
        fit = []
        
        for i in range(0,self.padres):

            rows = self.poblacion.shape[0]
            aux = random.randint(0,rows-1)

            if individuo == []:
                individuo.append(self.poblacion[aux])
                fit.append(self.fitList[aux])
                
            else:
                
                for n in individuo:
                    if np.array_equal(self.poblacion[aux], n) == False:
                        continue
                    else:
                        while np.array_equal(self.poblacion[aux], n):
                            aux = random.randint(0,rows-1)

                individuo.append(self.poblacion[aux])
                fit.append(self.fitList[aux])

        fit , individuo = self.sort(fit,individuo)
        
        return fit,individuo

#-------------------------------------------------------------------------------------------------------------------------------------        

    #---Seleccion por elitismo---
    def elite(self):
        for i in range(0,self.padres):
            self.tempPob.append(self.poblacion[i])
            self.tempFitList.append(self.fitList[i])


#-------------------------------------------------------------------------------------------------------------------------------------

    #-----CRUCE----
    def cruce(self,individuo):

        fit=[]

        punto = random.randint(0,len(individuo[0])-2)
        auxList = individuo.copy()
        
        individuo[0][punto+1:] = auxList[1][punto+1:]
        individuo[1][punto+1:] = auxList[0][punto+1:]
            
        fit.append(self.objetivo(individuo[0]))
        fit.append(self.objetivo(individuo[1]))

        fit , individuo = self.sort(fit,individuo)
        return fit, individuo

#-------------------------------------------------------------------------------------------------------------------------------------

    #---MUTACION---
    def mutacion(self,individuos,fit):
        individuo = random.randint(0,len(individuos)-1)
        alelo = random.randint(0,len(individuos[0])-1)
        mutado = random.uniform(self.varRange[0],self.varRange[1])
        individuos[individuo][alelo] = mutado
        fit[individuo] = self.objetivo(individuos[individuo])

        fit , individuos = self.sort(fit,individuos)
        return fit, individuos

#-------------------------------------------------------------------------------------------------------------------------------------        

    #---ALGORITMO GENETICO PRINCIPAL---
    def start(self):
        for genotipo in self.poblacion:
                self.fitList.append(self.objetivo(genotipo))
        self.fitList, self.poblacion = self.sort(self.fitList,self.poblacion)
        print('Algoritmo Corriendo.....\n')
        print('POBLACION INICAL:')
        print(self.poblacion)

        while self.fitList[0] > self.presicion and self.h < self.epocas:
            
            if (self.h)%50 == 0:
                    print(f'Epocas {self.h}')
                    print('.........')

            self.elite()
            while len(self.tempPob) < len(self.poblacion):

                fit,individuo = self.tounament()

                if random.random() <= self.pc:
                    fit ,individuo = self.cruce(individuo)
                    if random.random() <= self.pm:
                        fit,individuo= self.mutacion(individuo,fit)
                for i in range(0,len(fit)):
                    self.tempPob.append(individuo[i])
                    self.tempFitList.append(fit[i])

            self.fitList, self.poblacion = self.sort(self.tempFitList,self.tempPob)
            self.tempPob = []
            self.tempFitList = []

            self.h=self.h+1

        print('POBLACION FINAL: ')
        print(self.poblacion)
        print('\nAlgoritmo finalizado')

#-------------------------------------------------------------------------------------------------------------------------------------        

    #---Representacion como string de los atributos de la clase---
    def __str__(self):

        str = [f'El mejor individuo es: {self.poblacion[0]}\n'
               f'Su tolerancia es del {self.fitList[0]}%\n'
               f'Epocas computadas: {self.h}'
        
        ]

        #STRING DE DESARROLLO Y MONITOREO DE ATRIBUTOS
        # str = [f'Variables del objeto gen3x3: \n',
        #     #    f'Matriz coeficientes:\n {self.coeficientes} \n',
        #     #    f'Matriz terminos independientes: \n{self.independientes} \n',
        #        f'Matriz de poblacion: \n{self.poblacion}\n',
        #        f'Fitness: \n{self.fitList} \n',
        #        f'Rango de las variables: {self.varRange} \n',
        #        f'Tamaño poblacion: {self.populationSize} \n',
        #        f'Cantidad de variables: {self.varSize} \n',
        #        f'Presicion: {self.presicion} \n',
        #        f'Porcentaje de mutacion: {self.pm} \n',
        #        f'Porcentaje de cruce: {self.pc} \n',
        #        f'Epocas: {self.epocas} \n'
        #        f'Padres por elitismo y torneos: {self.padres} \n',
        #        f'poblacion temporal: {self.tempPob} \n',
        #        f'fit temporal: {self.tempFitList} \n',   
        # ]

        return "\n".join(str)
