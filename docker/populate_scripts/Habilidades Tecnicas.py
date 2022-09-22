import json

skills=[
    'Traqueostomía',
    'Gastrostomía',
    'Sondeo vesical',
    'Sonda Foley',
    'Colostomía',
    'Cistostomía',
    'Estimulación anal',
    'Inyecciones intramusculares',
    'Sonda nasogástrica',
    'Manejo de parapléjicos/postrados',
    'Uso de tecle',
    'Equipo SARS para daño medular',
    'Transferencia',
]

habilidades=[]


for i in range(len(skills)):

    habilidades.append(
            {
                "model": "technical_skills.technicalSkill",
                "pk": i,
                "fields": {
                    "name": skills[i],
                }
            }
        )

json_data = json.dumps(habilidades, ensure_ascii=False)
print(json_data)
f2 = open("habilidades.json", "w", encoding="utf-8")
f2.write(json_data)
f2.close()