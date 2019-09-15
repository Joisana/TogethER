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