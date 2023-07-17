import random
import Adafruit_DHT
import time
from azure.iot.device import IoTHubDeviceClient, Message
sensor = Adafruit_DHT.DHT11
pin = 4
CONNECTION_STRING ="HostName=sensordata.azuredevices.net;DeviceId=ZZZZZ;SharedAccessKey=ZZZZZZZZZZZZZZZZZZ"
#Formulas
HI = -8.78469475556 + (1.61139411*temperature) + (2.33854883889*humidity) + (-0.14611605*temperature*humidity) + (-0.012308094*temperature*temperature) + (-0.0164248277778*humidity*humidity)+
(0.002211732*temperature*temperature*humidity) + (0.00072546*temperature*humidity*humidity) + (-0.000003582* *temperature*temperature*humidity*humidity)
TDI = temperature-(0.55-0.0055*humidity)*(temperature-14.5)
THI = 0.8*temperature + ((humidity*temperature)/500)

MSG_SND = ’{{"temperature": {temperature},"humidity":{humidity},"hi": {hi},"tdi": {tdi},"thi": {thi}}}’
while True:
  humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)}

def iothub_client_init():
  client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)

def iothub_client_telemetry_sample_run():
  try:
    client = iothub_client_init()
    print ( "Sending data to IoT Hub, press Ctrl-C to exit" )
    while True:
      msg\_txt_formatted = MSG_SND.format(temperature=temperature,
      humidity=humidity, hi=hi, tdi= tdi,thi=thi)
      message = Message(msg_txt_formatted)
      print( "Sending message: {}".format(message) )
      client.sen\_message(message)
      print ( "Message successfully sent" )
      time.sleep(3)
  return client
