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

## Integración con Matlab

## [Integración con Python](/LogoTesla/ControllerData/IRB140_6_81/RAPID/TASK1/PROGMOD/Module1.mod)

Para el diseño del código se inició crando un punto nombrado como HOME, desde el cual el robot parte para iniciar las trayectorias. Seguido a esto se crean puntos para el origen, el EjeX y el EjeY, los cuales nos ayudan para referenciar los mapeos que se realizan durante las trayectorias.

<p align="center">
  <img src="/Imágenes/CreacionHerramienta.PNG" />
 <img src="/Imágenes/Puntos_X_Y_Origen.PNG" style="width: 45%; height: auto;" />
</p>

A continuación se crearon los diferentes nombres como referencia para cada una de las salidas, desde la función main se activaron los motores y se establecio una salida de potencia alta en cada uno de estos, una vez pasados por los puntos del estado HOME, se procedió a pasar por los puntos creados de "Origen", "EjeX" y "EjeY", con el fin de evaluar los mapeos que se van a crear atraves de estosl.

<p align="center">
  <img src="/Imágenes/Codigo_TrayectoriaHOME.PNG" />
</p>

Se creó la función paletizado Z el cual consiste en realizar una trayectorias en forma de Z atraves de una matriz diseñada de 3x3 y que llegue a los puntos de origen, del eje x y del eje Y, para esto se diseñó una función ciclica por el cual pasara por todos los puntos del Pallet del 1 al 9.

<p align="center">
  <img src="/Imágenes/Codigo_FuncionPaletizadoZ.PNG" />
</p>

Se creó la función paletizado S el cual consiste en realizar una trayectorias en forma de S através de una matriz diseñada de 3x3 y que llegue a los puntos de origen, del eje x y del eje Y, para esto se paso como una secuencia normal de los 9 puntos con una funcion ciclica, al llegar al punto 4, esta pasa inmediatamente a la posición 6, mientras que cuando llegue al punto 6 esta debe pasar por la posición 4, el resto de las posiciones si conservan sus mismos puntos.

<p align="center">
  <img src="/Imágenes/Codigo_FuncionPaletizadoS.PNG" />
</p>

Se creó la función paletizado externo la cual consiste en el diseño deun pallet através de una matriz 4x4 y que pase por los 16 puntos entre los cuales se encuentran las posiciones de "Origen", del "EjeX" y del "EjeY" por medio de una fuinción ciclica de 16 posiciones.

<p align="center">
  <img src="/Imágenes/Codigo_FuncionPaletizadoExterno.PNG" />
</p>

Finalmente se diseño en la función main un ciclo el cual leyera cada una de las entradas, al tener una señal de entrada en el bit 512, el sistema activara la salida del bit 515 y llamara la función del paletizado Z, por otro lado al activar la entrada del bit 513 este llamara la función del paletizado en S activando la salida del biot 516, y finalmente con la señal de entrada del bit 514 se llamara la funcion del paletizado externo activando del mismo modo la salida del bit 517.

<p align="center">
  <img src="/Imágenes/Codigo_CicloTrayectorias.PNG" />
</p>

Para acceder al código puede seleccionar el subtítuo de esta sección "Código main EPSON" o darle clic [aquí](/Lab2/Main.prg)

## Videos de pruebas de funcionamiento

Simulación

https://github.com/jlvillalobosj/Robot_EPSON/assets/57506705/6cfeb508-4afe-40cf-9301-b48298c972de

Prueba Real

https://github.com/jlvillalobosj/Robot_EPSON/assets/57506705/5ce8e1dd-460b-4427-b27b-d27af2a8e11b


