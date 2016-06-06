import pygeoip


gi = pygeoip.GeoIP('./GeoLiteCity.dat')

def printRecord(tgt):
	rec = gi.record_by_name(tgt)
	city = rec['city']
	region = rec['region_code']
	country = rec['country_name']
	longitude = rec['longitude']
	latitude = rec['latitude']

	print('[*] Target: ' + str(tgt) + ' Geo-located.')
	print('[+] ' + str(city) + ', ' + str(region) + ', ' + str(country))
	print('[+]  Latitude: ' + str(latitude) + ', Longitude: ' + str(longitude))

#TODO: don't hard code ip but pass via command line.
tgt = '173.255.226.98'
printRecord(tgt)
