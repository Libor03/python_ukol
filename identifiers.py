'''
Klíčová slova v Pythonu (keywords)

Podobně jako v jiných programovacích jazycích jsou rovněž v Pythonu rezervována slova, která se nemohou používat
jako názvy proměnných, funkcí nebo jiné identifikátory.
V Pythonu verze 3.7 je 33 klíčových slov; tento počet se může v různých verzím mírně proměňovat.
Klíčová slova jsou v Pythonu case sensitive.
Všechna klíčová slova s výjimkou True, False a None jsou psána malými písmeny.
'''

# Výpis jednořádkového řetězce v Pythonu
print('Přehled klíčových slov v jazyce Python')

# Výpis víceřádkového řetězce v Pythonu
print('''-----------------------------------------------------------
False	    await	    else	    import	    pass
None	    break	    except	    in	        raise
True	    class	    finally	    is	        return
and	        continue	for	        lambda	    try
as	        def	        from	    nonlocal	while
assert	    del	        global	    not	        with
async	    elif	    if	        or	        yield
-----------------------------------------------------------''')

'''
Identifikátory v Pythonu (identifiers)

Identifikátory pojmenovávají entity, jako jsou třídy, funkce, proměnné, konstanty a další.

Pravidla pro zápis identifikátorů:
1. Identifikátory mohou být kombinací alfanumerických znaků a podtržítek [a-zA-Z_].
2. Identifikátory nemohou začínat numerickým znakem.
3. Jako identifikátory nemohou být použita klíčová slova.
4. Součástí identifikátorů nemohou být symboly jako např. [!@#$%] a další.
5. Identifikátory mohou mít libovolnou délku.    
'''

"""
Cvičení 1:

Identifikátory pro označení entit (proměnných nebo konstant) na následujících řádcích jsou použity zčásti
správně, ale zčásti také špatně. Oddělte zrno od plev - zakomentujte všechny špatně zadané řádky a připište do 
komentáře, proč byl identifikátor použit nesprávně. Navrhněte pod komentářem správné řešení.
"""

# import-from = 'China' - identifikátor nesmí obsahovat symbol pomlčky
import_from = 'China'

x = 0
# global = 1 - klíčové slovo
Global = 1

PI = 3.14
city = "Opava"
# hilda@sspu-opava.cz = 'Hilda Dokonalá' - zakázané znaky
Hilda_Dokonalá='hilda@sspu-opava.cz'
password2 = 'TajneHeslo'
# 007agent = 'James Bond' - začíná číslicí
agent007  = 'James Bond'

