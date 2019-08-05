from django.db import models

# Create your models here.
class Post(models.Model):
	#When was the post made
	creation_date = models.DateTimeField('date posted')

	#The title of the post
	post_title = models.CharField(max_length=200)

	#The short preview of the article
	post_short_text = models.CharField(max_length=500)

	#The full content of the post
	post_content = models.CharField(max_length=3000)

	#The link to the image for this post
	post_image_url = models.CharField(max_length=200)

	def __str__(self):
		return self.post_title + ":" + str(self.creation_date)

class Volunteer(models.Model):
	#First name of the volunteer
	first_name = models.CharField(max_length=200)

	#Last name of the volunteer
	last_name = models.CharField(max_length=200)

	#Email of the volunteer
	email = models.EmailField(max_length=254)

	#Volunteer's phone number
	account_phone = models.CharField(max_length=15)

	#Any additional information
	additional_information = models.CharField(max_length=500)

	def __str__(self):
		return self.first_name + " " + self.last_name + ":" + str(self.email)

class Event(models.Model):
	#Which day of the week it is.
	day_of_the_week = models.CharField(max_length=200)

	#The date the event is going to happen
	assigned_date = models.DateField('date assigned')

	#The schedule for the events.
	events = models.CharField(max_length=1000)

	#The link to the image for this event
	image_url = models.CharField(max_length=200)

	def __str__(self):
		return self.day_of_the_week + ":" + str(self.assigned_date)

class User(models.Model):
	#Person's name who registered account
	first_name = models.CharField(max_length=200)

	#Person's name who registered account
	last_name = models.CharField(max_length=200)

	#Person's email who registered account
	email = models.EmailField(max_length=254)

	#Person's phone number who registered account
	phone = models.CharField(max_length=15)

	#The events the person registered for.
	events = models.CharField(max_length=1500)

	#Any additional guests they are bringing with them.
	additional_guests = models.CharField(max_length=1500)

	#User's cart
	cart = models.CharField(max_length=1500)

	def __str__(self):
		return self.first_name + " " + self.last_name + ":" + self.email

class Item(models.Model):
	#What was the name of the item?
	item_name = models.CharField(max_length=200)

	#What was the cost of the item?
	item_cost = models.FloatField(default=0)

	#Description of the item.
	item_description = models.CharField(max_length=1000)

	#Order information about item
	order_info = models.CharField(max_length=1000)

	def __str__(self):
		return self.item_name + ":cost" + str(self.item_cost)

