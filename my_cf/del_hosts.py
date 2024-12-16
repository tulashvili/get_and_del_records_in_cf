import requests
from dotenv import load_dotenv
import get_hosts_my_cf


for record in get_hosts_my_cf.dns_records:
    delete_url = f"https://api.cloudflare.com/client/v4/zones/{get_hosts_my_cf.datshost_zone_id}/dns_records/{record['id']}"
    
    del_response = requests.delete(delete_url, headers=get_hosts_my_cf.headers)
    
    if del_response.status_code == 200:
        print(f"Удалено: {record['name']} ({record['content']})")
    else:
        print(f"Ошибка удаления записи {record['name']}: {del_response.status_code}, {del_response.text}")