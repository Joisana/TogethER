from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.urls import reverse

from .models import EscapeRoom, GoingOut, User


def getMe(request):
	try:
		return User.objects.get(id=request.session['user_id'])
	except (KeyError, User.DoesNotExist):
		return None

def index(request):
	return render(request, 'application/index.html', {'me': getMe(request)})

def users(request):
	return HttpResponse("Tutaj będzie lista wszystkich użytkowników.")

def history(request):
    return HttpResponse("Tutaj będzie historia odwiedzin.")

def registration(request):

	# jeśli użytkownik pierwszy raz otwiera stronę z rejestracją (przed wysłaniem formularza)
	if 'username' not in request.POST:
		return render(request, 'application/registration.html', {})

	# jeśli nazwa użytkownika jest pusta (użytkownik zostawił puste pole)
	if not request.POST['username']:
		return render(request, 'application/registration.html', {
            'error_message': "Nazwa użytkownika nie może być pusta.",
        })

	# jeśli powtarza się nazwa użytkownika
	if User.objects.filter(username=request.POST['username']): 
		return render(request, 'application/registration.html', {
			'error_message_exists': request.POST['username'],
		})

	# jeśli hasło jest za krótkie (użytkownik zostawił puste pole lub wpisał za krótkie hasło)
	if len(request.POST['password']) <3:
		return render(request, 'application/registration.html', {
            'error_message': "Hasło jest za krótkie. Wybierz hasło długości co najmniej 3 znaków.",
        })

	newUser = User()
	newUser.username = request.POST['username']
	newUser.passwordHash = request.POST['password']
	newUser.save()

	return HttpResponseRedirect(reverse('application:index'))


def login(request):

	if 'username' not in request.POST:
		return render(request, 'application/login.html', {})

	try:
		user = User.objects.get(username=request.POST['username'])
		if user.passwordHash != request.POST['password']:
			raise Exception('Invalid password')
		request.session['user_id'] = user.id
		return HttpResponseRedirect(reverse('application:index'))
	except:
		return render(request, 'application/login.html', {'error_message': "Nieprawidłowa nazwa użytkownika lub hasło."})

def logout(request):
    try:
        del request.session['user_id']
    except KeyError:
        pass
    return HttpResponseRedirect(reverse('application:index'))



def escaperooms(request):

	if 'user_id' not in request.session:
		return render(request, 'application/escaperooms.html', {
			'escaperooms': EscapeRoom.objects.all(),
		})

	me = User.objects.get(id=request.session['user_id'])

	if 'escaperooms_changes' in request.POST: # jeśli kliknięto "Zapisz zmiany"
		# lista id odwiedzonych escape roomów
		visitedIdList = [int(s) for s in request.POST.getlist('escaperooms[]')]
		me.visited.set([EscapeRoom.objects.get(id = i) for i in visitedIdList])
		me.save()

		return HttpResponseRedirect(reverse('application:escaperooms'))

	visited = me.visited.all()

	return render(request, 'application/escaperooms.html', {
		'escaperooms': EscapeRoom.objects.all(),
		'me': getMe(request),
		'visited': visited,
		'which_escape_rooms': request.POST.get('which_escape_rooms', 'all'),
	})


def goingOut(request, goingout_id):

	me = getMe(request)
	if not me:
		return render(request, 'application/index.html', {})

	go = GoingOut.objects.get(id = goingout_id)

	if 'chosen_escaperoom' in request.POST:
		escapeRoom = EscapeRoom.objects.get(id = request.POST['chosen_escaperoom'])
		go.decision = escapeRoom
		go.save()


	visited_by_participants = EscapeRoom.objects.none() # pusty queryset

	
	# escape roomy, w których chociaż jeden uczestnik wydarzenia już był
	for participant in go.participants.all():
		visited_by_participants = visited_by_participants.union(participant.visited.all())
	
	unvisited = EscapeRoom.objects.all().difference(visited_by_participants)


	if 'participant_name' in request.POST:
		try:
			participant = User.objects.get(username = request.POST['participant_name'])
		except User.DoesNotExist:
			return render(request, 'application/goingout.html', {
				'go': go,
				'participant_error_message': "Taki użytkownik nie istnieje.",
				'unvisited': unvisited,
				'me': me,
			})
		else:
			go.participants.add(participant)
			go.save()
			return HttpResponseRedirect("/wyjscie/" + str(go.pk))

	if 'delete_event' in request.POST:
		go.delete()
		return HttpResponseRedirect(reverse('application:planned'))


	if 'reset_decision' in request.POST:
		go.decision = None
		go.save()
		return HttpResponseRedirect(reverse('application:goingout', kwargs={'goingout_id': goingout_id}))


	return render(request, 'application/goingout.html', {
		'go': go,
		'unvisited': unvisited,
		'me': me,
	})


def newGoingOut(request):
	go = GoingOut()

	go.organisator = getMe(request)
	if not go.organisator:
		return HttpResponseRedirect(reverse('application:index'))

	go.save()
	go.participants.add(go.organisator)
	go.save()

	return HttpResponseRedirect("/wyjscie/" + str(go.pk))


def planned(request):

	me = getMe(request)
	if not me:
		return HttpResponseRedirect(reverse('application:index'))

	planned_goingouts = me.goingOuts.all()
	return render(request, 'application/planned.html', {
		'planned_goingouts': planned_goingouts.all(),
		'me': me,
	})

def buddies(request):
	
	me = getMe(request)
	if not me:
		return HttpResponseRedirect(reverse('application:index'))

	if 'buddy_name' in request.POST:
		try:
			buddy = User.objects.get(username = request.POST['buddy_name'])
			if buddy == me:
				return render(request, 'application/buddies.html', {
					'me_error_message': "Niestety nie możesz sam siebie dodać do znajomych :(",
					'me': me,
				})
		except User.DoesNotExist:
			return render(request, 'application/buddies.html', {
				'buddy_error_message': "Taki użytkownik nie istnieje.",
				'me': me,
			})
		me.buddies.add(buddy)
		me.save()
		return HttpResponseRedirect(reverse('application:buddies'))

	return render(request, 'application/buddies.html', {
		'me': me,
	})

def profile(request, user_id):

	try:
		user = User.objects.get(id = user_id)
	except User.DoesNotExist:
		raise Http404("Użytkownik nie istnieje.")

	return render(request, 'application/profile.html', {
		'me': getMe(request),
		'user': user,
	})
