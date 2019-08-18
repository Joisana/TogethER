from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.urls import reverse

from .models import User, EscapeRoom

def getUsername (request):
	try:
		return User.objects.get(id=request.session['user_id']).username
	except (KeyError, User.DoesNotExist):
		return ''

def index(request):
	return render(request, 'application/index.html', {'username': getUsername(request)})

def users(request):
	return HttpResponse("Tutaj będzie lista wszystkich użytkowników.")

def buddies(request):
	return HttpResponse("Tutaj będzie lista znajomych danego użytkownika.")

def invitations(request):
	return HttpResponse("Tutaj będzie możliwość wybierania z listy znajomych, których się zaprasza (lub wpisywania w okienko nicku).")

def goodER(request):
	return HttpResponse("Tutaj będzie lista ER, w których żadna z idących osób jeszcze nie była.")

def history(request):
    return HttpResponse("Tutaj będzie historia odwiedzin.")

def planned(request):
	return HttpResponse("Tutaj będą planowane pokoje.")

def event(request):
	return HttpResponse("Tutaj będzie link do wydarzenia (wyjścia do ER) z informacją o pokoju, dacie, godzinie, kto idzie itp.")

def registration(request):
	newUser = User()

	# jeśli użytkownik pierwszy raz otwiera stronę z rejestracją (przed wysłaniem formularza)
	if 'username' not in request.POST:
		return render(request, 'application/registration.html', {})
	
	newUser.username = request.POST['username']

	# jeśli nazwa użytkownika jest pusta (użytkownik zostawił puste pole)
	if not newUser.username:
		return render(request, 'application/registration.html', {
            'error_message': "Nazwa użytkownika nie może być pusta.",
        })

	# jeśli powtarza się nazwa użytkownika
	if User.objects.filter(username=newUser.username): 
		return render(request, 'application/registration.html', {
			'error_message_exists': newUser.username,
		})

	# jeśli hasło jest za krótkie (użytkownik zostawił puste pole lub wpisał za krótkie hasło)
	if len(request.POST['password']) <3:
		return render(request, 'application/registration.html', {
            'error_message': "Hasło jest za krótkie. Wybierz hasło długości co najmniej 3 znaków.",
        })

	newUser.passwordHash = request.POST['password']

	newUser.save()
	return HttpResponseRedirect(reverse('application:index'))


def login(request):

	if 'username' not in request.POST:
		return render(request, 'application/login.html', {})

	try:
		user = User.objects.get(username=request.POST['username'])
	except:
		return render(request, 'application/login.html', {'error_message': "Nieprawidłowy user"})

	
	if user.passwordHash == request.POST['password']:
		request.session['user_id'] = user.id
		return HttpResponseRedirect(reverse('application:index'))
	else:
		return render(request, 'application/login.html', {'error_message': "Nieprawidłowe hasło."})


def logout(request):
    try:
        del request.session['user_id']
    except KeyError:
        pass
    return HttpResponseRedirect(reverse('application:index'))


def escaperooms(request):
	return render(request, 'application/escaperooms.html', {
		'escaperooms': EscapeRoom.objects.all(),
		'username': getUsername(request),
	})
