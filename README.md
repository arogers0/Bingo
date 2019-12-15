# Bingo Simulator
This game is part of my ECEG 240 Digital System Design final group project. The simulation displays three 5x5 bingo boards side-by-side in a GUI. A button labeled "Call Value" may pull a value that is on one or multiple boards, at which point that square on the board will light up. When used with a 5x5 array of LEDs, the boards can be displayed on the hardware by clicking "Board 1", "Board 2", or "Board 3".
### Running the code
The simulator is designed to be entirely run from a raspberry pi 3 connected to a breadboard with LED's arranged in a 5x5 matrix, with the LED at 0x0 corresponding to port 2, increasing by row until LED at 4x4 corresponding to port 26. The raspberry pi should also be connected to a monitor and keyboard so that the GUI can be interacted with. Run `GPIOmain.py` for this.
If only using the GUI without the raspberry pi attached, run `main.py`.
### Stat Analysis
`Stat Analysis Results.pdf` shows the result of us running `STATmain.py` many times with different numbers of boards. The code determines, given a number of boards and number of times to loop, the average number of tiles that need to be called before a winner is declared and how many times each board won. To perform your own stat analysis, edit and run `STATmain.py`.
