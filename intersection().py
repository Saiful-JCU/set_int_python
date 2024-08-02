'''
the intersection() method returns a new set whereas intersection that's have only items that are similar to both the stes
'''

cities = {'tokyo', 'madrid', 'berlin'}
cities1 = {'tokyo', 'seoul', 'kabul'}
union = cities.intersection(cities1)
print(union)

cities3 = cities.intersection_update(cities1)
print(cities3)