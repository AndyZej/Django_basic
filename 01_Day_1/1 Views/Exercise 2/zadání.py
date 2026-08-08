Cvičení 2 – konfigurace projektu
Použijte nástroj manage.py k vytvoření nové aplikace django_1,
přidejte aplikaci exercises_app do souboru settings.py,
nainstalujte ovladač PostgreSQL:
Pomocí nástroje PIP nainstalujte balíček psycopg2-binary.
Konfigurujte Django pro práci s databází PostgreSQL:
Nastavte databázi a zahrňte ji do projektu, pojmenujte ji exercises,
ve souboru settings.py najděte položku DATABASES a změňte ji tak, aby pracovala s vaší databází:

DATABASES = {
    'default': {
        'NAME': '<here enter database name>',
        'ENGINE': 'django.db.backends.postgresql',
        'USER': '<here enter the name of database user>',
        'PASSWORD': '<here enter the password for the database>',
        'HOST': '127.0.0.1'
    }
}

Proveďte první migraci,
spusťte vývojový server a zkontrolujte, zda funguje.
Změnila se domovská stránka projektu? Jak?