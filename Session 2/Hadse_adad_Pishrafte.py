import random
count = 0
adad = random.randint(1, 10000)

hads = int(input("Begoo hads bezan: "))

while hads != adad:
    if hads < adad:
        print("Kame Bishtar begoo.......")
    elif hads > adad:
        print("Lotfan Biya payintar baba.......")

    hads = int(input("Begoo hads bezan: "))
    count += 1
print("Tamoome berid esterahat")
print("Tedad hads ha: ", count)
