from Genetico import Gen
from control.matlab import *
import matplotlib.pyplot as plt

def PID(individuo):
    
    global y_base
    global t
    fit = 0
    #global planta yi yc t1;
    pid= tf([individuo[0],individuo[1],individuo[2]],[1, 0])
    sys_serie = series(pid,planta)
    sys_cloop = feedback(sys_serie,1)
    y,t = step(sys_cloop,t)

    for i in range(0,len(y)-1):
        fit = fit + abs(y_base[i]-y[i])
    
    return fit

if __name__ == '__main__':
  
    ecuacion = Gen()
    ecuacion.populationSize = 10
    ecuacion.varSize = 3
    ecuacion.presicion = 0.2
    ecuacion.varRange = [-10,10]
    ecuacion.epocas = 1000
    ecuacion.presicion = 0.3
    ecuacion.padres = 2
    ecuacion.pc = 0.9
    ecuacion.pm = 0.2

    ecuacion.initPob()

    t = []
    aux = 0
    for i in range(0,50):
        t.append(aux)
        aux = aux + 0.02   
        
    planta = tf([10],[1, 2, 10])
    pid_base = tf([12.0918, 8.4047, 17.1467],[1, 0])
    sys_serie_base = series(pid_base,planta)
    sys_cloop_base = feedback(sys_serie_base,1)
    y_base,t1 = step(sys_cloop_base,t) #Salida base

    ecuacion.objetivo = PID
    ecuacion.start()

    print(ecuacion)
    
    y_final = ecuacion.poblacion[0]
    # print(y_final)
    pid=tf([y_final[0],y_final[1],y_final[2]],[1, 0])
    sys_serie=series(pid,planta)
    sys_cloop=feedback(sys_serie,1)
    step_final,t2=step(sys_cloop,t)

    #Graficas
    fig = plt.figure("Respuesta")
    fig.subplots_adjust(hspace=0.5, wspace=0.5)
    
    ax = fig.add_subplot(2, 2, 1)
    ax.plot(t2,y_base,'r')

    plt.grid(True)
    plt.title(u"Respuesta planta base")
    plt.xlabel("segundos")

    ax = fig.add_subplot(2, 2, 2)
    ax.plot(t2,step_final,'b')

    plt.grid(True)
    plt.title(u"Respuesta planta calculada")
    plt.xlabel("segundos")
    plt.show()
