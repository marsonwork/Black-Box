from datetime import date, datetime
import csv
from INA219 import *

data = ["0","0","0","0","0","0"]	#List to store UPS parameters

#1: Print enable
#0: Print disable
debug_en = 1 

ina219 = INA219(addr=0x42)

while True:
        bus_voltage = ina219.getBusVoltage_V()             # voltage on V- (load side)
        shunt_voltage = ina219.getShuntVoltage_mV() / 1000 # voltage between V+ and V- across the shunt
        current = ina219.getCurrent_mA()                   # current in mA
        power = ina219.getPower_W()                        # power in W
        p = (bus_voltage - 6)/2.4*100
        if(p > 100):p = 100
        if(p < 0):p = 0

        # INA219 measure bus voltage on the load side. So PSU voltage = bus_voltage + shunt_voltage
        #print("PSU Voltage:   {:6.3f} V".format(bus_voltage + shunt_voltage))
        #print("Shunt Voltage: {:9.6f} V".format(shunt_voltage))
        today_date = date.today()
        localtime = time.asctime( time.localtime(time.time()) )
        LoadVoltage =str("{:6.3f} V".format(bus_voltage))
        Current =str("{:9.6f} A".format(current/1000))
        Power = str("{:6.3f} W".format(power))
        Percentage = str("{:3.1f}%".format(p))
        data[0] = str(today_date)
        data[1] = str(localtime)
        data[2] = LoadVoltage
        data[3] = Current
        data[4] = Power
        data[5] = Percentage

        if debug_en:
                print("Date: ",today_date)
                print("Time: ",localtime) 
                print("Load Voltage:  {:6.3f} V".format(bus_voltage))
                print("Current:       {:9.6f} A".format(current/1000))
                print("Power:         {:6.3f} W".format(power))
                print("Percent:       {:3.1f}%".format(p))
                print("")	

        with open("upslog.csv", 'a+') as csvfile: 
                csvwriter = csv.writer(csvfile)
                csvwriter.writerow(data)

        time.sleep(5)
