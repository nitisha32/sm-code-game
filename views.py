from django.shortcuts import render, redirect
from .models import StudentPerformance, CodingQ, Parent, Student
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index(request):
	if request.method=='POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('/codinggame/exercises')
		else:
			return render(request,'login_fail.html')
	return render(request,'login.html')

def exercises(request):
	student = Student.objects.get(user=request.user)
	if request.method=='POST' and 'theme' in request.POST:
		print("selected theme: ", request.POST['theme'])
		student.current_theme = request.POST['theme']
		student.save()

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
		new_record.save()
	elif request.method == 'POST' and 'goToQues' in request.POST:
		new_counter = int(request.POST['goToQues']) - 1

		student_data = StudentPerformance.objects.filter(student_linked=student).order_by('-question')
		all_questions = CodingQ.objects.all().order_by('question_order')
		question = all_questions[new_counter]
		ques_counter = 0
		for ques in all_questions:
			ques_counter+=1
			if ques == student_data[0].question:
				break
		question.target_position = question.target_position.split(',')
		question.mover_position = question.mover_position.split(',')
		target_loc = []
		mover_loc = []
		for item in question.target_position:
			item = int(item)
			target_loc.append(item)
		question.target_position = target_loc
		for item in question.mover_position:
			item = int(item)
			mover_loc.append(item)
		question.mover_position = mover_loc
		if question.obstacle_positions != None:
			question.obstacle_positions = question.obstacle_positions.split(',')
			counter = 0
			obstacles_loc = []
			for position in question.obstacle_positions:
				if counter%2==0:
					obstacles_loc.append([int(question.obstacle_positions[counter]),int(question.obstacle_positions[counter+1])])
				counter+=1
			question.obstacle_positions = obstacles_loc
		q_meta_data = { 'totalq': len(all_questions), 'currentq': new_counter+1, 'completedq': ques_counter+1}
		section_theme = student.current_theme
		context = {
			'question': question,
			'q_meta_data': q_meta_data,
			'username': student.name,
			'section_theme': section_theme
		}
		return render(request,'exercises.html', context = context)
	elif request.method == 'POST' and 'logout' in request.POST:
		logout(request)
		return redirect('/testing1')
	if student.current_theme ==None:
		context = {
			'username': student.name,
		}
		return render(request, 'choose_theme.html', context=context)
	else:	
		student_data = StudentPerformance.objects.filter(student_linked=student).order_by('-question')
		all_questions = CodingQ.objects.all().order_by('question_order')
		q_counter = 0
		if len(student_data) != 0:
			for ques in all_questions:
				q_counter+=1
				if ques == student_data[0].question:
					break
		try:
			question = all_questions[q_counter]
		except:
			return render(request,'completed.html')
		q_meta_data = { 'totalq': len(all_questions), 'currentq': q_counter+1,  'completedq': q_counter+1}
		
		question.target_position = question.target_position.split(',')
		question.mover_position = question.mover_position.split(',')
		target_loc = []
		mover_loc = []
		for item in question.target_position:
			item = int(item)
			target_loc.append(item)
		question.target_position = target_loc
		for item in question.mover_position:
			item = int(item)
			mover_loc.append(item)
		question.mover_position = mover_loc
		if question.obstacle_positions != None:
			question.obstacle_positions = question.obstacle_positions.split(',')
			counter = 0
			obstacles_loc = []
			for position in question.obstacle_positions:
				if counter%2==0:
					obstacles_loc.append([int(question.obstacle_positions[counter]),int(question.obstacle_positions[counter+1])])
				counter+=1
			question.obstacle_positions = obstacles_loc
		section_theme = student.current_theme
		context = {
			'question': question,
			'q_meta_data': q_meta_data,
			'username': student.name,
			'section_theme': section_theme
		}
		return render(request,'exercises.html', context=context)