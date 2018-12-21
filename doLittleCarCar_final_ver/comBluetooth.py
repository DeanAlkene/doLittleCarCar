# coding:utf-8
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