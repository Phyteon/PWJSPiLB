import serial
import sys
import glob

def serial_ports():
    """ Lists serial port names

        :raises EnvironmentError:
            On unsupported or unknown platforms
        :returns:
            A list of the serial ports available on the system
    """
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')

    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result


def message_slicer(str, col):
    sym_num = len(str)
    slices = []
    if sym_num > 96:
        print("Message too long, please shorten it!\n")

    else:
        i = 0
        volatile_str = ""
        while i < sym_num:
            volatile_str += str[i]
            i = i + 1
            if i % col == 0 or i == sym_num:
                slices.append(volatile_str)
                volatile_str = ""


version = "0.1"
print("Welcome to waifu board connection terminal program!\n")
print("Current version: " + version + "\n")
print("Here is a list of available serial ports:\n")
all_ports = serial_ports()
[print(i + "\n") for i in all_ports]
port = input("Please specify port to which the board is connected:\n")
while not (port in all_ports):
    port = input("You have specified wrong port, please try again:\n")
baud = input("Please specify baud rate:\n")
ser = serial.Serial()
ser.baudrate = baud
ser.port = port
print(ser)
print("Do you wish to establish connection with specified port?\n")
ans = input("y/n? ")
if ans == "y":
    ser.open()
    if ser.is_open():
        print("Connection has been successfully established.\n")
    else:
        print("Unable to establish connection :/\n")

