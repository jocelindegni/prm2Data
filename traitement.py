departement_communes = open(
    './resources/A-traiter.xlsx_Feuil1.csv',
    'r', encoding='utf8')
adjectifsFR = open('./resources/adjectifsFR.txt', encoding='utf8')
adjectifsEN = open('./resources/adjectifsEN.txt', encoding='utf8')
adjectifsAll = open('./resources/Adj-all.csv', encoding='utf8')
adjectifsEs = open('./resources/espagnol.txt')
additionalAdjectif = open('./resources/prefixe.csv')
adjectifsItalien = open('./resources/italian.txt')

adjectifsList = []

for adj in additionalAdjectif:
    indexRetour = adj.find('\n')
    adjectifsList.append(adj[0:indexRetour].lower())

for adj in adjectifsFR:
    indexRetour = adj.find('\n')
    adjectifsList.append(adj[0:indexRetour].lower())# retirer le caractere '\n'
#print(adjectifsList)
for adj in adjectifsEN:
    indexRetour = adj.find('\n')
    adjectifsList.append(adj[0:indexRetour].lower())

for adj in adjectifsAll:
    indexRetour = adj.find('\n')
    adjectifsList.append(adj[0:indexRetour].lower())

for adj in adjectifsEs :
    indexRetour = adj.find('\n')
    adj = adj[0:indexRetour]
    adList = adj.split('-')
    adList[0].strip()
    adjectifsList.append( adList[0].lower())

nbreOc=0
nbreOil=0

def traitement():
    # Liste des departements et communes avec la geolocalisation
    oilOcFile = open('./resources/result.csv', 'w', encoding='utf8')
    i = 0
    for line in departement_communes:
        if i == 0: # ligne du header
            i += 1
            continue
        # Nom commune placé à la 9em position
        value = oilOc(line.split(";")[6].lower())
        indexRetour = line.find('\n')
        oilOcFile.write(line[0:indexRetour] + ';' + str(value) + '\n')


# Retourne 1 si oil ou -1 si oc sinon 0
def oilOc(nomCommune):
    global  nbreOil
    global nbreOc
    # On compte les nombre d'occurence pour oil et oc (le nombre d'adjectif)
    value = 0
    for adj in adjectifsList:
        index = nomCommune.find(adj)
        if index > 0:  # adjectif trouvé au milieu du mot
            nbreOc += 1
            value = -1
            break
        elif index == 0 and len(adj) != len(nomCommune):
            value = 1
            nbreOil += 1
            break

    return value

traitement()
print (str(nbreOil) + " "+str(nbreOc))
#print(adjectifsList)