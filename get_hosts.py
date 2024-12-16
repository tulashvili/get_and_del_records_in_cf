import requests
import json
import os
from dotenv import load_dotenv

# Загружаем переменные окружения
load_dotenv()

datshost_zone_id = os.getenv("CLOUDFLARE_MY_INFRA_ZONE_ID")

# URL и заголовки
url = f"https://api.cloudflare.com/client/v4/zones/{datshost_zone_id}/dns_records"
headers = {
    "Content-Type": "application/json",
    "X-Auth-Email": os.getenv("CLOUDFLARE_EMAIL_MY_INFRA"),
    "X-Auth-Key": os.getenv("CLOUDFLARE_API_KEY_MY_INFRA")
}

# Параметры для пагинации
page = 1
per_page = 50  # Количество записей на странице

while True:
    # Формируем URL с пагинацией
    paginated_url = f"{url}?page={page}&per_page={per_page}"

    # Выполняем запрос к API
    response = requests.get(paginated_url, headers=headers)

    if response.status_code == 200:
        data = response.json()  # Разбираем ответ JSON
        for hosts in data["result"]:
            if "switcherry" in hosts["name"] and "vpn" in hosts["name"] and not "blog" in hosts["name"]:
                print(f'{{ name = "{hosts["name"]}", value = "{hosts["content"]}" }},')
            # print(hosts)

        # Проверяем, есть ли следующая страница
        result_info = data.get("result_info", {})
        if "total_pages" in result_info and page < result_info["total_pages"]:
            page += 1  # Переходим к следующей странице
        else:
            break  # Нет следующей страницы, выходим из цикла
    else:
        print(f"Ошибка: {response.status_code}, {response.text}")
        break
