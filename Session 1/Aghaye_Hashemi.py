foroushe_agha_reza = input("Foroushe Agha Reza ro behem begoo: ")
foroushe_MahLagha_khanom = input("Foroushe MahLagha Khanom ro behem begoo: ")
foroushe_Soltan_Mahmoud = input("Foroushe Soltan Mahmoud ro behem begoo: ")

foroushe_agha_reza = int(foroushe_agha_reza)
foroushe_MahLagha_khanom = int(foroushe_MahLagha_khanom)
foroushe_Soltan_Mahmoud = int(foroushe_Soltan_Mahmoud)

if (foroushe_agha_reza > foroushe_Soltan_Mahmoud) and (foroushe_agha_reza > foroushe_MahLagha_khanom):
    print("Padashe in mah taghdim mishavad beeeeee.... Agha Rezaaaa!!!")
elif foroushe_MahLagha_khanom > foroushe_agha_reza and foroushe_MahLagha_khanom > foroushe_Soltan_Mahmoud:
    print("Barandeye padashe in mah kasi nist jozzzz....... MahLagha Khanooommmm!!!!")
elif foroushe_Soltan_Mahmoud > foroushe_agha_reza and foroushe_Soltan_Mahmoud > foroushe_MahLagha_khanom:
    print("Padashe in mah ra be dargahe homayouniye soltan mahmoud arze midarim. bashad ke maghboul oftad...")
else:
    print("Padashe in mah taghsim mishavad beyne se foroushande.")
