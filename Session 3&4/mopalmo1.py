import random
for i in range(0,3):
    counter = 0

    zere = random.randint(1,100)
    print('moghavemate zereh : ' , zere)
    shamshir = 20
    print('moghavemate shamshir : ' , shamshir)

    while shamshir < zere :
        shamshir += random.randint(3,5)
        counter += 1
        print(shamshir)

    print('Afarin!')
    print('toonestim tooye {} bar be ghod'.format(counter))








