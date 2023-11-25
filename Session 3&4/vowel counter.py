# kalame = input("Ye kalame begoo ta vawelhash ro beshmaram: ")
kalame = "radar"
vowels = ["a", "i", "o", "u", "e"]
counter = 0

for i in kalame:
    if i.lower() in vowels:
        counter += 1
print(counter)
