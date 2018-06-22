from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.http import Http404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Member
from .forms import MemberForm



def index(request):
	return render(request, 'stori/base.html')


def register(request):
	return render(request, 'stori/register.html')

def save(request):
	if request.method == "POST":
		mm = Member()
		mm.full_name = request.POST['full_name']
		mm.email = request.POST['email']
		mm.gender = request.POST['gender']
		mm.date_birth = request.POST['date_birth']
		mm.phone_number = request.POST['phone_number']
		mm.address = request.POST['address']
		mm.town_city = request.POST['town_city']
		mm.country = request.POST['country']
		mm.occupation = request.POST['occupation']
		mm.pics = request.FILES['image']
		mm.save()

	return render(request, 'stori/congrats.html')


def congrats(request):
	return render(request, 'stori/congrats.html')


def account(request):
	return render(request, 'stori/account.html')

def login(request):
    logout(request)
    username = password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/main/')
    return render_to_response('login.html', context_instance=RequestContext(request))

# @login_required(login_url='/login/')
# def main(request):









