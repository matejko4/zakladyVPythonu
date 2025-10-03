'''
Odsazování v Pythonu (indentation)

Většina programovacích jazyků jako C, C++, Java nebo JavaScript používá k vymezení bloků kódu složené závorky (braces).
V Pythonu se používá odsazování. Blok kódu (např. tělo funkce, cyklu atd.) tedy začíná s odsazením a končí prvním
neodsazeným řádkem.
Počet mezer v odsazení je libovolný, ale musí být konzistentní aspoň v rámci jednoho bloku.
K odsazení musí být použita minimálně jedna mezera.
Obvykle se k odsazování používá tubulátor, který bývá nejčastěji nastaven na 4 mezery.
'''
"""
# Odsazení bloku kódu uvnitř cyklu a podmínky
for i in range(1, 10):
    print(i)
    if i % 2 == 0:
        print('even')
    else:
        print('odd')

"""
'''
Dokumentační řetězce v Pythonu (docstrings)

Víceřádkový řetězec následující hned po záhlaví funkce v Pythonu je nazýván docstring (documentation string neboli 
dokumentační řetězec) a obsahuje stručné vysvětlení toho, co funkce provádí.
Přestože je to nepovinný doplněk programového kódu, je považován za "good programming practice", tedy jednu z dobrých
zásad, které by měl programátor v Pythonu dodržovat.
Docstrings se zapisují mezi trojnásobné uvozovky (tedy podobně jako komentáře).
Tyto dokumentační řetězce jsou přístupné prostřednictvím "magického" __doc__ atributu funkce.    
'''

# Odsazení bloku kódu uvnitř funkce a použití docstring
"""
def greet(name):
    '''
    This function greets to the person
    passed in as a parameter
    '''
    print("Ahoj, " + name + "!")
"""
# Vypíše docstring spojený s funkcí greet
#print(greet.__doc__)
# Vyvolá funkci greet s parametrem 'Hilda'
#greet('Hilda')

"""
Cvičení 2:

Vytvořte libovolně pojmenovanou vlastní funkci s minimálně jedním parametrem, v níž využijete cyklus for, 
aspoň jednu podmínku if a funkci print(). Dodržte správné odsazování kódu a opatřete funkci stručnou dokumentací.
Do konzole vypište nejprve docstring vaší funkce a potom zavolejte funkci samotnou.   
"""

def statistika_tymu(goly, zapasy, body):
    """
    Vypočítá základní statistiky týmu (góly/zápas, kolik procent bodů ziskali, slovní hodnocení).
    """

    if zapasy <= 0:
        print("Počet zápasů musí být kladné číslo.")
        return
    elif zapasy * 3 < body:
        print("Počet bodů nemůže být vyšší než maximální možný počet bodů.")
        return
    
    prumer_golu = goly / zapasy
    max_body = zapasy * 3  
    procento_bodu = (body / max_body) * 100 if max_body > 0 else 0

    print(f"Góly celkem: {goly}")
    print(f"Zápasy: {zapasy}")
    print(f"Body: {body} / {max_body} ({procento_bodu:.1f} %)")
    print(f"Průměr gólů na zápas: {prumer_golu:.2f}")

    
    hvezdy = int(round(prumer_golu))
    print("Útočná síla:", end=" ")
    for _ in range(hvezdy):
        print("*", end="")
    if hvezdy == 0:
        print("Tragédie")
    else:
        print()

    if procento_bodu >= 90:
        print("Hodnocení: Nejspíše Barcelona")
    elif procento_bodu >= 80:
        print("Hodnocení: Silný tým")
    elif procento_bodu >= 50:
        print("Hodnocení: Průměrný tým")
    else:
        print("Hodnocení: Je čas na změnu trenéra")


print(statistika_tymu.__doc__)
statistika_tymu(10, 22, 9)


