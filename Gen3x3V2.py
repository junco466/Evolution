from ftplib import all_errors
import numpy as np
import random

class Gen3x3:

    #constructor de la clase Gen3x3
    def __init__(self):
        
        
        #self.i,self.j = np.shape(self.coeficientes)
        #self.fitnees = []
        #np.random.seed(0)
        self.init = True
        self.coeficientes = None
        self.independientes = None
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
        #self.genotipo = np.random.rand(10,3)*100
        #self.epocas = epocas
        
#-------------------------------------------------------------------------------------------------------------------------------------        
    
    #Inicializar poblacion inicial con valores random
    def initPob(self):

        #np.random.seed(0)
        if len(self.varRange) == 2 and self.varSize > 0 and self.populationSize > 0:
            self.poblacion = self.varRange[0] +(self.varRange[1]-self.varRange[0]) * np.random.rand(self.populationSize,self.varSize)
        else:
            print("Error: Bad configuration, please check: populationSize, varSize, varRange")
    
#-------------------------------------------------------------------------------------------------------------------------------------           
    
    #Ordenar una matriz o lista, con dependiendo de otra matriz
    def sort(self,independentList,dependentList):
        
        independentList = np.array(independentList)
        dependentList = np.array(dependentList)
        ind = independentList.argsort()
        independentList = independentList[ind]
        dependentList = dependentList[ind]

        return independentList,dependentList

#-------------------------------------------------------------------------------------------------------------------------------------        

    #Llenado de la lista fitness
    def fitness(self,objetivo):
        if self.init:
            for genotipo in self.poblacion:
                self.fitList.append(objetivo(genotipo,self.coeficientes,self.independientes))
                self.init = False
        else:
            for genotipo in self.tempPob:
                self.tempFitList.append(objetivo(genotipo,self.coeficientes,self.independientes))

#-------------------------------------------------------------------------------------------------------------------------------------        

    #Seleccion por torneo, organizados de mayor a menor
    def tounament(self):
        
        individuo = []
        fit = []
        #tempArray = zip(initPob, fitness)
        
        for i in range(0,self.padres):

            rows = self.poblacion.shape[0]
            aux = random.randint(0,rows-1)
            #aux = int(np.random.choice(rows,size=1,replace=True))
            #print(f'auxiliar {aux}')

            if individuo == []:
                individuo.append(self.poblacion[aux])
                fit.append(self.fitList[aux])
                #print(f'individuo {individuo}')
                #print(f'fit {fit}')
                
            else:
                
                for h in individuo:
                    if np.array_equal(self.poblacion[aux], h) == False:
                        print('DIFERENTESS')
                        continue
                    else:
                        while np.array_equal(self.poblacion[aux], h): # <------AQUI ESTA EL ERROR COMPARACION DE LISTAS O ARREGLOS
                            print(f'entre al while equal con aux {aux}')
                            aux = random.randint(0,rows-1)
                            print(f'sali al while equal con aux {aux}')

                individuo.append(self.poblacion[aux])
                fit.append(self.fitList[aux])
                print(f'ERORRRRRRRRRRR individuo {individuo}')
                #print(f'fit {fit}')

        fit , individuo = self.sort(fit,individuo)
        print(f'ERORRRRRRRRRRR SORTTTT individuo {individuo}')
        print(f'ERORRRRRRRRRRR SORTTTT FITT {fit}')

        # aux = random.randint(0,rows-1)
        # if np.array_equal(self.poblacion[aux], individuo[0]) == False:
        #     pass
        # else:
        #     while np.array_equal(self.poblacion[aux], individuo[0]): # <------AQUI ESTA EL ERROR COMPARACION DE LISTAS O ARREGLOS
        #         print(f'entre al while equal con aux {aux}')
        #         aux = random.randint(0,rows-1)
        #         print(f'sali al while equal con aux {aux}')
        # individuo[1] = self.poblacion[aux]
        # fit[1]= self.fitList[aux]
        # print(f'ERORRRRRRRRRRR222222 individuo {individuo}')
        # print(f'ERORRRRRRRRRRR22222   FITTT22 {fit}')


        return fit,individuo

#-------------------------------------------------------------------------------------------------------------------------------------        

    #Seleccion por elitismo
    def elite(self):
        for i in range(0,self.padres):
            self.tempPob.append(self.poblacion[i])
            self.tempFitList.append(self.fitList[i])

