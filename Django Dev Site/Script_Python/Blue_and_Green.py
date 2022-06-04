##import sys

#file_sucess = open('log_saida_normal.txt', 'w', encoding='utf-8')
#file_err = open('log_saidaa_err.txt', 'w', encoding='utf-8' )

#sys.stdout = file_sucess
#sys.stdout = file_err



programa = 'Blue and Green Djins Loot Calculator v0.10'
print('#'*50)
print(f'{programa:^50}')
print('#'*50)

##Listas de itens a serem computados
alesar = ['Ancient Shield', 0.9, 'Black Shield', 0.8,'Bonebreaker', 10,'Dragon Hammer', 2,'Dreaded Cleaver', 15,'Giant Sword', 17,'Haunted Blade', 8,'Knight Armor', 5,'Knight Axe', 2,'Knight Legs', 5,'Onyx Flail', 22,'Ornamented Axe', 20,'Serpent Sword', 0.9,'Skull Staff', 6,'Titan Axe', 4,'Tower Shield', 8,'Vampire Shield', 15,'Warrior Helmet', 5]
yaman = ['Glacial Rod', 6.5,'Hailstorm Rod', 3,'Moonlight Rod', 0.2,'Muck Rod', 6,'Necrotic Rod', 1,'Northwind Rod', 1.5,'Springsprout Rod', 3.6,'Terra Rod', 2,'Underworld Rod', 4.4]
nahbob = ['Angelic Axe', 5,'Blue Robe', 10,'Bonelord Shield', 1.2,'Boots of Haste', 30,'Broadsword', 0.5,"Butcher's Axe", 18,'Crown Armor', 12,'Crown Helmet', 2.5,'Crown Legs', 12,'Crown Shield', 8,'Crusader Helmet', 6,'Dragon Lance',	9,'Dragon Shield',	4,'Fire Axe', 8,'Fire Sword',	4,'Glorious Axe', 3,'Guardian Shield', 2,'Ice Rapier',	1,'Obsidian Lance', 0.5,'Phoenix Shield', 16,"Queen's Sceptre", 20,'Royal Helmet', 30,'Shadow Sceptre', 10,'Spike Sword', 1,'Thaian Sword', 16,'War Hammer', 1.2]
haroun = ['Orb', 0.75,'Wand of Cosmic Energy', 2,'Wand of Decay', 1,'Wand of Defiance', 6,'Wand of Draconia', 1,'Wand of Dragonbreath', 0.2,'Wand of Everblazing', 6,'Wand of Inferno', 3,'Wand of Starstorm', 3.6,'Wand of Voodoo', 4.4,'Wand of Vortex', 0.1]

alesar1 =len(alesar)
yaman1 = len(yaman)
nahbob1 = len(nahbob)
haroun1 = len(haroun)

###Variáveis que acumulam a soma dos itens
somaA = 0
somaY = 0
somaN = 0
somaH = 0

###Interação com o Usuário
opções = ['GREEN','BLUE']
resposta = str(input('Qual djin você quer calcular? digite "GREEN" ou "BLUE". ')).upper()

while resposta not in opções:
    print ('Comando inválido tente "Green" ou "Blue". ')
    resposta = str(input('Qual djin você quer calcular? digite "GREEN" ou "BLUE". ')).upper()
    
if resposta == 'GREEN':
    for c in range(0,alesar1,2):
        qtd = int(input(f'Digite a quantidade de {alesar[c]}:   '))
        somaA += alesar[c+1] * qtd
        print (f'--------------------------------------------->{alesar[c+1] * qtd:.3f}k')

    for c in range (0,yaman1,2):
        qtd = int(input(f'Digite a qtd de {yaman[c]}:   '))
        somaY += yaman[c+1] * qtd
        print (f'--------------------------------------------->{yaman[c+1] * qtd:.3f}k')
    print (f'O Total de loot GREEN ALESAR foi de: {somaA:.3f}k.   ')   
    print (f'O Total de loot GREEN YAMAN foi de: {somaY:.3f}k.   ')   
    print (f'O Total ALESAR e YAMAN foi de {somaA + somaY:.3f}k')

elif resposta == 'BLUE':
    for c in range (0, nahbob1,2):
        qtd = int(input(f'Digite a quantidade de {nahbob[c]}:   '))
        somaN += nahbob[c+1] * qtd
        print (f'--------------------------------------------->{nahbob[c+1] * qtd:.3f}k')
    for c in range (0, haroun1,2):
        qtd = int(input(f'Digite a quantidade de {haroun[c]}:   '))
        somaH += haroun[c+1] * qtd
        print (f'--------------------------------------------->{haroun[c+1] * qtd:.3f}k')
    print (f'O Total de loot BLUE NAHBOB foi de: {somaN:.3f}k.   ')   
    print (f'O Total de loot BLUE HAROUN foi de: {somaH:.3f}k.   ')   
    print (f'O Total NAHBOB e HAROUN foi de {somaN + somaH:.3f}k')

print()
print('#'*50)
print(f'{programa:^50}')
print('#'*50)

### Fim do programa
quit = input()
