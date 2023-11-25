protein = []
vitamin =[]
carbohydrat = []
drinks = []

list_kharid = [protein, vitamin, carbohydrat , drinks]
kinds_of_food = ['protein', 'vitamin', 'carbohydrat' , 'drinks']
# print(kinds_of_food)

for item in range(0,4):
    list_kharid[item].append(input('baraye {} chi bekharim? '.format(kinds_of_food[item])))

print('baraye protein ina ro bekhar :')
print(list_kharid[0])
print('=======================================')

print('baraye vitamin ina ro bekhar :')
print(list_kharid[1])
print('=======================================')

print('baraye carbo ina ro bekhar :')
print(list_kharid[2])
print('=======================================')

print('baraye nushidani ina ro bekhar :')
print(list_kharid[3])
#in print ha ro behtare ba for benevisim