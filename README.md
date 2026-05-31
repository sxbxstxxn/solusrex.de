# solusrex.de

Kleine Django-Seite fuer solusrex.de. Das urspruengliche statische Design wurde als Django-Template uebernommen.

## Lokal starten

```powershell
python -m venv .venv
.\.venv\Scripts\pip install -r requirements.txt
.\.venv\Scripts\python manage.py migrate
.\.venv\Scripts\python manage.py runserver
```

Die Seite ist danach unter http://127.0.0.1:8000 erreichbar.

## Mit Docker starten

```powershell
docker compose up --build
```

Die Seite ist danach unter http://localhost:8000 erreichbar.

## Wichtige Umgebungsvariablen

- `DJANGO_SECRET_KEY`: Secret Key fuer Django
- `DJANGO_DEBUG`: `True` fuer lokale Entwicklung, sonst `False`
- `DJANGO_ALLOWED_HOSTS`: Kommagetrennte Liste erlaubter Hosts
