import json
import pdb
data = json.loads(open('inventory-lnfasto.json').read())

iv = 0
PoId = {}
PoCp = {}
PoStam = {}
PoAtt = {}
PoDef = {}
PoIv = {}

for numb in data:
        pokemon = []
        
        try:
            #pdb.set_trace()
            stam = numb['inventory_item_data']['pokemon_data']['individual_stamina']
            att = numb['inventory_item_data']['pokemon_data']['individual_attack']
            defense = float(numb['inventory_item_data']['pokemon_data']['individual_defense'])
            iv = round((stam + att + defense) / 45, 2)
            PoId['id = '] = [(numb['inventory_item_data']['pokemon_data']['pokemon_id'])]
            PoCp['cp = '] = [(numb['inventory_item_data']['pokemon_data']['cp'])]
            PoStam['stamina = '] = [(numb['inventory_item_data']['pokemon_data']['individual_stamina'])]
            PoAtt['attack = '] = [(numb['inventory_item_data']['pokemon_data']['individual_attack'])]
            PoDef['defense = '] = [(numb['inventory_item_data']['pokemon_data']['individual_defense'])]
            PoIv['iv = '] = [iv]
            pokemon.append(PoId)
            pokemon.append(PoCp)
            pokemon.append(PoIv)
            pokemon.append(PoStam)
            pokemon.append(PoAtt)
            pokemon.append(PoDef)
            print pokemon
        except:
                KeyError           



