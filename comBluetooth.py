# coding:utf-8
import serial
import serial.tools.list_ports

def comBlutooth(op, port):
    op = bytes(op.encode())
    port.write(op)
    prompt = port.readline()
    prompt.strip()
    prompt = str(prompt.decode())
    print(prompt)

def main():
    port = serial.Serial("COM4", 9600, timeout = 1)
    op = input()
    while op != 'S':
        comBlutooth(op, port)
        op = input()
    comBlutooth('P', port)
main()
    