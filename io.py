'''
Vestavěné funkce v Pythonu (built-in functions)

Python nabízí řadu vestavěných funkcí, které jsou okamžitě dostupné rovněž v pythonovské konzoli.
Funkce input() a print() patří k nejčastěji používaným, protože umožňují provádět standardní vstupní a výstupní operace.
'''

'''
Výstupní operace pomocí funkce print()

Funkci print() používáme pro výstup dat na standardní výstupní zařízení - obrazovku.
Výchozí syntax funkce print() je:

print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)

- *objects = hodnoty, které mají být vypsány
- sep = separátor použitý mezi hodnotami; výchozí je mezera
- end = čím má být výpis ukončen; výchozí hodnota je escape sekvence "\n", tedy ukončení řádku
- file =  objekt, do něhož má být výpis proveden; výchozí hodnota je sys.stdout (standardní výstupní zařízení čili obrazovka)  
'''
# Příklad jednoduchého výpisu na obrazovku
print('Standardní výpis na obrazovku')

# Příklad výpisu proměnné
rok = 2020
print('Koronavirový rok ', rok)

# Příklad rozdílných výpisů při změně nastavení argumentů funkce print()
print(1, 2, 3, 4)
print(1, 2, 3, 4, sep=',')
print(1, 2, 3, 4, sep=';', end='!')

'''
Formátovaný výstup

Atraktivnější formátování výstupu dosáhneme pomocí metody str.format().
Tato metoda je dostupná pro jakýkoliv objekt typu string.
Složené závorky {} (braces) jsou zde používány jako zástupné symboly (placeholders), do kterých jsou vypisovány
hodnoty předané v argumentech.
'''

# Příklad formátovaného výstupu s využitím dvou proměnných x a y
x = 5; y = 10
print('Hodnota x je {} a y je {}'.format(x, y))

'''
Pořadí výpisu argumentů můžeme změnit zadáním indexů do složených závorek. 
'''

# Příklad formátovaného výstupu s využitím dvou proměnných x a y
print('Nejprve vypíši {1} slovo a teprve potom {0}'.format('první', 'druhý'))

'''
Ve formátovaném výstupním řetězci můžeme používat také pojmenované argumenty (keyword arguments).
'''

# Příklad formátovaného výstupu s využitím pojmenovaných argumentů
print('Jsem {prijmeni}, {jmeno} {prijmeni}.'.format(jmeno = 'James', prijmeni = 'Bond'))

'''
Rovněž je možné při formátování řetězců aplikovat tradiční sprintf() styl převzatý z jazyka C - tedy s využitím
operátoru "%".
'''

# Příklad formátovaného výstupu s využitím operátoru %
number = 10.1234
print('Hodnota čísla na 2 desetinná místa: %3.2f' %number)

'''
Vstup v Pythonu (input)

Pro standardní vstup z obrazovky používáme funkci input([prompt]).
[prompt] je nepovinný řetězec, výzva k zadání vstupu, která se objeví na obrazovce. 
Je třeba si uvědomit, že zadaný vstup je vždy typu string a v případě požadovaného číselného vstupu je nutné
provést konverzi pomocí funkcí int() (převádí na celé číslo) nebo float() (převádí na reálné číslo).
'''

# Příklad použití funkce input() a konverze zadaného vstupu z typu string na typ int
vek = input('Zadejte svůj věk: ')
if (int(vek) >= 18):
    print('Jste oprávněn[a] volit')
else:
    print('Bohužel ještě nemůžete volit')

'''
Funkce eval() dokáže vyhodnotit celý výraz předaný v podobě řetězce.
'''

# Příklad použití funkce input() ve spojení s funkcí eval()
vyraz = input('Zadej libovolný matematický výraz (vyjádřený pomocí operátorů známých v jazyce Python): ')
print('Výsledek vyhodnocení výrazu {1} je {0}'.format(eval(vyraz), vyraz))

"""
Cvičení 3:

Vytvořte originální aplikaci v Pythonu, v níž požádáte uživatele o různé vstupní údaje a
využijete na maximum možností výstupů do konzole. Může to být vtipný dotazník, jednoduchý znalostní test (např. 
z matematiky...), průvodce fiktivní instalací atd. Fantazii se meze nekladou a vtipnější vyhrává :-)
Aplikaci uložte do samostatného souboru myapp.py.     
"""





