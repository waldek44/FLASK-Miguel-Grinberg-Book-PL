# FLASK - tworzenie aplikacji internetowych w Pythonie. 
> Tutorial treningowy na podstawie książki autorstwa Miguela Grinberga (Helion), ISBN: 978-83-283-6383-0
<hr>

### 1. INSTALACJA

Instaluję Flask
```
pip install Flask
```
<hr>

Mogę sprawdzić zainstalowane pakiety
```
pip freeze
```
U mnie to: 
> click==7.1.2  
> Flask==1.1.2  
> itsdangerous==1.1.0  
> Jinja2==2.11.2  
> MarkupSafe==1.1.1  
> Werkzeug==1.0.1  

### 2. PODSTAWOWA STRUKTURA APLIKACJI

#### INICJALIZACJA
Wszystkie aplikacje Flask muszą utworzyć **instancję aplikacji**
```
from flask import Flask
app = Flask(__name__)
```

> Przeglądarki wysyłają żądania do serwera www. Serwer www przekazuje wszystkie żądania od klientów do tego obiektu (używając protokołu WSGI).

<hr>

1. Tworzę plik **hello.py** w którym zawieram instancję
Aby zobaczyć swe dzieło na lokalu uaktywniam zmienną FLASK_APP i uruchamiam serwer
```
set FLASK_APP=hello.py
flask run
```
<hr>

#### TRASY DYNAMICZNE

1. Definiuję trasę dynamiczną w **hello.py** - po wprowadzeniu w pasku imienia pojawi się dynamicznie w szablonie.

<hr>

#### TRYB DEBUGOWANIA
Domyślnie jest wyłączony - posiada dwa moduły: reloader i debugger(pojawia się gdy przeglądarka zgłosi nieobsługiwany wyjątek).
Nigdy nie włączam go na produkcji! Aby włączyć tryb loader:  
```
set FLASK_APP=hello.py
set FLASK_DEBUG=1
flask run
```

<hr>

#### OPCJE WIERSZA POLECEŃ 
Wszystkie opcje CLI dostępne poleceniem:
```
flask
lub
flask --help
```

`flask run` - uruchamia serwer (na stronie 34 jest więcej info)  
`flask routes` - wyświetla routy aplikacji
`flask shell` - uruchamia powłokę

<hr>

#### CYKL ŻĄDANIE - ODPOWIEDŹ

> Gdy Flask otrzyma request od przeglądarki musi udostępnić kilka obiektów funkcji widoku.
> Framework flask używa kontekstów aby tymczasowo udostępniać globalnie wybrane obiekty.

Flask ma dwa konteksty:  
KONTEKST APLIKACJI (jego zmienne globalne to **g** i **current_app**)  
**g**  - obiekt który aplikacja może użyć jako pamięci tymczasowej podczas obsługi żądania. Resetowana przy każdym żądaniu.  
 **current_app** - instancja aktywnej aplikacji
 
 KONTEKST ŻĄDANIA (jego zmienne globalne to **request** i **session**)  
**request** - obiekt który hermetyzuje zawartość żądaniaHTTP od klienta  
**session** - słownik, sesja użytkownika, zapamiętywana między żądaniami

> Flask aktywuje (przekazuje) konteksty przed wysłaniem żądania do aplikacji i usuwa je po obsłużeniu żądania.

<hr>

#### PRZESYŁANIE ŻĄDANIA

Routes mogę sprawdzić w CLI (`flask routes`) ale dokładniejszy opis zawierający nazwę funkcji do której trasa kieruje uzyskam tak:
```
flask shell
from hello import app
app.url_map
```
> Flask automatycznie dodaje metody HEAD i OPTIONS do żądań a domyślnie dodatkowo GET  

Flask udostępnia obiekt żądania jako zmienną kontekstu request - ten obiek zawiera wszystkie informacje jakie klient zawarł w żądaniu HTTP

Flask dostarcza też hooki do obsłużenia kodu przed wywołaniem żądania (before_request, before_first_request, after_request, teardown_request). Opis hooków na str. 37

<hr>

#### ODPOWIEDZI
> Str. 39  
> Opis dodawania do odpowiedzi kodu statusu (domyślnie 200), oraz obiektów odpowiedzi (np. headers, set_cookie, itp...). 


