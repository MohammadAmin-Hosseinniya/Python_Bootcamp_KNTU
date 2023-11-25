# in kod adadha ro ba ham jam mikone, ta vaghti ke majmooeshoun az 100 bezane balatar

sum = 0

while sum < 100:
    adad = int(input("KHOB BEGOO: "))
    sum += adad

    if sum > 100:
        print("zarfiyat : ", sum - 101)
        sum -= adad

    if sum == 100:
        break
    print(sum)

print("Halghe tamoum shod")
print("jame nahayi shod ", sum)
