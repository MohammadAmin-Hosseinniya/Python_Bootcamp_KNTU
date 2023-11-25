manchester = (input("Manchester bazi dare? (y/n)") == "y")
milan = (input("milan bazi dare? (y/n)") == "y")
perspolis = (input("perspolis bazi dare? (y/n)") == "y")

print(manchester)

if manchester or milan or perspolis:
    print("football bebein!")
else:
    print("film bebein.")