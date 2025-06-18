import json
import keyboard
import time

# Загрузка JSON из файла
with open('output.json', 'r', encoding='utf-8') as file:
    data = json.load(file)



# Сохраняем в файл
with open('output.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

for user in data["users"]:
    print(user["login"])    #keyboard.write(user1["login"])
    print(user["passwd"])   #keyboard.write(user1["passwd"])
    time.sleep(1)