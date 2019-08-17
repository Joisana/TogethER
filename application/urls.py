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

    # zapraszanie graczy (wybierasz, z kim chcesz pójść do ER)
    path('zapraszanie/', views.invitations, name ='invitations'),

    # znajomi gracze (można przeglądać, dodawać i usuwać ze znajomych)
    path('znajomi/', views.buddies, name = 'buddies'),

    # dobre pokoje (lista ER, w których żaden ze znajomych nie był)
    path('dobreER/', views.goodER, name = 'goodER'),

    # historia odwiedzin
    # dotychczasowe wyjścia ze znajomymi (widać, w jakich pokojach się było i z kim)
    path('historia/', views.history, name = 'history'),

    # gotowe wydarzenie
    path('wydarzenie/', views.event, name = 'event'),

    # ekran rejestracji użytkownika
    path('rejestracja/', views.registration, name = 'registration'),
]


# TE RZECZY POTEM SIĘ WKLEI DO ŚRODKA LISTY urlpatterns

'''
    # ekran logowania --> zamiast tego może być wyskakujące okno z logowaniem
    #path('logowanie', views.logging, name = 'logowanie')
'''





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