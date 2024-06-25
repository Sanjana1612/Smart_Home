import serial
import time
import telepot
bot=telepot.Bot('6590059318:AAHbG5S8IlG_b9BuIzDajHZmQVWIUlKOXEc')
data = serial.Serial(
                    'COM6',
                    baudrate = 9600,
                    parity=serial.PARITY_NONE,
                    stopbits=serial.STOPBITS_ONE,
                    bytesize=serial.EIGHTBITS,
                    timeout=1
                    )


while True:
    Data = data.read()
    Data = Data.decode('utf-8', 'ignore')
    # print("Raw data is ---- {}  ---".format(Data))
    print(Data)
    if Data=='G':
        print('GAS LEAKAGE')
        bot.sendMessage('1887483813',str('GAS LEAKAGE DETECTED'))
    if Data=='F':
        print('FIRE LEAKAGE')
        bot.sendMessage('1887483813',str('FIRE DETECTED'))
    

