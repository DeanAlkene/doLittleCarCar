# coding:utf-8
import serial
import serial.tools.list_ports
'''
A: GO AHEAD
B: GO BACK
C: GO BACK FAST
F: GO AHEAD FAST
L: TURN LEFT (LEFT WHEEL STOP)
M: TURN LEFT ANGLE (LEFT WHEEL RUN)
N: TURN RIGHT ANGLE (RIGHT WHEEL RUN)
P: PARK
R: TURN RIGHT (RIGHT WHELL STOP)
'''
def comBlutooth(op, port):
    op = bytes(op.encode())
    port.write(op)
    prompt = port.readline()
    prompt.strip()
    prompt = str(prompt.decode())
    print(prompt)

def main():
    port = serial.Serial("COM4", 9600, timeout = 1)
    op = input();
    while op != 'S':
        comBlutooth(op, port)
        op = input()
    comBlutooth('S', port)
main()