def clean_question(question):

	#Primary target
	target_loc = []
	question.target_position = question.target_position.split(',')
	for item in question.target_position:
		item = int(item)
		target_loc.append(item)
	question.target_position = target_loc

	#Grid Size
	grid = []
	question.grid_size = question.grid_size.split(',')
	for item in question.grid_size:
		item = int(item)
		grid.append(item)
	question.grid_size = grid
	
	#Mover
	mover_loc = []
	question.mover_position = question.mover_position.split(',')
	for item in question.mover_position:
		item = int(item)
		mover_loc.append(item)
	question.mover_position = mover_loc

	#Obstacles
	if question.obstacle_positions != None:
		question.obstacle_positions = question.obstacle_positions.split(',')
		counter = 0
		obstacles_loc = []
		for position in question.obstacle_positions:
			if counter%2==0:
				obstacles_loc.append([int(question.obstacle_positions[counter]),int(question.obstacle_positions[counter+1])])
			counter+=1
		question.obstacle_positions = obstacles_loc

	#Secondary Targets
	if question.secondary_target_positions != None:
		question.secondary_target_positions = question.secondary_target_positions.split(',')
		counter = 0
		sec_target_loc = []
		for position in question.secondary_target_positions:
			if counter%2==0:
				sec_target_loc.append([int(question.secondary_target_positions[counter]),int(question.secondary_target_positions[counter+1])])
			counter+=1
		question.secondary_target_positions = sec_target_loc

	return question