from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Parent(models.Model):
	name = models.CharField(max_length=150)
	email = models.CharField(max_length=50)
	phone_number = models.CharField(max_length=15)
	referral = models.CharField(max_length=70)
	schooling_type = models.CharField(max_length=20)

	def __str__(self):
		return self.name

class Student(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	THEME_CHOICES = (
		('sp', 'Space'),
		('fo', 'Forest'),
		('ex', 'Explorer'),
		('ho', 'Hospital'),
		('su', 'Superhero'),
		('ra', 'Rabbit'),)
	parent = models.ForeignKey (
		'Parent',
		on_delete=models.CASCADE,)
	name = models.CharField(max_length=30)
	age = models.IntegerField()
	current_theme = models.CharField(
		max_length=20,
		choices=THEME_CHOICES,
		null=True,
		blank=True,)
	theme_set = models.CharField(max_length=30,null=True,blank=True,)
	current_level = models.IntegerField(default=1)
	gender = models.CharField(max_length=30)
	user_sessions = models.TextField(default='[]')

	def __str__(self):
		return self.name

class CodingQ(models.Model):
	difficulty = models.IntegerField()
	mover_position = models.CharField(blank=True,max_length=10)
	target_position = models.CharField(blank=True,max_length=10)
	secondary_target_positions = models.CharField(max_length=200, null=True, blank=True)
	obstacle_positions = models.CharField(max_length=200, null=True, blank=True)
	question_order = models.IntegerField()
	grid_size = models.CharField(blank=True,max_length=10)

	def __str__(self):
		return "L"+str(self.difficulty) + "-" + str(self.question_order)

class StudentPerformance(models.Model):
	difficulty = models.IntegerField()
	student_linked = models.ForeignKey (
		'Student',
		on_delete=models.CASCADE,)
	question = models.ForeignKey (
		'CodingQ',
		on_delete=models.CASCADE,)
	time_taken = models.CharField(blank=True,max_length=100)
	num_of_tries = models.IntegerField(default=0)
	code_tried = models.TextField(blank=True)

	def __str__(self):
		return str(self.student_linked) + '-' + str(self.question)
