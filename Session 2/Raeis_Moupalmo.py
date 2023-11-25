from random import randint

ghodrate_shamshir = 20
moghavemate_zereh = randint(1, 99)

count = 0

while ghodrate_shamshir <= moghavemate_zereh:
    ertegha = randint(3, 5)
    ghodrate_shamshir += ertegha
    count += 1
    print("Mashalla Raeis! In dafe {}ta behtaresh kardi! Karet Aliye Edame bede!".format(ertegha))

print("Sarbaz bad az {} azmayesh, belakhare az pa dar oumad!!".format(count))
print("Moghavemate zereh {} hast".format(moghavemate_zereh))
print("Ghodrate shamshir {} shode.".format(ghodrate_shamshir))

for i in range(4):
    ghodrate_shamshir += randint(3, 5)

print("Ghodrate shamshir bad az pardazeshe mojadad {} shode.".format(ghodrate_shamshir))
