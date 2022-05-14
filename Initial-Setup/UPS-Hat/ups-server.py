from flask import Flask, render_template #Render template is used to use html page  #pip install flask
import os
from INA219 import *

app = Flask(__name__)

'''
@app.route('/'): this determines the entry point; the / means the root of the website, so http://127.0.0.1:5000/
def index(): this is the name you give the route, in this case index, because it’s the index (or homepage) of the website
return 'Hello world': this is the content of the web page, which is returned when the user goes to this URL
'''

def temperature_of_raspberry_pi():
    cpu_temp = os.popen("vcgencmd measure_temp").readline()
    return cpu_temp.replace("temp=", "")


@app.route('/')
def index():
    #Measuring raspberry pi cpu temperature:
    pi_cpu_temp=temperature_of_raspberry_pi()

    #Measuring UPS Parameters:
    bus_voltage = ina219.getBusVoltage_V() 
    current = ina219.getCurrent_mA()
    power   = ina219.getPower_W()
    p = (bus_voltage - 6)/2.4*100
    if(p > 100):p = 100
    if(p < 0):p = 0

    voltage = str("{:6.3f} V".format(bus_voltage))
    current=str("{:9.6f} A".format(current/1000))
    power=str("{:6.3f} W".format(power))
    percentage=str("{:3.1f}%".format(p))
    return render_template('index.html',voltage=voltage,current=current,power=power,percentage=percentage,cputemp=pi_cpu_temp) #This will load the index.html webpage under the templates directory

'''
#New page in html, url/cakes
@app.route('/cakes')
def cakes():
    #return 'Yummy cakes!'
    return render_template('cakes.html')

@app.route('/hello/')
def hello():
    name = "Test"
    return render_template('pages.html',name=name)

'''

#below part runs the web server and your app
if __name__ == '__main__':
    ina219 = INA219(addr=0x42)
    app.run(debug=True, host='0.0.0.0') #the host='0.0.0.0' means the web app is accessible to any device on the network.