# Biblioteka
              
## Badges

[![Python License](https://img.shields.io/badge/Python-License-green.svg)](https://pl.python.org/forum/index.php?topic=803.0;wap2)
## O aplikacji


Aplikacja webowa pozwala nam na tworzenie użytkowników, 
którzy po zalogowaniu mogą wypożyczać książki, wcześniej dodane przez administratorów. 
Aplikacja pozwala na dodawanie wszelkiego rodzaju publikacji takich jak: książki, broszury, gazety, 
czasopisma i inne wydawnictwa ciągłe, druki ulotne, afisze.

![Logo](https://miro.medium.com/max/1200/1*slHeZngyeUr7ypEz7MNL5w.png)


## Uruchamianie

Aby uruchomić aplikację, musimy pobrać środowisko python 3.11.1 z oficjalnym 
oraz domyślnym system zarządzania pakietami pip.
 Następnie musimy wykonać w CMD następujące komendy: 
 - pip install django
 - pip install djangorestframework
 - pip install django-cors-headers
 - pip install djangorestframework-simplejwt
 - python manage.py makemigrations
 - python manage.py migrate
 - python manage.py runserver

## License

Python License


## Authors

- [@Hubert Łebkowski](https://github.com/lebkowskih)
- [@Jakub Pawiński](https://github.com/JakubPawi)


## Architektura systemu

#### Stos technologiczny - architektura rozwojowa
- Visual Studio Code (IDE)
- SQLite

#### Stos technologiczny - architektura uruchomieniowa
- Python
- Django
- Git


## Wymagania

#### Wymagania funkcjonalne

Każdy może stworzyć nowego użytkownika, 
który będzie miał możliwość przeglądania kategori i autorów punlikacji oraz możliwość 
wypożyczenia książek lub innych rodzaju publikacji. 


#### Wymagania niefunkcjonalne

- dostępność/niezawodność - aplikacja jest dostępna cały czas
- wydajność - aplikacja w szybki sposób reaguje na czynności użytkownika
- użyteczność - wszystkie zmiany, są zapisywane w bazie danych
