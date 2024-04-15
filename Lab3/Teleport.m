%%
rosshutdown;
rosinit; %Conexi ́on con nodo maestro
%%
teleportClient = rossvcclient('/turtle1/teleport_absolute','turtlesim/TeleportAbsolute');
teleportMsg= rosmessage(teleportClient);
teleportMsg.X = 10;
teleportMsg.Y= 10;
teleportMsg.Theta=0;
poseSubs = rossubscriber('/turtle1/pose','turtlesim/Pose');
%%
call(teleportClient,teleportMsg);
pause(1)
disp(poseSubs.LatestMessage);