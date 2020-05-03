from pypostalcode import PostalCodeDatabase
pcdb = PostalCodeDatabase()
location = pcdb['V5K']
print(location.postalcode)
print(location.city)
print(location.province)
