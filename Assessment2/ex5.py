import json

with open('ex5.json', 'r') as file:
    ex5 = json.load(file)

for item in ex5:
    if item['name'] == 'Old Fashioned':
        item['batters']['batter'].append({'id': '1005', 'type': 'Tea'})

with open('ex5.json', 'w') as file:
    json.dump(ex5, file, indent=4)

print("JSON file updated successfully!")
