# Commandes

Historique de toutes les commandes

## Init projet

- ```createsuperuser``` pour localhost/admin

## Init des modeles

- ```makemigrations```
- ```migrate```

## Apres modification du {nomapp}/settings.py

- ```makemessages --ignore venv --locale fr```
- ```makemessages --ignore venv --locale en```

- Compiler les messages de traduction modifiés dans le django.po :
- ```compilemessages --ignore .venv```
