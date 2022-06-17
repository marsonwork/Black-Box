from datetime import date, datetime
import csv
from INA219 import *
import sys, os

upsdata = []    #List to store UPS parameters

dashboard = '/var/www/html/index.html'
log_file = "/home/pi/UPS-Hat/upslog.csv" #For log to be at particular locaiton

#1: Print enable
#0: Print disable
debug_en = 1 

ina219 = INA219(addr=0x42)

# Disable print
def blockPrint():
    sys.stdout = open(os.devnull, 'w')

# Enable print
def enablePrint():
    sys.stdout = sys.__stdout__

def update_html(voltage,current,power,percentage,cputemp):
        f = open(dashboard, 'w')
        html_code = '''
        <!DOCTYPE html>
        <html>
        <head>
                <title>Black Box Health Monitor</title> 
                <meta http-equiv="refresh" content="2">
                <style>
                        .styled-table {
                            border-collapse: collapse;
                            margin: 25px 0;
                            font-size: 0.9em;
                            font-family: sans-serif;
                            border-radius: 5px 5px 0 0;
                            overflow: hidden;
                            min-width: 400px;
                            box-shadow: 0 0 20px rgba(0, 0, 0, 0.15);
                            margin-left: auto;
                        margin-right: auto;
                        margin-top: 100px;
                                margin-bottom: 100px;
                        }
                        .styled-table thead tr {
                            background-color: #009879;
                            color: #ffffff;
                            text-align: center;
                        }
                        .styled-table th,
                        .styled-table td {
                        padding: 12px 15px;
                        }
                        .styled-table tbody tr {
                            border-bottom: 1px solid #dddddd;
                        }

                        .styled-table tbody tr:nth-of-type(even) {
                            background-color: #f3f3f3;
                        }

                        .styled-table tbody tr:last-of-type {
                            border-bottom: 2px solid #009879;
                        }
                        .styled-table tbody tr.first-row {
                            font-weight: bold;
                        color: #009879;
                        text-align: center;
                        }
                        h1 {
                                color: #009879;
                                font-family: courier;
                                font-size: 40px;
                                font-weight: bold;
                                margin-top: 100px;
                                margin-bottom: 1px;
                                text-align: center;
                        }
                </style>
        </head>
        <body>
                <h1>Black Box Health Monitor</h1>
                <table class="styled-table">
                    <thead>
                        <tr>
                            <th>UPS Voltage</th>
                            <th>Current Drawn</th>
                            <th>Power Consumption</th>
                            <th>Battery Percentage</th>
                            <th>Pi's CPU Temp</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr class="first-row">
                            <td>'''+voltage+'''</td>
                            <td>'''+current+'''</td>
                            <td>'''+power+'''</td>
                            <td>'''+percentage+'''</td>
                            <td>'''+cputemp+'''</td>
                        </tr>
                        <!-- and so on... -->
                    </tbody>
                </table>
        </body>
        </html>
        '''
        # writing the code into the file
        f.write(html_code)
        # close the file
        f.close()

def temperature_of_raspberry_pi():
        cpu_temp = os.popen("vcgencmd measure_temp").readline()
        return cpu_temp.replace("temp=", "")


while True:

        if   debug_en == 1: enablePrint()
        elif debug_en == 0: blockPrint()

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

        pi_cpu_temp=temperature_of_raspberry_pi()

        print("Date: ",today_date)
        print("Time: ",localtime) 
        print("Load Voltage:  {:6.3f} V".format(bus_voltage))
        print("Current:       {:9.6f} A".format(current/1000))
        print("Power:         {:6.3f} W".format(power))
        print("Percent:       {:3.1f}%".format(p))
        print("")

        update_html(LoadVoltage,Current,Power,Percentage,pi_cpu_temp)

        upsdata = [str(today_date),str(localtime),LoadVoltage,Current,Power,Percentage,pi_cpu_temp]

        with open(log_file, 'a+') as csvfile: 
                csvwriter = csv.writer(csvfile)
                csvwriter.writerow(upsdata)

        time.sleep(60)
