import json
#0.Lire le fichier JSON

def read_json_file(file_path:str)->list[dict]:
    with open(file_path) as f:
        players = json.load(f)
    return players


# 1. Trier les joueurs par elo 

sorted_player = sorted(read_json_file("./data/player.json"),key=lambda d: d['elo_points'])

# 2.creation des 2 groupes

group_1 = sorted_player[0:len(sorted_player)//2]
group_2 = sorted_player[len(sorted_player)//2:len(sorted_player)]

# 3.Creation des paires / matchs

matches = []
for i in range(0,len(sorted_player)//2):
    matches.append([group_1[i],group_2[i]])


# 4.Creation d'un fichier JSON avec les matchs 

with open("./data/matches.json","w") as f:
    json.dump(matches,f,indent=4)

