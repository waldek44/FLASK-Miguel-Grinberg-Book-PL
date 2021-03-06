# FLASK - tworzenie aplikacji internetowych w Pythonie. 
> Tutorial treningowy na podstawie książki autorstwa Miguela Grinberga (Helion), ISBN: 978-83-283-6383-0
<hr>

## 1. INSTALACJA

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

## 2. PODSTAWOWA STRUKTURA APLIKACJI

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

## 3. SZABLONY

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

<hr>

## 4. FORMULARZE INTERNETOWE

> W przypadku żądań typu POST wysyłanych w formularzu od klienta do serwera, obiekt żądania zapewnia 
> dostęp do informacji wprowadzonych przez użytkownika za pomocą pola request.form

W pracy z formularzami pomaga rozszerzenie flask-WTF (To rozszerzenie jest wrapperem integrującym pakiet WTForms z Flaskiem).  

Instaluję flask-WTF
```
pip install flask-wtf
```
flask-WTF wyjątkowo nie oczekuje inicjalizacji w aplikacji, ale oczekuje skonfigurowania SECRET_KEY. Tworzę go więc w **hello.py**  

<hr>

#### KLASY FORMULARZY
> We flask-WTF każdy formularz internetowy jest reprezentowany przez klasą (która dziedziczy po FlaskForm).  
> Klasa ta definiuje listę pól formularza. Każde pole to osobny obiekt. Lista pól na str. 59

Importuję wtf i dodaję klasę formularza w **hello.py**  

<hr>

#### RENDEROWANIE FORMULARZY

> Funkcja widoku musi przekazać do szablonu instancję klasy (NameForm u mnie) jako argument. Wtedy pola formularza po wywołaniu w szablonie renderują się do elementów HTML.

Edytuję funkcję widoku **index()** w pliku **hello.py**.  Teraz ta funkcja będzie miała dwa zadania:  
Najpierw wyrenderuje formularz, a potem obsłuży wprowadzone przez użytkownika dane.

Renderuję formularz w **templates/index.html**
 
<hr>

#### PRZEKIEROWANIA I SESJE UŻYTKOWNIKA

> Aplikacje internetowe mogą zapamiętywać dane przechodzące z jednego żądania do kolejnego, przechowując je w sesji użytkownika.
> Domyślnie sesje użytkownika są przechowywane w plikach cookie po stronie klienta.
> We Flask mam do dyspozycji globalną zmienną żądania - **session**, mogę z niej korzystać jak ze standardowego słownika w Pythonie.

<hr>

#### WYŚWIETLANIE KOMUNIKATÓW

We Flask do wyświetlania informacji i alertów używam metody **flash()**. Dla przykładu dodaję ifa który wyświetli alert
jeśli użytkownik był zalogowany w sesji pod innym imieniem. Taki flash trzeba renderować w szablonie, zmieniam **templates/base.html**
 
<hr>

## 5. BAZY DANYCH

<hr>

#### ZARZĄDZANIE BAZĄ DANYCH ZA POMOCĄ FLASK-SQLALCHEMY

Flask-SQLAlchemy to rozszerzenie które ułatwia pracę z frameworkiem ORM SQLAlchemy, które warto zainstalować:
```
pip install flask-sqlalchemy
```

