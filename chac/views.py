from django.shortcuts import render, redirect, reverse
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

from .models import Post, Item, Event
from .forms import VolunteerForm, ContactForm, RegistrationForm

import stripe

#Home page view
def index(request):
	latest_posts = Post.objects.order_by('-creation_date')[:2]
	context = {
		"latest_posts": latest_posts,
	}
	return render(request, 'chac/index.html', context)

#Event schedule view
def schedule(request):
	schedule = Event.objects.order_by('-assigned_date').reverse()
	context = {
		"schedule": schedule,
	}
	return render(request, 'chac/schedule.html', context)

#Travel information view
def travel(request):
	context = {}
	return render(request, 'chac/travel.html', context)

#Event registration view
def register(request):
	if request.method == 'POST':
		form = RegistrationForm(request.POST)

		if form.is_valid():
			
			user = form.save()

			stripe.api_key = 'sk_test_s3NFutzfI5QM7EOByZfIdvyU00UZntBA2p'

			order_description = ""
			total = 0

			cart_items = request.POST.get('cart_items').split(';')
			for item in cart_items:
				if item:
					item_info = item.split(',')
					item_name = item_info[0]
					item_desc = item_info[1]
					item_cost = Item.objects.get(item_name=item_name).item_cost

					user.cart += item_name + "," + item_desc + "," + str(item_cost) + ";"
					

					total += item_cost

			user.save()
			total *= 100
			total = int(total)

			charge = stripe.Charge.create(
				amount=total,
				currency='cad',
				description='Creole Heritage Association Canada',
				source=request.POST['stripeToken']
			)

			return redirect('thanks', title="Thanks for registering", message="Your registration was a success!")
		else:
			return HttpResponse(form.errors)
	else:
		form = RegistrationForm()


	items = Item.objects.all()

	context = {
		"form": form,
		"items": items,
		"key": settings.STRIPE_PUBLISHABLE_KEY,
	}

	return render(request, 'chac/register.html', context)

#Volunteer registration view
def volunteer(request):
	if request.method == 'POST':
		form = VolunteerForm(request.POST)

		if form.is_valid():
			volunteer = form.save()
			return HttpResponseRedirect('thanks')
	else:
		form = VolunteerForm()

	context = {
		'form': form
	}

	return render(request, 'chac/volunteer.html', context)

#Contact us page view.
def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)

		if form.is_valid():
			send_mail(
				form.cleaned_data['first_name'] + " " + form.cleaned_data['last_name'] + " sent you a message",
				form.cleaned_data['message'] + "\n\nreply to: " + form.cleaned_data['email'],
				form.cleaned_data['email'],
				['macinnisbryce@gmail.com', form.cleaned_data['email']],
				#'creoleheritageassociationca@gmail.com' ],
				fail_silently=False,
			)

			return HttpResponseRedirect()
	else:
		form = ContactForm()

	context = {
		'form': form,
	}

	return render(request, 'chac/contact.html', context)

#Read the posts in more detail view
def detail(request, post_title):
	post = Post.objects.get(post_title=post_title)

	context = {
		"post": post,
	}
	return render(request, 'chac/detail.html', context)

def thanks(request):
	context = {
	}
	return render(request, 'chac/thanks.html', context)