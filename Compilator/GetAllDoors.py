import requests
import os
import xml.etree.ElementTree as ET
import configparser

config = configparser.ConfigParser()
config.read(os.path.abspath("Config.ini"))

host = str(config["TESA"]["IP"])
service = 'DoorsWebService'
body_close_door = """<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
xmlns:soap="http://soap.ws.ts1000.tesa.es/">
 <soapenv:Header/>
 <soapenv:Body>
 <soap:doorGetAll>
 <operatorName>{}</operatorName>
 <operatorPassword>{}</operatorPassword>
 </soap:doorGetAll>
 </soapenv:Body>
</soapenv:Envelope>
""".format(str(config["TESA"]["test_user"]),str(config["TESA"]["test_pass"]))
url = f"https://{host}:8181/TesaHotelPlatform/{service}"   
headers = {'Content-Type': 'text/xml'}
try:
    response = requests.post(url, data=body_close_door, headers=headers, verify=False)
    root = ET.fromstring(response.content)
    for wireless_door in root.findall('.//wirelessDoor'):
        door_name = wireless_door.find('doorName').text
        door_id = wireless_door.find('doorId').text
        print(f"Puerta '{door_name}' con id '{door_id}'")
except Exception as e:
    print(e)

#Tener en cuenta que puede cambiar entre TesaHotelPlatform y ServerPlatform dependiendo de donde entremos