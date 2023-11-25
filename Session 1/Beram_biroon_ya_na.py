bacheha = input("bacheha radifan? (y/n) ")
maman_baba = input("maman babat okeyan? (y/n) ")
mashgha = input("mashghato neveshti? (y/n) ")

if (bacheha == "y"):
    bacheha = True
else:
    bacheha = False

if (maman_baba == "y"):
    maman_baba = True
else:
    maman_baba = False

if (mashgha == "y"):
    mashgha = True
else:
    mashgha = False


if bacheha and maman_baba and mashgha:
    print("khosh begzare pas!!")
elif (not bacheha) and maman_baba and mashgha:
    print("kheyli badbakhti!!!")
elif bacheha and (not maman_baba) and mashgha:
    print("boro mozakere kon...")
elif bacheha and maman_baba and (not mashgha):
    print("beshin sare jat mashghato benvis harfam nazan.")

# We have three conditions. Each can be either True or False. then, we have 2*2*2 situations at all. which we have...
# considered four of them here. You can add rest of them and play with announcments you show to the user!
