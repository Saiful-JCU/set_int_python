'''
the union() method returns a new set whereas update() method adds item into the existing set from another set.
'''

cities = {'tokyo', 'madrid', 'berlin'}
cities1 = {'tokyo', 'seoul', 'kabul'}
union = cities.union(cities1)
print(union)

cities3 = cities.update(cities1)
print(cities3)


