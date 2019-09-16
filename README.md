TogethER – aplikacja do umawiania się do escape roomów
======================================================

Działanie aplikacji
-------------------

Aplikacja umożliwia:

* przeglądanie istniejących escape roomów (oglądanie ich na LockMe)
* rejestrację użytkowników
* logowanie użytkowników
* zaznaczanie, które escape roomy już odwiedziliśmy
* wyświetlanie tylko odwiedzonych lub tylko nieodwiedzonych escape roomów
* przeglądanie profili użytkowników
* patrzenie, w ilu i których escape roomach byliśmy tych samych co inny użytkownik
* dodawanie i usuwanie innych użytkowników ze znajomych
* tworzenie i edytowanie wydarzeń (wyjść do escape roomów)
* przegląd planowanych wyjść do escape roomów

Tworzenie wydarzeń
------------------

W ramach wydarzenia można zapraszać użytkowników (wpisując ich nick lub wybierając z listy znajomych). Aplikacja sama zaproponuje wszystkie escape roomy, w których nikt spośród uczestników wydarzenia jeszcze nie był. Można wybrać escape room, do którego się wybierzemy :D Jeśli już ktoś kliknął escape room, a wolimy się jeszcze pozastanawiać, który wybrać, możemy wycofać decyzję (przycisk "Jeszcze się nie zdecydowałem"). Jeśli zrezygnujemy z wyjścia do escape roomu, można usunąć wydarzenie.

Panel administratora
--------------------

Escape roomy można dodawać, edytować i usuwać w panelu administracyjnym Django (/admin). Jest on w zasadzie potrzebny tylko do tego; resztę rzeczy można zrobić w obrębie aplikacji.


Budowanie projektu
------------------

Aplikacja została napisana w Django 2.2.4 z użyciem Pythona 3.