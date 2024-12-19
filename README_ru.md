[ENG](README_eng.md)

## Для чего скрипт

Данный скрипт предназначен для получения из cloudlfare `id`,`content` и `id` записей и их удаления, при необходимости

## Как использовать

1. `git clone <repo>`
2. Создаем папку `.env` и вставляем **идентичные строки**:

`CLOUDLFARE_ZONE_ID_PROD` = его можно найти [тут](https://developers.cloudflare.com/fundamentals/setup/find-account-and-zone-ids/)

`CLOUDFLARE_API_KEY_PROD` = его можно найти [тут](https://developers.cloudflare.com/fundamentals/api/get-started/keys/)

`CLOUDFLARE_EMAIL_PROD` = его можно найти в _My Profile -> Preferences -> Email Address_

Например:

```
CLOUDFLARE_EMAIL_PROD = test@test
CLOUDFLARE_API_KEY_PROD = 1a2a33564362fs5hfhuh
CLOUDLFARE_ZONE_ID_PROD = 1a2a33564362fs
```

3. Запускаем `main.py`
   В процессе будет предложено УДАЛИТЬ записи, но этого делать необязательно, если вы хотите лишь посмотреть их список

## Возможные функции, которые будут добавлены в будущем

- Интеграция с vault для просмотра записей без ручного ввода `API_KEY` и `ZONE_ID`
- Веб-версия
