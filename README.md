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
    - *roscore:* Activa el nodo maestro.
    - *Srosrun turtlesim turtlesim node:* Se esta ejecutando el nodo turtlesim_node del paquete turtlesim. Este nodo es responsable de crear la ventana de simulación de TurtleSim la cual nos permite obtener un entorno gráfico los diferentes movimientos y comportamientos que puede tener el proyecto del turtle
    - *source devel/setup.bash:* Se esta indicando por un terminal que ejecute los comandos dentro de setup.bash, lo cual configura el entorno para  encontrar los paquetes de ROS que ham sido compilado y utilizarlos correctamente.
   - *rosinit:* Activa la conexión al nodo maestro local.
   - *rosshutdown:* Cierra la conexión al nodo maestro local.
   - *rossubscriber:* Crea un subscriptor a un tópico específico con un tipo de mensaje específico.
   - *rosscvclient:* Genera un cliente para un servicio.
## [Integración con Matlab](/Lab3)
En primer lugar, se debe cerrar la conexión usando el comando <i>rosshutdown</i>. Acto seguido se hizo uso del comando <i>rosinit</i> para realizar la conexión con el nodo maestro local.
Se crea un publicador al tópico que controla la velicidad tanto angular como linear del robot. Se modifica el mensaje a mandar de tal forma que se envie una velocidad lineal en x de 1 (y por la forma en que funciona este publicador, actuará con esta velocidad por 1 segundo).
Se realizó la suscripción al tópico pose usando el comando <i>rossubscriber</i> del toolbox de Ros de Matlab. Esta suscripción permite acceder al evento en el que se actualiza la pose del robot y reaccionar adecuadamente.
Por último se realizó el envio del mensaje actualizado lo que genera un cambio en la velocidad del robot, y por lo tanto varios cambios en la pose del robot. 
<p align="center">
  <img src="/Imagenes/Matlab_subscription.png" />
</p>

En la siguiente figura, se puede apreciar el resultado del último de los cambios en la pose:

<p align="center">
  <img src="/Imagenes/Subs_res.png" />
</p>

Para poder modificar la pose del robot se deben usar los servicios expuestos por turtlesim. Más específicamente, el servicio <i>TeleportAbsolute</i> mediante el cuál se puede realizar este cambio. Para realizar este cambio se crea un cliente para el servicio de "Teleport Absolute" mediante el comando <i>rossvcclient</i> en donde se especifica el servicio y el tipo de mensaje asociado al servicio. Después se crea y configura el mensaje, en donde en este caso se tienen los parámetros X, Y y Theta de la pose del robot. y por último se utiliza la función <i>call</i> para hacer la llamada al servicio.
<p align="center">
  <img src="/Imagenes/Teleport_res.png" />
</p>
En la siguiente figura se puede el resultado de llamar este servicio 2 veces, uno con parámetos(1,1,0) y después con (10,10,0). 
<p align="center">
  <img src="/Imagenes/Matlab_Tranport_res.png"/>
</p>
Se puede ver claramente como la pose del robot se comporta adecuadamente.

## [Integración con Python](/catkin_ws/devel/lib/hello_turtle/myTeleopKey.py)

Para el diseño del código se inició importando las diferentes librerías necesarias para los diferentes movimientos que se esperaba fuera a tener el sistema, inmediatamente se creo el llamado de la función main() con la interrupción *rospy.ROSInterruptException* relacionada con el cierre de nodos causadas por el usuario o el mismo sistema procediendo a crear las diferentes funciones.
<p align="center">
  <img src="/Imagenes/LlamadoMain.PNG" />
</p>

En la función de ingreso por teclado se inicio creando una entrada para los descriptores de archivos para de este modo guardar los diferentes atributos que conformas los archivos en la variable *old* y *new*, en los atributos de linea del terminal de la variable new *(lflag)* se especifico evitar la cadena de carácteres y que este no fuera impreso, mientras que para sus carácteres de configuración del terminal *(cc)* se configuró un mínimo de carácteres de 1 y tiempo cero para continuar con la ejecución del código. Finalmente se guardan las nuevas configuraciones del descriptor de archivos con la función *TCSETATTTR* y se lee la entrada de datos del mismo descriptor para guardarlo en la variable c.

<p align="center">
  <img src="/Imagenes/funcionTeclado.PNG" />
</p>

Para la función de movimientos se hizo uso del bojeto *publisher* de la librería rospy, en esta se indicó el tópico *cmd_vel* mostrando el tipo de función que iba a tener el nodo turtle1 y tipo de mensaje *geometry_msgs* 
representando la forma de mensaje que se va a enviar, se creo el mensaje con la función *Twist()* para configurar la velocidad de este por medio de *.lineal.x* para un moviminento lineal y *.angular.z* para una rotación. Finalmente se procedió a enviar el mensaje del publicacod a una frecuencia de envio de 10hz.
<p align="center">
  <img src="/Imagenes/funcionMovimientoLinealAngular.PNG" />
</p>

Para establecer la posición absoluta en el punto central del sistema, se hace uso del servicio de *TeleportAbsolute* del nodo de turtle1. Inicialmente con la ayuda de la librería *ServiceProxy* se busca establecer una conexión con el sistma del nodo turtle1 y guardarñp en la variable teleport_mainPosition, se crea la variable req para instanciar las peticiones del cual para este caso constan de la posicipon x, y y una orientación fija. Finalmente se realiza la comunicación con el nodo en base a las peticiones establecidas

<p align="center">
  <img src="/Imagenes/funcionAbsoluta.PNG" />
</p>

Para indicar un movimiento preciso en base a la última pose del dispositivo, se hace uso del servicio TeleportRelative, el cual al contar con una estructura similar al servicio absoluto se hace un cambio úncamente en sus argumentos, ya que este se basa en sus ángulos de euler indicando un movmiento angular y lineal.

<p align="center">
  <img src="/Imagenes/funcionRelativa.PNG" />
</p>

Finalmente se diseñó en la función main un llamado a las diferentes funciones creadas basados en los requerimientos tales que al tener una entrada por teclado *'w'* o *'s'* se llama al movimiento lienal del proyecto turtle, con un ingreso *'a'* y *'d'* se hacen rotaciones sobre su eje z, con la entrada *'r'* se realiza una rotación de 180° de la posición en la que se encuentre y con una entrada *'space'* vuelve al punto centro del proyecto con x=5.5, y=5.5 y theta=0.

<p align="center">
  <img src="/Imagenes/funcionMain.PNG" />
</p>

[screen-recording.webm](https://github.com/jhonathann/Intro-a-Ros/assets/57506705/d58d1299-fac2-4a72-9d05-03f57812d0ab)

