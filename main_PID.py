import numpy as np
from Gen3x3V2 import Gen3x3
from control.matlab import *
from more_itertools import sort_together
import matplotlib.pyplot as plt

# def objetivo(geno,coef,inde):
        
#         height, width = np.shape(coef)
#         fit = 0

#         for i in range(height):
#             aux = 0
#             for j in range(width):
#                 aux = aux + (geno[j] * coef[i][j])
#                 #print(f'geno{geno[j]}')
            
#             #print(f'auxiliar{aux}')
#             #print(f'independiente i{self.independientes[i]}')
#             fit = fit + abs((inde[i] - aux))
            
#         return fit  

def PID(individuo):
    
    global y_base
    global t
    fit = 0
    #global planta yi yc t1;
    pid=tf([individuo[0],individuo[1],individuo[2]],[1, 0])
    sys_serie=series(pid,planta)
    sys_cloop=feedback(sys_serie,1)
    y,t=step(sys_cloop,t)
    for i in range(0,len(y)-1):
        fit = fit + abs(y_base[i]-y[i])
    
    return fit
    
    # e=abs(yi - yc);
    # a = sum(e);


if __name__ == '__main__':
  
   #prueba = np.array([4.643,0.821,2.250])
    #Configuracion del algoritmo
    ecuacion = Gen3x3()
    ecuacion.populationSize = 500
    ecuacion.varSize = 3
    ecuacion.presicion = 0.2
    ecuacion.varRange = [-10,10]
    ecuacion.epocas = 1000
    ecuacion.presicion = 50
    ecuacion.padres = 2
    ecuacion.pc = 0.9
    ecuacion.pm = 0.2

    ecuacion.initPob()

    t = []
    aux = 0
    for i in range(0,100):
        t.append(aux)
        aux = aux + 0.1   

    planta=tf([5,2],[1, 5, 8, 4])
    pid_base=tf([13.0447, 37.6692, 18.9251],[1, 0])
    sys_serie_base=series(pid_base,planta)
    sys_cloop_base=feedback(sys_serie_base,1)
    y_base,t1=step(sys_cloop_base,t)

    ecuacion.objetivo = PID
    #ecuacion.fitness(objetivo)
    

    

    ecuacion.start()

    print(ecuacion)
    
    y_final = ecuacion.poblacion[0]
    print(y_final)
    pid=tf([y_final[0],y_final[1],y_final[2]],[1, 0])
    sys_serie=series(pid,planta)
    sys_cloop=feedback(sys_serie,1)
    step_final,t2=step(sys_cloop,t)

    print(f'tamaño base {len(y_base)} t1: {len(t1)}')
    print(f'tamaño final {len(step_final)} t1: {len(t2)}')


    #Graficas

    
    fig = plt.figure("Respuesta")
    fig.subplots_adjust(hspace=0.5, wspace=0.5)
    ax = fig.add_subplot(2, 2, 1)
    ax.plot(t2,step_final,'r')
    ax = fig.add_subplot(2, 2, 2)
    ax.plot(t2,y_base,'r')
    
    plt.grid(True)
    plt.title(u"Respuesta al escalón")
    plt.xlabel("segundos")
    plt.show()
    
    # print('yi: ')
    # print(yi)
    # print(len(yi))
    # print('t: ')
    # print(t)


    #fitness, initPob = ecuacion.sort(fitness,initPob)
   

    # while fitness[0] > presicion or h > epocas:
    #     tempPob.append(initPob[0])
    #     tempPob.append(initPob[1])
    #     print(tempPob)


    #     h = h+1
    #     break
