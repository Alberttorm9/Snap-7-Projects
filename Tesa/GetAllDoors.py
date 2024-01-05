import requests
import re
host = 'XXX.XXX.XXX.XXX'
service = 'DoorsWebService'
body_close_door = """<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
xmlns:soap="http://soap.ws.ts1000.tesa.es/">
 <soapenv:Header/>
 <soapenv:Body>
 <soap:doorGetAll>
 <operatorName>XXX</operatorName>
 <operatorPassword>XXX</operatorPassword>
 </soap:doorGetAll>
 </soapenv:Body>
</soapenv:Envelope>
"""
url = f"https://{host}:8181/TesaHotelPlatform/{service}"   
headers = {'Content-Type': 'text/xml'}
try:
    response = requests.post(url, data=body_close_door, headers=headers, verify=False)
    response_shown = re.findall(r'<doorName>(.*?)</doorName>', str(response.content))
    response_shown = sorted(response_shown)
    print(response_shown, response.content)
except Exception:
    print(Exception)
