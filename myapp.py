import time

utrpeni = input('Zadejte, jak dlouho vám trvalo, než se vám podařilo zprovoznit Python interpreter? '
                '(prosím, zadejte v hodinách): ')
if (int(utrpeni) == 3):
    print('Gratuluji, trvalo vám to stejně dlouho jako mně!')
elif (int(utrpeni) < 3):
    print('A to jsi jako jak udělal? ')
else:
    print('Tak to tě lituji, že ti to trvalo déle jak mně')

cislicko = input('Každopádně, pokud tento dotazník děláš, určitě se ti podařilo interpreter zprovoznit '
                 'pověz mi, kolik otázek očekáváš v tomto dotazníku?')

if (int(cislicko) >=6):
    print('Ses zbláznil? Už teď nestíhám dělat úkoly, natož vymýšlet tolik otázek, dám ti nápovědu, '
          'bude jich o něco méně :)')
elif (int(cislicko) == 2):
    print('Vážně si myslíš, že tady končím?! Za koho mě máš? I když jak to říkáš, zní to docela lákavě... To ale není '
          'dostačující!')

elif (int(cislicko) ==1):
    print('Ptal jsem se tě na počet otázek v tomto dotazníku, ne na tvoje IQ, již toto byla 2. otázka,'
          ' jak sis mohl myslet, když už čteš 2. otázku, že v tomto dotazníku je jenom 1? ￣へ￣')
else:
    print("Sám nevím, kolik tady bude otázek když to píši, ale tvůj návrh nezní špatně!")

print("No já už musím běžet, chci se najíst, počkáš na mě chvilinku?")
print("Libor has left the chat")
time.sleep(3)
print("")
print("s8tn666 has entered the chat")
s8tn= input("Á, co to tady vidím? že by nějaký smrtelník, který se nechal nachytat a dostal se do tohoto prokletého dotazníku!"
      " Jediné, co tě drželo naživu byla přítomnost toho, co právě odešel. Nyní již mě nic nebrání tomu abych udělal to,"
      "po čem jsem toužil tak strašně dlouho, pověz mi, kolik podobných dotazníků jsu již prošel?")

if(int(s8tn) <=1):
    print("Takže jsem první? to je dobře, Velmi dobře")
else:
    print("No to se dalo asi očekávat, kdo byl předemnou? Ten který se nazývá Proherceslav? Kušáš Pomalý?")
print("Musím končit, ale já se vrátím!")
print("s8tn666 has left the chat")
time.sleep(.800)
print("Libor has entered the chat")
print("už jsem zpátky, promiň za to, snad se tu nic divného nedělo, každopádně jsem usoudil, že by "
      "už měla stačit jenom jedna otázka")
while True:
    print("")
    znamka = input("kdyby jste toto známkoval, jakou známku by jste mi dal?")


    if (int(znamka) ==1):
        print("Vážně? Děkuji, doufal jsem v 1, ale nebyl jsem si jistý, jestli je to dostačující")
        break
    elif(int(znamka) >=6):
        print("Takovou známku ani dostat nemůžu")
    else:
        print("ale s tímto já nesouhlasím, co to zkusit znovu")

