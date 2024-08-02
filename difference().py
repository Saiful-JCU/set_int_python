'''
this method prints only items that are only items that are only present in the original set and not in both the sets.
'''

cities = {'tokyo', 'madrid', 'berlin'}
cities1 = {'tokyo', 'seoul', 'kabul'}
union = cities.difference(cities1)
print(union)

cities3 = cities.difference_update(cities1)
print(cities3)

