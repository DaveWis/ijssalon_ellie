#aanbieding
def aanbieding_1(smaak, prijs, korting):
    korting = prijs - prijs * korting
    print(f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {korting} euro")

text = aanbieding_1("aardbei", 4, 0.1)

# Inkomsten totaal 
# ik heb het idee dat dit simpeler kan...
def inkomsten_totaal(inkomsten, btw_percentage):
    totaal = sum(inkomsten)
    btw_bedrag = totaal * btw_percentage
    return f"Het totaal van alle inkomsten van deze week is {totaal} euro, waarover {btw_bedrag} euro btw betaald dient te worden."

week_inkomsten = [220, 430, 125, 160, 205, 90, 345]
btw_percentage = 0.09
text_inkomsten = inkomsten_totaal(week_inkomsten, btw_percentage)
print(text_inkomsten)

#Min en Max
def laag_en_hoog(mijn_lijst):
    return max(mijn_lijst), min(mijn_lijst)

mijn_lijst = [220, 430, 125, 160, 205, 90, 345]
max_min = laag_en_hoog(mijn_lijst)
print(max_min)

#gemiddelde
def gemiddelde(mijn_lijst):
    gemiddeld_bedrag = sum(mijn_lijst) / 7 
    return f"De gemiddelde inkomsten deze week zijn {gemiddeld_bedrag} euro."

mijn_lijst = [220, 430, 125, 160, 205, 90, 345]
gemiddelde_text = gemiddelde(mijn_lijst)
print(gemiddelde_text)

#meervoudig hoog/laag - voor de ValueError heb ik chat gpt geraadpleegd
def meervoudig(invoer_lijst):
    if len(invoer_lijst) < 5 or len(invoer_lijst) > 10:
        raise ValueError
    return hoog_en_laag(invoer_lijst)
           
def hoog_en_laag(invoer_lijst):
   return max(invoer_lijst), min(invoer_lijst)

invoer_lijst = [10, 5, 3, 2, 1, 2, 9]
uitkomst_meervoudig = hoog_en_laag(invoer_lijst)
print(uitkomst_meervoudig)

#opdracht 12 begrijp ik niet, waar is het bestand "aanbieding.py", wat is het doel van de functie?












