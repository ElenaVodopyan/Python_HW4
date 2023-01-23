data = open('ice-cream.txt', mode = 'r', encoding = 'utf-8')
ice_cream = data.readlines()
data.close()
set1 = set(ice_cream[0].split(' '))
set2 = set(ice_cream[1].split(' '))

print(set1.difference(set2))
