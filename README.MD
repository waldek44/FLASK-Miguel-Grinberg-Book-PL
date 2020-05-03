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

<hr>

### 3. SZABLONY

Rozdzielam logikę biznesową od logiki prezentacji. Domyślnie Flask szuka szablonów html w podkatalogu templates

<hr>

Tworzę: katalog **templates** oraz pliki  **templates/index.html** i **templates/user.html**

<hr>

Modyfikuję funkcję widoku w **hello.py**

<hr>

#### ZMIENNE

Jinja 2 rozpoznaje zmienne dowolnego typu, np:  
```
<p>Słownik: {{ mydict['key'] }}  </p>
<p>Lista: {{ mylist[3] }}  </p>
<p>Lista ze zmiennym indeksem: {{ mylist[myintvar] }}  </p>
<p>Wartość z metody obiektu: {{ myobject.somemethod() }}  </p>
```

Zmienne można modyfikować filtrami:
```
<p> {{ name|save }} </p>           // renderuje wartość bez interpretowania znaków modyfikacji 
<p> {{ name|capitalize }} </p>     // renderuje pierwszy znak na dużą literę
<p> {{ name|lower }} </p>          // zmienia tekst na małe litery
<p> {{ name|upper }} </p>          // zmienia tekst na duże litery
<p> {{ name|title }} </p>          // Pierwsza litera każdego słowa jest duża
<p> {{ name|trim }} </p>           // usuwa początkowe i końcowe białe znaki
<p> {{ name|striptags }} </p>      // usuwa znaczniki html
```

<hr>

#### BOOTSTRAP

Instaluję rozszerzenie do integracji z bootstrap
```
pip install flask-bootstrap
```

<hr>

Inicjalizuję to rozszerzenie w pliku **hello.py**

<hr>

Rozszerzenie flask-bootstrap posiada już własne szablony bazowe w venv i mogę je dziedziczyć, tworzę własny **templates/base.html** 
i w nim dziedziczę po **bootstrap/base.html**. Edytuję też **templates/user.html** .


<hr>
 
Dodaję też obsługę wyjątków 404 i 500. Tworzę **templates/404.html** i **templates/500.html** oraz tworzę do nich widoki w **hello.py**

<hr>

#### PLIKI STATYCZNE

Flask domyślnie szuka plików statycznych w podkatalogu static. Tworzę podkatalog **static**. Dodaję favicon.

<hr>

#### DATA I CZAS - MOMENT.JS
Biblioteka Moment.js pozwala na pracę w Flask w UTC a potem konwertowanie czasu na lokalny po stronie klienta (przez przeglądarkę).  
Instaluję rozszerzenie do pracy z Moment.js
```
pip install flask-moment
```

<hr>

Inicjuję te rozszerzenie w instancji **hello.py**

<hr>

Dodaję bibliotekę w **bootstrap/base.html**

<hr>

Importuję zmienną datetime i dodaję ją do funkcji index w **hello.py**

<hr>

Renderuję zmienną current_time z widoku w szablonie **bootstrap/index.html**