> We Flask-SQLAlchemy baza danych jest podawana jako adres URL (mysql to użytkownik://użytkownik:hasło@localhost/nazwa_bazy)
> i zapisujemy ją w zmiennej SQLALCHEMY_DATABASE_URI

Inicjalizuję i konfiguruję bazę danych w **hello.py**

<hr>

#### DEFINICJA MODELU
> Model to klasa Pythona z atrybutami odpowiadającymi kolumnom przypisanej mu tabeli bazy danych.  
> Na str. 75 są najpopularniejsze typy kolumn w SQLAlchemy

W **hello.py** definiuję modele **Role** i **User**

<hr>

#### OPERACJE NA BAZACH DANYCH
Modele mam już skonfigurowane, można ich używać. Dobrą metodą wypróbowania modeli jest skorzystanie z powłoki Pythona:  
```
set FLASK_APP=hello.py
flask shell
from hello import db
db.create_all()
``` 
 Polecenie **db.create_all()** tworzy nowy plik bazy danych.
 
 Wstawianie przykładowych wierszy:
 ```
from hello import Role, User
admin_role = Role(name='Admin')
mod_role = Role(name='Moderator')
user_role = Role(name='User')
user_john = User(username='Jan', role='admin_role')
user_suzan = User(username='Zuzia', role='user_role')
user_david = User(username='Dawid', role='user_role')
```

<hr>

#### BAZA DANYCH W FUNKCJACH WIDOKU
Edytuję widok index w hello.py aby dodawał dane z formularza do db. Edytuję też **templates/index.html**

<hr>

#### KONFIGURACJA INTEGRACJI Z POWŁOKĄ PYTHONA
Aby nie importować instancji aplikacji do powłoki shell za każdym razem muszę utworzyć procesor kontekstu powłoki 
i zarejestrować go za pomocą dekoratora **@app.shell_context_processor** w **hello.py** 

<hr>

#### MIGROWANIE BAZ DANYCH | PAKIET FLASK-MIGRATE
Aby aktualizować tabele db po zmianach dokonanych w modelach używam frameworka migracji flask-migrate.  
```
pip install flask-migrate
```
Inicjuję pakiet w **hello.py** 

Inicjuję też pakiet w aplikacji za pomocą CLI:
```
flask db init
```
To polecenie utworzy katalog migracji. Następnie wysyłam migracje ze skryptów:
```
flask db migrate
flask db upgrade
```

 
<hr>

## 6. WIADOMOŚCI EMAIL
> Wysyłanie wiadomości email z aplikacji za pomocą standardowej biblioteki Pythona **smtplib** ułatwia pakiet **Flask-Mail**  
> Rozszerzenie to łączy się z serwerem SMTP i przesyła do niego wiadomość, po czym serwer dostarcza ją do adresata. 
> Klucze konfiguracyjne na str. 87 

```
pip install flask-mail
```

Konfiguruję wysyłanie maila w **hello.py** 

<hr>

#### WYSYŁANIE WIADOMOŚCI E-MAIL Z POWŁOKI PYTHONA

Aby przetestować konfigurację:
```
set FLASK_APP=hello.py
set MAIL_USERNAME=<gmail username>
set MAIL_PASSWORD=<gmail password>

flask shell
from flask_mail import Message
from hello import mail
msg = Message('Testowy mail', sender='toja@aplikacja.com', recipients=['toja@aplikacja.com'])
msg.body = 'To jest tekst'
msg.html = 'To jest treść w <b>HTML</b>.'
with app.app_context():
    mail.send(msg)

```

<hr>

#### INTEGROWANIE WIADOMOŚCI E-MAIL Z APLIKACJĄ

Wyodrębniam elementy operacji wysyłania e-mail do osobnej funkcji w **hello.py**, rozbudowuję funkcję indextak aby wysłała maila do
administratora za każdym razem gdy pojawi się nowy user. Szczegóły na str.89 i 90  
Tworzę **templates/mail/new_user.html** i **templates/mail/new_user.txt**.  

Następnie muszę w terminalu utworzyć zmienną FLASKY_ADMIN
```
set FLASKY_ADMIN=mymail@gmail.com
```

<hr>

#### ASYNCHRONICZNE WYSYŁANIE E-MAIL

> Wiele rozszerzeń Flaska ma problem ponieważ wymagają aktywnego kontekstu aplikacji lub żądań do działania. Niestety konteksty 
> mogą być powiązane z innym wątkiem, dlatego warto czasem utworzyć kontekst aplikacji za pomocą funkcji **app.app_context()**. 
>Instancja app jest wtedy przekazywana do wątku jako argument, aby można w nim było utworzyć kontekst.

Używam funkcji **send_async_email()** aby uniknąć opóźnień w wysyłaniu.

<hr>

## 7. STRUKTURA DUŻEJ APLIKACJI

1. Tworzę **config.py** i przenoszę tam logikę konfiguracji z pliku **hello.py**  

<hr>

#### PAKIET APLIKACJI 

> Pakiet aplikacji to miejsce w którym znajdują się wszystkie szablony, pliki statyczne i kody.

Tworzę katalog **app**  i przenoszę do niego **templates** i **static**

<hr>

#### KORZYSTANIE Z FABRYKI APLIKACJI
Tworzę konstruktor pakietu app - **__init__.py**, a w nim funkcję wytwórczą aplikacji **create_app()** - daje mi to możliwość
tworzenia wielu instancji aplikacji, oraz ułatwia testy.
> ten konstruktor importuje większość moich rozszerzeń, tworzy je niezainicjowane. 

<hr>

#### IMPLEMENTACJA FUNKCJI APLIKACJI W PROJEKCIE
> Schemat (Blueprint) jest podobny do aplikacji. Różnica polega na tym, że pozostaje w stanie uśpienia dopóki schemat nie zostanie zarejestrowany w aplikacji.
> Schematy powstają przez utworzenie obiektu Blueprint('nazwa projektu', pakiet w którym znajduje się schemat (zazwyczaj __name__) )

1. W pakiecie **app** tworzę podpakiet **app/main** przeznaczony do obsługi pierwszego schematu (Blueprint) aplikacji.  
2. W **app/main** tworzę konstruktor tworzący schemat **app/main/__init__.py**
3. Tworzę plik zawierający trasy aplikacji **app/main/views.py**
4. Tworzę plik zawierający procedury obsługi błędów **app/main/errors.py**
5. Rejestruję Schemat Blueprint w w funkcji tworzącej aplikację wewnątrz **app/__init__.py**
6. Tworzę plik zawierający formularze **app/main/forms.py**
7. Tworzę moduł **flaksy.py** w katalogu najwyższego poziomu gdzie definiuję instancję aplikacji.
8. Głównym skryptem aplikacji nie jest już **hello.py** lecz **flaksy.py** dlatego muszę zaktualizować zmienne środowiska:
```
set FLASK_APP=flasky.py
set FLASK_DEBUG=1
```
9. Tworzę plik zależności:
```
pip freeze >requirements.txt
```
> Jeśli będę musiał zbudować to środowisko na nowym komputerze, wystarczy komenda `pip install -r requirements.txt`

10. Definiuję testy jednostkowe w pliku **tests/test_basics.py** i dodaję też **tests/__init__.py**
11. Tworzę plik **app/models.py**
12. Migruję:
```
flask db migrate
flask db upgrade
```
13. Dodaję pakiet mailowy **app/email.py**

