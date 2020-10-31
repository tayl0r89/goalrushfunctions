import sys
from google.cloud import firestore

if len(sys.argv) < 2:
    print("Must provide an input file of teams.")
    exit()

file = sys.argv[1]
print(file)
teams = []
with open(file, 'r') as team_file:
    for line in team_file:
        teamParts = line.split(",")
        team = {}
        team['id'] = teamParts[0]
        team['name'] = teamParts[1]
        if len(teamParts) > 2:
            aliases = []
            for i in range(2, len(teamParts)):
                if len(teamParts[i].strip()) > 0:
                    aliases.append(teamParts[i].strip())
            team['aliases'] = aliases
        teams.append(team)

db = firestore.Client()

batch = db.batch()
for team in teams:
    ref = db.collection("teams").document(team['name'])
    batch.set(ref, team)

batch.commit()
