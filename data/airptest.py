import requests

url = 'http://openapi.airport.co.kr/service/rest/dailyExpectPassenger/dailyExpectPassenger'
params ={'serviceKey' : '/y02phtYoWtYhxVsVYBkkGHFDcKWEC/Dd8IMHp4Zx7kj2Q4oEcTbXbp74nZSOsLu8wmeYkB76HxQqRdIoJNmkg==', 'schDate' : '20220217', 'schAirport' : 'PUS', 'schTof' : 'I', 'schHH' : '16' }

response = requests.get(url, params=params)
print(response.content)