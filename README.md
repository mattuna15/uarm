# uarm
Uarm Code

blockly - random blockly code for Uarm Studio<br>

network_uarm - network server to allow access to robot over network<br>
    Open a socket on the server port 12345.<br>
    <br>
    Send commands:<br>
      position - receive current position of robot<br>
      info - get current device information<br>
      move - move to position e.g. client.py "move 5 5 5 200 True" use: move x y z speed relative<br>
      reset - reset uarm<br>
