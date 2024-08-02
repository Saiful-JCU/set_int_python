'''
this method prints only items that are not similar to both the sets.
'''

cities = {'tokyo', 'madrid', 'berlin'}
cities1 = {'tokyo', 'seoul', 'kabul'}
union = cities.symmetric_difference(cities1)
print(union)

cities3 = cities.symmetric_difference_update(cities1)
print(cities3)
