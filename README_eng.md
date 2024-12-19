[RU](README_ru.md)

## What the script is for

This script is used to get from cloudlfare `id`, `content` and `id` records and delete them, if necessary.

## How to use

1. `git clone <repo>`.
2. Create a `.env` folder and insert **identical lines**:

`CLOUDLFARE_ZONE_ID_PROD` = it can be found [here](https://developers.cloudflare.com/fundamentals/setup/find-account-and-zone-ids/)

`CLOUDFLARE_API_KEY_PROD` = it can be found [here](https://developers.cloudflare.com/fundamentals/api/get-started/keys/)

`CLOUDFLARE_EMAIL_PROD` = it can be found in _My Profile -> Preferences -> Email Address_.

For example:

```
CLOUDFLARE_EMAIL_PROD = test@test
CLOUDFLARE_API_KEY_PROD = 1a2a33564362fs5hfhuh
CLOUDLFARE_ZONE_ID_PROD = 1a2a33564362fs
```

3. Run `main.py`.
   In the process, you will be prompted to DELETE the entries, but you don't have to do that if you just want to see a list of them

## Possible features to be added in the future

- Integration with vault to view records without manually entering `API_KEY` and `ZONE_ID`.
- Web version

Translated with DeepL.com (free version)
