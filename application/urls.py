from django.urls import path

from . import views

app_name = 'application'
urlpatterns = [

    # ekran startowy
    path('', views.index, name='index'),

    # lista wszystkich ER
    # niezalogowani widzą tylko listę
    # zalogowani mogą zaznaczać i odznaczać, w których pokojach byli
    # przy każdym widać: kwadracik do zaznaczania, ew. ikonkę (zdjęcie), nazwę ER, nazwę firmy, miasto, ew. adres, ew. krótki opis
    path('escaperoomy/', views.escaperooms, name = 'escaperooms'),
    
    # lista wszystkich użytkowników
    path('uzytkownicy/', views.users, name = 'users'),

    # znajomi gracze (można przeglądać, dodawać i usuwać ze znajomych)
    path('znajomi/', views.buddies, name = 'buddies'),

    # historia odwiedzin
    # dotychczasowe wyjścia ze znajomymi (widać, w jakich pokojach się było i z kim)
    path('historia/', views.history, name = 'history'),

    #planowane wyjścia (zarówno te, które mają już decyzję, jak i te, które jeszcze czekają na decyzję)
    path('planowane/', views.planned, name = 'planned'),

    # ekran rejestracji użytkownika
    path('rejestracja/', views.registration, name = 'registration'),

    # ekran logowania użytkownika
    path('logowanie/', views.login, name = 'login'),

    # ekran logowania użytkownika
    path('wylogowanie/', views.logout, name = 'logout'),

    # edycja istniejącego wyjścia (zapraszanie znajomych, wybór ER)
    path('wyjscie/<int:goingout_id>/', views.goingOut, name ='goingout'),

    # tworzenie nowego wyjścia (przekierowanie do edycji wyjścia)
    path('newgoingout/', views.newGoingOut, name ='newgoingout'),

    # profil użytkownika (dowolnego)
    path('profil/<int:user_id>/', views.profile, name ='profile'),
]




''' POMYSŁY

W MIARĘ REALNE
- ranking pokojów, do których chce się pójść (po widoku 'pasujace' każdy by głosował na kilka swoich ulubionych pokojów z listy)
- godziny otwarcia escape roomów + każdy uczestnik by dodatkowo określał, w jakich godzinach i dniach może iść (apka by zwracała tylko pasujące ER-y)


RACZEJ NIEREALNE
- umawianie się z obcymi ludźmi (wtedy wybiera się pokój, do którego chce się iść i pasujące godziny i dni, a apka przydziela nam towarzystwo)
- integracja bazy danych z LockMe (zaciąganie danych o ER)
- tagi do escape roomów (każdy użytkownik zaznacza, jakiego typu pokoje go interesują)


ZUPEŁNIE NIEREALNE
- każdy uczestnik deklaruje, jak daleko może jechać i apka wybiera tylko ER w dogodnej dla wszystkich odległości (+ integracja z JakDojadę)
    --> mogłoby to działać nawet dla jednego użytkownika (jeśli np. przyjechał do obcego miasta i chce szybko wybrać ER, który jest blisko i jest akurat otwarty)
'''