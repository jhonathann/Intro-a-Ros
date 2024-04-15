# Intro a Ros

# Grupo 2

- Julian Leonardo Villalobos Jiménez - jlvillalovbosj@unal.edu.co
- Jhonathann Alexander Gómez Velásquez - jhagomezve@unal.edu.co

El presente repositorio tiene por objetivo mostrar el funcionamiento de Robot Operating System ROS y su integración tanto con MATLAB como con python. Usando para ello turtlesim y las diferentes tópicos y servición que este provee.

<p align="center">
  <img src="/Imagenes/IntroRos.PNG" width="1000" />
</p>

## Solucion planteada

Para abordar el problema, se implementó la siguiente estrategia:

- Se estableció la configuración para el descriptor de archivos con el fin de establecer condiciones para la entrada de datos.
- Se separaron los carácterés necesarios para la función específica de cada uno.
- Se establecio la velocidad del movimiento lienar y angular del sistema.
- Se diseño un control absoluto y relativo del sistema para una posición y un movimiento preciso.

## Funciones y comandos utilizados

Con ayuda de las diferentes documentaciones de ROS se usaron diferentes funciones y comandos que nos premitieron realizar desplazamientos, establecer nodos, subscripciones, entre otros.

1. Comandos de configuración dl proyecto
    - *roscore:* Activa o desactiva la salida de los motores del brazo robótico.
    - *Srosrun turtlesim turtlesim node:* Se esta ejecutando el nodo turtlesim_node del paquete turtlesim. Este nodo es responsable de crear la ventana de simulación de TurtleSim la cual nos permite obtener un entorno gráfico los diferentes movimientos y comportamientos que puede tener el proyecto del turtle
    - *source devel/setup.bash:* Se esta indicando por un terminal que ejecute los comandos dentro de setup.bash, lo cual configura el entorno para  encontrar los paquetes de ROS que ham sido compilado y utilizarlos correctamente.
2. Funciones de desplazamiento
    - *Go:* Desplaza el robot a un punto realizando un movimiento puntual, es necesario en este caso mencionar el movimieintomen Z para desplazarlo verticalmente como una función aparte, se aclara que por medio de este movimiento el robot sufre menos esfuerzos por lo que es menos posible que aparezcan errores en este caso.
    - *Move:* Desplaza el robot hasta el punto referenciado usando una interpolación lineal, aunque usa un trayecto mas corto puede afectar alguna de las articulaciones del robot
    - *Wait:* Se encarga de pausar la ejecución del código hasta cumplir una condición específica, ya sea por alguna señal de entrada, un tiempo determinado, entre otras.
    - *Call:* Se considera como un llamado a una función externa a la que se este realizando.

## [Integración con Matlab](/Lab3)
<p align="center">
  <img src="/Imagenes/Matlab_subscription.png" />
</p>
<p align="center">
  <img src="/Imagenes/Subs_res.png" />
</p>
<p align="center">
  <img src="/Imagenes/Teleport_res.png" />
</p>
<p align="center">
  <img src="/Imagenes/Matlab_Tranport_res.png"/>
</p>

## [Integración con Python](/catkin_ws/devel/lib/hello_turtle/myTeleopKey.py)

Para el diseño del código se inició importando las diferentes librerías necesarias para los diferentes movimientos que se esperaba fuera a tener el sistema, inmediatamente se creo el llamado de la función main() con la interrupción *rospy.ROSInterruptException* relacionada con el cierre de nodos causadas por el usuario o el mismo sistema procediendo a crear las diferentes funciones.
<p align="center">
  <img src="/Imagenes/LlamadoMain.PNG" />
</p>

En la función de ingreso por teclado se inicio creando una entrada para los descriptores de archivos para de este modo guardar los diferentes atributos que conformas los archivos en la variable *old* y *new*, en los atributos de linea del terminal de la variable new *(lflag)* se especifico evitar la cadena de carácteres y que este no fuera impreso, mientras que para sus carácteres de configuración del terminal *(cc)* se configuró un mínimo de carácteres de 1 y tiempo cero para continuar con la ejecución del código. Finalmente se guardan las nuevas configuraciones del descriptor de archivos con la función *TCSETATTTR* y se lee la entrada de datos del mismo descriptor para guardarlo en la variable c.

<p align="center">
  <img src="/Imagenes/funcionTeclado.PNG" />
</p>

Para la función de movimientos se hizo usop del bojeto *publisher* de la librería rospy, en esta se indicó el tópico *cmd_vel* mostrando el tipo de función que iba a tener el nodo turtle1 y tipo de mensaje *geometry_msgs* 
representando la forma de mensaje que se va a enviar, se creo el mensaje con la función *Twist()* para configurar la velocidad de este por medio de *.lineal.x* para un moviminento lineal y *.angular.z* para una rotación. Finalmente se procedió a enviar el mensaje del publicacod a una frecuencia de envio de 10hz.
<p align="center">
  <img src="/Imagenes/funcionMovimientoLinealAngular.PNG" />
</p>

Para la función de movimientos 

<p align="center">
  <img src="/Imagenes/LlamadoMain.PNG" />
</p>

Se creó la función paletizado externo la cual consiste en el diseño deun pallet através de una matriz 4x4 y que pase por los 16 puntos entre los cuales se encuentran las posiciones de "Origen", del "EjeX" y del "EjeY" por medio de una fuinción ciclica de 16 posiciones.

<p align="center">
  <img src="/Imagenes/LlamadoMain.PNG" />
</p>

Finalmente se diseño en la función main un ciclo el cual leyera cada una de las entradas, al tener una señal de entrada en el bit 512, el sistema activara la salida del bit 515 y llamara la función del paletizado Z, por otro lado al activar la entrada del bit 513 este llamara la función del paletizado en S activando la salida del biot 516, y finalmente con la señal de entrada del bit 514 se llamara la funcion del paletizado externo activando del mismo modo la salida del bit 517.

<p align="center">
  <img src="/Imagenes/LlamadoMain.PNG" />
</p>

Para acceder al código puede seleccionar el subtítuo de esta sección "Código main EPSON" o darle clic [aquí](/Lab2/Main.prg)

