from django.shortcuts import render, redirect
from .models import StudentPerformance, CodingQ, Parent, Student
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from .tools import clean_question
from datetime import datetime

# Create your views here.
def index(request):
	return redirect('/codinggame/login')

def login(request):
	if not(request.user.is_anonymous):
		student = Student.objects.get(user=request.user)
		if student.current_theme == None:
			return redirect('/codinggame/choose_theme')
		else:
			return redirect('/codinggame/exercises')
	if request.method=='POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			auth_login(request, user)
			student = Student.objects.get(user=request.user)
			student.user_sessions += '[' +str(datetime.now()) + ','
			student.save()
			if student.current_theme == None:
				return redirect('/codinggame/choose_theme')
			else:
				return redirect('/codinggame/exercises')
		else:
			return render(request,'login_fail.html')
	return render(request,'login.html')

def choose_theme(request):
	student = Student.objects.get(user=request.user)
	if request.method=='POST' and 'theme' in request.POST:
		student.current_theme = request.POST['theme']
		student.save()
		if student.current_level==1:
			return redirect('/codinggame/tutorial')
		else:
			return redirect('/codinggame/exercises')
	elif request.method == 'POST' and 'logout' in request.POST:
		student.user_sessions += str(datetime.now()) + '],'
		student.save()
		logout(request)
		return redirect('/codinggame')

	if student.current_level == 1:
		message = "Welcome " + student.name + "! Choose your adventure"
		adventures = ['sp', 'ho', 'su']
		adventure_urls = ['img/space.png', 'img/hospital.png', 'img/superhero.png']
		adventure_details = ['Be an astronaut in search for new planets', 'Drive your ambulance and save lives', 'Be a superhero and save a plane from crashing']
	else:
		congrats = str(student.current_level - 1)
		message = "Congratulations on completing level " + congrats + ", " + student.name + "! Choose your next adventure"
		adventures = ['ex', 'ra', 'fo']
		adventure_urls = ['img/desert.png', 'img/rabbit.png', 'img/forest.png']
		adventure_details = ['Look for treasure at an ancient temple', 'Help the hungry rabbit find carrots', 'Be a farmer and harvest crops']
	context = {
		'message': message,
		'adventures': adventures,
		'adventure_urls': adventure_urls,
		'adventure_details': adventure_details,
		'username': student.name
	}
	return render(request, 'choose_theme.html', context=context)

def tutorial(request):
	if request.method == 'POST' and 'skip' in request.POST:
		return redirect('/codinggame/exercises')
	elif request.method == 'POST' and 'logout' in request.POST:
		student.user_sessions += str(datetime.now()) + '],'
		student.save()
		logout(request)
		return redirect('/codinggame/')
	student = Student.objects.get(user=request.user)
	if student.current_theme!=None:
		section_theme = student.current_theme
	else:
		return redirect('/codinggame/choose_theme')
	ex_url = 'exercises-tut-' + section_theme + '.html'
	context = {
		'username': student.name,
	}
	return render(request, ex_url, context=context)


def exercises(request):
	if (request.user.is_anonymous):
		return redirect('/codinggame/login')
	student = Student.objects.get(user=request.user)
	if request.method == 'POST' and 'tries' in request.POST:
		tries = request.POST['tries']
		time_taken = request.POST['timetaken'].split(',')
		code_tried = request.POST['codetried']
		question_id = request.POST['questionid']

		code_tried_list = []
		current_element = ''
		for letter in code_tried:
			if letter == '[':
				pass
			elif letter == ' ':
				pass
			elif letter == ']':
				if current_element[0] == ',':
					current_element = current_element[1:]
				current_element = current_element.split(',')
				code_tried_list.append(current_element)
				current_element = ''
			else:
				current_element+=letter
		for item in time_taken:
			item = int(item)

		new_record = StudentPerformance()
		new_record.student_linked = student
		new_record.question = CodingQ.objects.get(id=question_id)
		new_record.time_taken = time_taken
		new_record.code_tried = code_tried_list
		new_record.num_of_tries = tries
		new_record.difficulty = CodingQ.objects.get(id=question_id).difficulty
		new_record.save()
	elif request.method == 'POST' and 'goToQues' in request.POST:
		new_counter = int(request.POST['goToQues']) - 1
		student_data = StudentPerformance.objects.filter(student_linked=student, difficulty=student.current_level).order_by('-question')
		all_questions = CodingQ.objects.filter(difficulty=student.current_level).order_by('question_order')
		ques_counter= 1 + CodingQ.objects.get(id=student_data[0].question_id).question_order
		q_details = clean_question(all_questions[new_counter])
		q_meta_data = { 
			'totalq': len(all_questions), 
			'currentq': new_counter+1, 
			'completedq': ques_counter
		}
		ex_url = 'exercises-' + student.current_theme + '.html'
		context = {
			'question': q_details,
			'q_meta_data': q_meta_data,
			'username': student.name,
		}
		return render(request,ex_url, context = context)
	elif request.method == 'POST' and 'logout' in request.POST:
		student.user_sessions += str(datetime.now()) + '],'
		student.save()
		logout(request)
		return redirect('/codinggame/')
	
	#Without any POST request
	student_data = StudentPerformance.objects.filter(student_linked=student, difficulty=student.current_level).order_by('-question')
	all_questions = CodingQ.objects.filter(difficulty=student.current_level).order_by('question_order')
	current_q = 1
	if len(student_data)!=0:
		current_q= 1 + CodingQ.objects.get(id=student_data[0].question_id).question_order
		print(current_q)
		if current_q == len(all_questions) + 1:
			if student.theme_set == None:
				student.theme_set = student.current_theme + ','
			else:
				student.theme_set += student.current_theme + ','
			student.current_level += 1
			student.current_theme=None
			student.save()
			return redirect('/codinggame/choose_theme')
	q_details = clean_question(CodingQ.objects.get(question_order=current_q, difficulty=student.current_level))
	q_meta_data = { 
		'totalq': len(all_questions), 
		'currentq': current_q,  
		'completedq': current_q
	}
	if student.current_theme!=None:
		section_theme = student.current_theme
	else:
		return redirect('/codinggame/choose_theme')
	
	ex_url = 'exercises-' + section_theme + '.html'
	context = {
		'question': q_details,
		'q_meta_data': q_meta_data,
		'username': student.name,
	}
	return render(request,ex_url, context=context)
		
