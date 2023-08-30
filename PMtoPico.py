import machine
from time import sleep

def read_pm_data():
    uart = machine.UART(0, baudrate=9600, tx=machine.Pin(4), rx=machine.Pin(5))
    # change the tx and rx pin numbers based on actual connections

    # continuously checks data from sensor, extracts the PM2.5 and PM10 values
    # when valid data is received, and returns values
    while True:
        if uart.any():
            # code reads 32 bytes of data and stores it
            data = uart.read(32)
            # checks if data is not None and verifies first two bytes of data
            # match the expected data frame header values
            if data is not None and data[0] == 0x42 and data[1] == 0x4d:
                # extract PM2.5 & PM10 concentration values from received data
                pm2_5 = data[10] * 256 + data[11]
                pm10 = data[12] * 256 + data[13]
                return pm2_5, pm10

if __name__ == "__main__":
    pm2_5, pm10 = read_pm_data()
    print("PM2.5 concentration:", pm2_5)
    print("PM10 concentration:", pm10)

    # wait for one second before attempting to read from the sensor again
    sleep(1)