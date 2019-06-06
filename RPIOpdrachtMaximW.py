import paho.mqtt.client as mqtt
import Adafruit_CharLCD as LCD
import RPi.GPIO as GPIO
import time
import smbus

broker_address="broker.mqttdashboard.com"

mijni2c = smbus.SMBus(1)
adres = 0x08

GPIO.setmode(GPIO.BCM)

ipin = 26

aan = False

GPIO.setup(16, GPIO.OUT)
GPIO.setup(21,GPIO.OUT)
GPIO.setup(ipin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

rs, en, d4, d5, d6, d7, backlight, cols, rows = 25, 24, 23, 17, 18, 22, 4, 16, 2

ph = 0

lcd = LCD.Adafruit_CharLCD(rs, en, d4, d5, d6, d7, cols, rows, backlight)

# Map functie voor converteren waarde ph meter
def map( x,  in_min, in_max, out_min, out_max):
    return float(x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

# WRITE functie voor log file laatste stand systeem bij unexpected powerdown
def writeFile(motorStand, PH) :
    fo = open("/home/pi/Documents/file.txt", "w")
    fo.write("Wat was de laatste motor stand?: \n")
    fo.write(str(motorStand) + "\n" )
    fo.write("Wat was de laatst gemeten PH-waarde?: \n")
    fo.write(str(PH) + "\n" )
    fo.close()

def icb(c):
    print("Remote mode enabled")
    lcd.clear()
    lcd.message("Remote access")
    client.connect("broker.mqttdashboard.com", 1883, 60)

GPIO.add_event_detect( ipin, GPIO.RISING, callback=icb, bouncetime=30 )

def on_connect(client, userdata, flags, rc):
    print("connected with result " +str(rc))
    client.subscribe("t/t")

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    global aan
    if msg.payload.decode() == "ON":
     print("Motor on")
     client.publish("t/t","Turned water loop ON")
     GPIO.output(21, GPIO.HIGH)
     aan = True
     writeFile(aan, ph)
     lcd.set_cursor(0,1)
     lcd.message('Motor OFF')
    if msg.payload.decode() == "LOOP":
     main()
    if msg.payload.decode() == "PORTION":
     geefVoeding()

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("broker.mqttdashboard.com", 1883, 60)

# Main loop
def main():
    while True:
     if GPIO.event_detected(ipin):
      break
     if ph < 7:
      geefVoeding()
     leesPhWaarde()
     motorLoop()

# Lees de ph-waarde
def leesPhWaarde():
    global ph
    databyte = mijni2c.read_byte(adres)
    ph = map(databyte, 0, 255, 14, 0)
    ph = round(ph,3)
    time.sleep(1)
    lcd.clear()
    lcd.message('PH-waarde: {0}'.format(ph))

# Main water loop
def motorLoop():
    print("Motor on")
    GPIO.output(21,GPIO.HIGH)
    lcd.set_cursor(0,1)
    lcd.message('Motor ON')
    global aan
    aan = True
    writeFile(aan, ph)
    time.sleep(6)
    print("Motor off")
    GPIO.output(21,GPIO.LOW)
    lcd.set_cursor(0,1)
    lcd.message('Motor OFF')
    aan = False
    time.sleep(2)
    writeFile(aan, ph)

# Breng de ph balans van de planten in orde
def geefVoeding():
    lcd.set_cursor(0,1)
    lcd.message('Voeding   ')
    GPIO.output(16, GPIO.HIGH)
    print('voeding')
    time.sleep(3)
    GPIO.output(16, GPIO.LOW)

# Run main loop at start
main()

client.loop_forever()
GPIO.cleanup()


