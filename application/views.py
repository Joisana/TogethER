from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.urls import reverse

from .models import User, EscapeRoom


def index(request):
	return HttpResponse("Tutaj będzie strona główna.")
	

def visited(request):
	return HttpResponse("Tutaj będą odwiedzone pokoje.")

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

def event(request):
	return HttpResponse("Tutaj będzie link do wydarzenia (wyjścia do ER) z informacją o pokoju, dacie, godzinie, kto idzie itp.")

def registration(request):
	newUser = User()
	try:
		newUser.username = request.POST['username']
	except (KeyError):
		return render(request, 'application/registration.html', {})
	
	# tutaj można poifować np. białe znaki
	if newUser.username:
		if User.objects.filter(username=newUser.username):
			return render(request, 'application/registration.html', {
				'error_message_exists': newUser.username
			})
		else:
			newUser.save()

	else:
		return render(request, 'application/registration.html', {
            'error_message': "Nazwa użytkownika nie może być pusta.",
        })

	return HttpResponseRedirect(reverse('application:index'))

	# , args=(question.id,)

def escaperooms(request):
	return render(request, 'application/escaperooms-unlogged.html', {
            'escaperooms': EscapeRoom.objects.all,
        })

