prijzen = { "aardbei" : 3,
         "vanille" : 4,
         "chocolade" : 5,
         }

aardbei_prijs = prijzen["aardbei"]

aanbieding_prijs = aardbei_prijs * 0.8

prijzen["aanbieding"] = aanbieding_prijs

reclame_text = f"Vandaag in de aanbieding, vanille-ijs, 1 liter - slechts € {aanbieding_prijs}"

reclame_text2 = reclame_text[:62]

reclame_text3 = reclame_text2.upper()

reclame_text4 = reclame_text3.split()


#ik snap niet waarom dit nodig is, .upper werkt zonder de for-loop, is het vanwege de split?
el = [word.lower() for word in reclame_text4]

for word in el:
    if len(word) <= 4:
        print(word.lower())
    else:
        print(word.upper())












