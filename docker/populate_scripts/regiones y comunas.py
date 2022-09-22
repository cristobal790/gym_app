import json

f = open('comunas.json', encoding="utf-8")

data = json.load(f)
print(data)
comunas_fields = ['name']

ans_regiones = []
ans_comunas = []
c1 = 1
c2 = 1
for r in data['regions']:
    region_name = r["name"]

    ans_regiones.append(
        {
            "model": "locations.region",
            "pk": c1,
            "fields": {
                "name": region_name,
            }
        }
    )



    comunas = r["communes"]
    for com in comunas:
        ans_comunas.append(
            {
                "model": "locations.comuna",
                "pk": c2,
                "fields": {
                    "name": com["name"],
                    "region_id": c1
                }
            }
        )
        c2 += 1


    c1 += 1



print(ans_comunas)

json_data = json.dumps(ans_regiones+ans_comunas, ensure_ascii=False)
print(json_data)
f2 = open("regiones.json", "w", encoding="utf-8")
f2.write(json_data)
f2.close()


#comunas
