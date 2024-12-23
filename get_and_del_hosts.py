import requests
import os
from dotenv import load_dotenv
import re

# load env var
load_dotenv()

# input words and split them to list
regex_pattern = input("Введите слова для поиска в имени хоста (разделяйте пробелами): ").strip()
search_words = regex_pattern.split()

datshost_zone_id = os.getenv("CLOUDLFARE_ZONE_ID_PROD")

# URL and headers
url = f"https://api.cloudflare.com/client/v4/zones/{datshost_zone_id}/dns_records"
headers = {
    "Content-Type": "application/json",
    "X-Auth-Email": os.getenv("CLOUDFLARE_EMAIL_PROD"),
    "X-Auth-Key": os.getenv("CLOUDFLARE_API_KEY_PROD")
}

def check_records(search_words):
    # param for pagination
    page = 1
    per_page = 50  # records on the page
    dns_records = []  # storage list for dns-records 

    while True:
        # make url with pagination
        paginated_url = f"{url}?page={page}&per_page={per_page}"

        # get request to API
        response = requests.get(paginated_url, headers=headers)

        if response.status_code == 200:
            data = response.json()  # parse json response
            for record in data["result"]:
                # filter result by words
                if all(word.lower() in record["name"].lower() for word in search_words):
                    dns_records.append({
                        "id": record["id"],
                        "name": record["name"],
                        "content": record["content"]
                    })
            # format output for paste in terraform
            for record in dns_records:
                print(f'{{ name = "{record["name"]}", value = "{record["content"]}", id = "{record["id"]}" }}')

            # check next page
            result_info = data.get("result_info", {})
            if "total_pages" in result_info and page < result_info["total_pages"]:
                page += 1  # move to next page
            else:
                break  # if next page is not, cycle is breaking
        else:
            print(f"Ошибка: {response.status_code}, {response.text}")
            break
    
    return dns_records

def del_records(dns_records):
    for record in dns_records:
        delete_url = f"https://api.cloudflare.com/client/v4/zones/{datshost_zone_id}/dns_records/{record['id']}"
        
        del_response = requests.delete(delete_url, headers=headers)
        
        if del_response.status_code == 200:
            print(f"Удалено: {record['name']} ({record['content']})")
        else:
            print(f"Ошибка удаления записи {record['name']}: {del_response.status_code}, {del_response.text}")