#-------------------------------------------------------------------------------------------------------------------------------------        

    #Loop del algoritmo genetico
    def start(self):
        h=0
        self.fitness(self.objetivo)
        self.fitList, self.poblacion = self.sort(self.fitList,self.poblacion)
        print(self.fitList)
        print(self.poblacion)
        print(f'\nfitness: {self.fitList}')

        while self.fitList[0] > self.presicion and h < self.epocas:
            
            count = 0
            self.elite()
            print(f'poblacion temporal en CONSTRUCCION: \n {self.tempPob} \n')
            while len(self.tempPob) < len(self.poblacion):
                count = count +1
                fit,individuo = self.tounament()

                if random.random() <= self.pc:
                    print('fit antes del cruce: ')
                    print(fit)
                    print()
                    fit ,individuo = self.cruce(individuo)
                    print('fit despues del cruce: ')
                    print(fit)
                    print()
                    if random.random() <= self.pm:
                        fit,individuo= self.mutacion(individuo,fit)
                for i in range(0,len(fit)):
                    print(f'IIIII {i}')
                    self.tempPob.append(individuo[i])
                    self.tempFitList.append(fit[i])
                print(f'poblacion temporal en CONSTRUCCION: \n {self.tempPob} \n')

            print('poblacion temporal:')
            print(self.tempPob)
            print(len(self.tempPob))
            print(f'count {count}')
            print()

            self.fitList, self.poblacion = self.sort(self.tempFitList,self.tempPob)
            #self.poblacion = np.array(self.tempPob)
            #self.fitList = self.tempFitList
            print(f'termine epoca {h}, el fit y la poblacion actualizadas son las siguientes: ')
            print(f'Poblacion: ')
            print(self.poblacion)
            print(len(self.poblacion))
            print()

            print(f'Fintess: ')
            print(self.fitList)
            print()

            self.tempPob = []
            self.tempFitList = []

            h=h+1

#-------------------------------------------------------------------------------------------------------------------------------------

    def cruce(self,individuo):
        print('individuo antes del cruce')
        print(individuo)
        print()

        fit=[]

        punto = random.randint(0,len(individuo[0])-2)
        auxList = individuo.copy()

        print(f'punto {punto} y lista auxiliar {auxList}\n')
        
        individuo[0][punto+1:] = auxList[1][punto+1:]
        individuo[1][punto+1:] = auxList[0][punto+1:]

        # for i in range(0,len(auxList[0])):
            
            # if i == punto:
            #     print(f'punto{punto}, i {i}')
            #     continue
            # else:

                # individuo[0][i] = auxList[1][i]
                # individuo[1][i] = auxList[0][i]
                # print(f'individuo {individuo}')
            
        fit.append(self.objetivo(individuo[0],self.coeficientes,self.independientes))
        fit.append(self.objetivo(individuo[1],self.coeficientes,self.independientes))

        fit , individuo = self.sort(fit,individuo)
        print('individuo despues del cruce')
        print(individuo)
        print()
        return fit, individuo

#-------------------------------------------------------------------------------------------------------------------------------------

    def mutacion(self,individuos,fit):
        print(f'individuo antes de mutado: {individuos}')
        print(f'fit, antes de la mutacion : {fit}')
        print()
        individuo = random.randint(0,len(individuos)-1)
        alelo = random.randint(0,len(individuos[0])-1)
        mutado = random.uniform(self.varRange[0],self.varRange[1])
        individuos[individuo][alelo] = mutado
        fit[individuo] = self.objetivo(individuos[individuo],self.coeficientes,self.independientes)

        fit , individuos = self.sort(fit,individuos)
        print(f'individuo despues de mutado punto (individuo:{individuo}),(alelo:{alelo}) : {individuos}')
        print(f'fit, luego de la mutacion : {fit}')
        print()
        return fit, individuos


#-------------------------------------------------------------------------------------------------------------------------------------        

    #Representacion como string de los atributos de la clase
    def __str__(self):

        str = [f'Variables del objeto gen3x3: \n',
               f'Matriz coeficientes:\n {self.coeficientes} \n',
               f'Matriz terminos independientes: \n{self.independientes} \n',
               f'Matriz de poblacion: \n{self.poblacion}\n',
               f'Fitness: \n{self.fitList} \n',
               f'Rango de las variables: {self.varRange} \n',
               f'Tamaño poblacion: {self.populationSize} \n',
               f'Cantidad de variables: {self.varSize} \n',
               f'Presicion: {self.presicion} \n',
               f'Porcentaje de mutacion: {self.pm} \n',
               f'Porcentaje de cruce: {self.pc} \n',
               f'Epocas: {self.epocas} \n'
               f'Padres por elitismo y torneos: {self.padres} \n',
               f'poblacion temporal: {self.tempPob} \n',
               f'fit temporal: {self.tempFitList} \n',   
        ]

        return "\n".join(str)
