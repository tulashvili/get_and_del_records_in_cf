import os
from dotenv import load_dotenv

load_dotenv()

print("Рабочая инфра email " + os.getenv("CLOUDFLARE_EMAIL_PROD"))
print("Рабочий api key " + os.getenv("CLOUDFLARE_API_KEY_PROD"))
print("------------")
print("Моя инфра api " + os.getenv("CLOUDFLARE_API_KEY_MY_INFRA"))
print("Моя инфра email " + os.getenv("CLOUDFLARE_EMAIL_MY_INFRA"))