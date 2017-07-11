import random
import pickle


objects_a = ['snack -Bobject-', 'cereals -Bobject -bar -Iobject-', 'cookie -Bobject-', 'book -Bobject-', 'pen -Bobject-', 'notebook -Bobject-',
			'laptop -Bobject-', 'tablet -Bobject-', 'charger -Bobject-', 'pencil -Bobject-', 'peanut -Bobject-',
			'biscuit -Bobject-', 'candy -Bobject-', 'chocolate -Bobject -br -Iobject-', 'chewing -Bobject- gum -Iobject-',
			'chocolate -Bobject- egg -Iobject-', 'chocolate -Bobject- tablet -Iobject-',
			'donuts -Bobject-', 'cake -Bobject-', 'pie -Bobject-', 'peach -Bobject-', 'strawberry -Bobject-',
			'blueberry -Bobject-', 'blackberry -Bobject-', 'burger -Bobject-', 'lemon -Bobject-', 'lemon -Bobject-',
			'banana -Bobject-', 'watermelon -Bobject-', 'pepper -Bobject-', 'pear -Bobject-', 'pizza -Bobject-', 'yogurt -Bobject-',
			'drink -Bobject-', 'beer -Bobject-', 'coke -Bobject-', 'sprite -Bobject-', 'sake -Bobject-', 'toothpaste -Bobject-',
			'cream -Bobject-', 'lotion -Bobject-', 'dryer -Bobject-', 'comb -Bobject-', 'towel -Bobject-', 'shampoo -Bobject-',
			'soap -Bobject-', 'choth -Bobject-', 'sponge -Bobject-', 'toothbrush -Bobject-', 'container -Bobject-', 'glass -Bobject-',
			'can -Bobject-', 'bottle -Bobject-', 'fork -Bobject-', 'knife -Bobject-', 'bowl -Bobject-', 'tray -Bobject-', 'plate -Bobject-',
			'newspaper -Bobject-', 'magazine -Bobject-']

objects_an = ['almond -Bobject-', 'onion -Bobject-', 'orange -Bobject-', 'apple -Bobject-']

objects_the = ['cookies -Bobject-', 'almonds -Bobject-', 'book -Bobject-', 'pen -Bobject-', 'notebook -Bobject-', 'laptop -Bobject-',
 			'tablet -Bobject-', 'charger -Bobject-', 'pencil -Bobject-', 'chips -Bobject-', 'senbei -Bobject-', 'pringles -Bobject-',
			'peanuts -Bobject-', 'biscuits -Bobject-', 'crackers -Bobject-', 'candies -Bobject-', 'chocolate -Bobject -br -Iobject-',
			'manju -Bobject-', 'mints -Bobject-', 'chewing -Bobject- gums -Iobject-', 'chocolate -Bobject- egg -Iobject-',
			'chocolate -Bobject- tablet -Iobject-', 'donuts -Bobject-', 'cake -Bobject-', 'pie -Bobject-', 'food -Bobject-',
			'peach -Bobject-', 'strawberries -Bobject-', 'grapes -Bobject-', 'blueberries -Bobject-', 'blackberries -Bobject-',
			'salt -Bobject-', 'sugar -Bobject-', 'bread -Bobject-', 'cheese -Bobject-', 'ham -Bobject-', 'burger -Bobject-',
			'lemon -Bobject-', 'onion -Bobject-', 'lemons -Bobject-', 'apples -Bobject-', 'onions -Bobject-', 'orange -Bobject-', 'oranges -Bobject-',
			'peaches -Bobject-', 'banana -Bobject-', 'bananas -Bobject-', 'noodles -Bobject-', 'apple -Bobject-', 'paprika -Bobject-',
			'watermelon -Bobject-', 'sushi -Bobject-', 'pepper -Bobject-', 'pear -Bobject-', 'pizza -Bobject-', 'yogurt -Bobject-',
			'drink -Bobject-', 'milk -Bobject-', 'juice -Bobject-', 'coffee -Bobject-', 'hot -Bobject- chocolate', 'whisky -Bobject-',
			'rum -Bobject-', 'vodka -Bobject-', 'cider -Bobject-', 'lemonade -Bobject-', 'tea -Bobject-', 'water -Bobject-', 'beer -Bobject-',
			'coke -Bobject-', 'sprite -Bobject-', 'wine -Bobject-', 'sake -Bobject-', 'toiletries -Bobject-', 'toothpaste -Bobject-',
			'cream -Bobject-', 'lotion -Bobject-', 'dryer -Bobject-', 'comb -Bobject-', 'towel -Bobject-', 'shampoo -Bobject-', 'soap -Bobject-',
			'cloth -Bobject-', 'sponge -Bobject-', 'toilet -Bobject- paper', 'toothbrush -Bobject-', 'container -Bobject-', 'containers -Bobject-',
			'glass -Bobject-', 'can -Bobject-', 'bottle -Bobject-', 'fork -Bobject-', 'knife -Bobject-', 'bowl -Bobject-', 'tray -Bobject-',
			'plate -Bobject-', 'newspaper -Bobject-', 'magazine -Bobject-']

objects_some = ['snacks -Bobject-', 'cookies -Bobject-', 'almonds -Bobject-', 'books -Bobject-', 'pens -Bobject-', 'chips -Bobject-',
 			'pringles -Bobject-', 'magazines -Bobject-', 'newspapers -Bobject-', 'peanuts -Bobject-', 'biscuits -Bobject-', 'crackers -Bobject-',
 			'candies -Bobject-', 'mints -Bobject-', 'chewing -Bobject- gums -Iobject-', 'donuts -Bobject-', 'cake -Bobject-', 'pie -Bobject-',
 			'food -Bobject-', 'strawberries -Bobject-', 'grapes -Bobject-', 'blueberries -Bobject-', 'blackberries -Bobject-', 'salt -Bobject-',
 			'sugar -Bobject-', 'bread -Bobject-', 'cheese -Bobject-', 'ham -Bobject-', 'lemons -Bobject-', 'apples -Bobject-',
 			'onions -Bobject-', 'oranges -Bobject-', 'peaches -Bobject-', 'bananas -Bobject-', 'noodles -Bobject-', 'paprika -Bobject-',
 			'watermelon -Bobject-', 'sushi -Bobject-', 'pepper -Bobject-', 'pizza -Bobject-', 'yogurt -Bobject-', 'drink -Bobject-',
 			'milk -Bobject-', 'juice -Bobject-', 'coffee -Bobject-', 'hot -Bobject- chocolate -Iobject-',
			'whisky -Bobject-', 'rum -Bobject-', 'vodka -Bobject-', 'cider -Bobject-', 'lemonade -Bobject-', 'tea -Bobject-', 'water -Bobject-',
			'beer -Bobject-', 'coke -Bobject-', 'sprite -Bobject-', 'wine -Bobject-', 'sake -Bobject-', 'toilet -Bobject- paper -Iobject-', 
			'containers -Bobject-', 'glasses -Bobject-', 'cans -Bobject-', 'bottles -Bobject-', 'forks -Bobject-', 'knifes -Bobject-',
			'bowls -Bobject-', 'trays -Bobject-', 'plates -Bobject-']

objects_a_piece_of = ['cake -Bobject-', 'pie -Bobject-', 'bread -Bobject-', 'cheese -Bobject-', 'ham -Bobject-', 'watermelon -Bobject-',
					 'sushi -Bobject-', 'pizza -Bobject-']

objects_a_cup_of = ['milk -Bobject-', 'coffee -Bobject-', 'hot -Bobject- chocolate -Iobject-', 'cider -Bobject-', 'lemonade -Bobject-',
					'tea -Bobject-', 'water -Bobject-', 'beer -Bobject-']

objects_a_can_of = ['red -Bobject -bll -Iobject-', 'cider -Bobject-', 'iced -Bobject- tea -Iobject-', 'beer -Bobject-', 'coke -Bobject-',
					 'sprite -Bobject-']

objects_a_glass_of = ['milk -Bobject-', 'juice -Bobject-', 'coffee -Bobject-', 'hot -Bobject- chocolate -Iobject-', 'whisky -Bobject-',
					'rum -Bobject-', 'vodka -Bobject-', 'cider -Bobject-', 'lemonade -Bobject-', 'iced -Bobject- tea -Iobject-',
					'water -Bobject-', 'beer -Bobject-', 'coke -Bobject-', 'sprite -Bobject-', 'wine -Bobject-', 'sake -Bobject-']

objects_a_bottle_of = ['milk -Bobject-', 'juice -Bobject-', 'whisky -Bobject-', 'rum -Bobject-', 'vodka -Bobject-', 'cider -Bobject-',
					 'lemonade -Bobject-', 'iced -Bobject- tea -Iobject-', 'water -Bobject-', 'beer -Bobject-', 'coke -Bobject-',
					 'sprite -Bobject-', 'wine -Bobject-','sake -Bobject-']



locations = ['bedroom -Blocation-', 'bed -Blocation-', 'bedside -Blocation-', 'closet -Blocation-', 'living -Blocation- room -Ilocation-',
			'TV -Blocation- stand -Ilocation-', 'sofa -Blocation-', 'couch -Blocation-', 'bedroom -Blocation- chair -Ilocation-',
			'kitchen -Blocation- chair -Ilocation-', 'living -Blocation- table -Ilocation-', 'center -Blocation- table -Ilocation-',
			'bar -Blocation-', 'office -Blocation-', 'drawer -Blocation-', 'desk -Blocation-', 'kitchen -Blocation-', 'bar -Blocation-',
			'cupboard -Blocation-', 'sink -Blocation-', 'sideshelf -Blocation-', 'bookcase -Blocation-',
			'dining -Blocation- table -Ilocation-', 'fridge -Blocation-', 'counter -Blocation-', 'corridor -Blocation-', 'door -Blocation-',
			'cabinet -Blocation-', 'bathroom -Blocation-', 'toilet -Blocation-', 'table -Blocation-']



names_female = ['hanna -Bperson-', 'barbara -Bperson-', 'samantha -Bperson-', 'erika -Bperson-', 'sophie -Bperson-', 'jackie -Bperson-',
				'skyler -Bperson-', 'jane -Bperson-', 'olivia -Bperson-', 'emily -Bperson-', 'amelia -Bperson-', 'lily -Bperson-',
				'grace -Bperson-', 'ella -Bperson-', 'scarlett -Bperson-', 'isabelle -Bperson-', 'charlotte -Bperson-', 'daisy -Bperson-',
				'sienna -Bperson-', 'chloe -Bperson-', 'alice -Bperson-', 'lucy -Bperson-', 'florence -Bperson-', 'rosie -Bperson-',
				'amelie -Bperson-', 'eleanor -Bperson-', 'emilia -Bperson-', 'amber -Bperson-', 'ivy -Bperson-', 'brooke -Bperson-',
				'summer -Bperson-', 'emma -Bperson-', 'rose -Bperson-', 'martha -Bperson-', 'faith -Bperson-', 'amy -Bperson-',
				'katie -Bperson-', 'madison -Bperson-', 'sarah -Bperson-', 'zoe -Bperson-', 'paige -Bperson-'] 


names_male = ['ken -Bperson-', 'erik -Bperson-', 'samuel -Bperson-', 'skyler -Bperson-', 'brian -Bperson-', 'thomas -Bperson-',
			'edward -Bperson-', 'michael -Bperson-', 'charlie -Bperson-', 'alex -Bperson-', 'john -Bperson-', 'james -Bperson-',
			'oscar -Bperson-', 'peter -Bperson-', 'oliver -Bperson-', 'jack -Bperson-', 'harry -Bperson-', 'henry -Bperson-',
			'jacob -Bperson-', 'thomas -Bperson-', 'william -Bperson-', 'will -Bperson-', 'joshua -Bperson-', 'josh -Bperson-',
			'noah -Bperson-', 'ethan -Bperson-', 'joseph -Bperson-', 'samuel -Bperson-', 'daniel -Bperson-', 'max -Bperson-',
			'logan -Bperson-', 'isaac -Bperson-', 'dylan -Bperson-', 'freddie -Bperson-', 'tyler -Bperson-', 'harrison -Bperson-',
			'adam -Bperson-', 'theo -Bperson-', 'arthur -Bperson-', 'toby -Bperson-', 'luke -Bperson-', 'lewis -Bperson-',
			'matthew -Bperson-', 'harvey -Bperson-', 'ryan -Bperson-', 'tommy -Bperson-', 'michael -Bperson-', 'nathan -Bperson-',
			'blake -Bperson-', 'charles -Bperson-', 'connor -Bperson-', 'jamie -Bperson-', 'elliot -Bperson-', 'louis -Bperson-',
			'aaron -Bperson-', 'evan -Bperson-', 'seth -Bperson-']


what_to_tell_about = ['name -Bwhat_to_tell-', 'nationality -Bwhat_to_tell-', 'eyecolor -Bwhat_to_tell-', 'haircolor -Bwhat_to_tell-',
					'surname -Bwhat_to_tell-', 'middle -Bwhat_to_tell- name -Iwhat_to_tell-', 'gender -Bwhat_to_tell-', 'pose -Bwhat_to_tell-',
					'age -Bwhat_to_tell-', 'job -Bwhat_to_tell-' 'shirt color -Iwhat_to_tell-', 'height -Bwhat_to_tell-', 'mood -Bwhat_to_tell-']
what_to_tell_to = [ "your team's -Bwhat_to_tell- affiliation -Iwhat_to_tell-", "your team's -Bwhat_to_tell- name -Iwhat_to_tell-",
					'the day -Bwhat_to_tell- of-', 'what -Bwhat_to_tell- day -Iwhat_to_tell -i -Iwhat_to_tell- tommorow -Iwhat_to_tell-',
					'the time -Bwhat_to_tell-', 'the weather -Bwhat_to_tell-',  'that -Bwhat_to_tell- I am coming',
					'to -Bwhat_to_tell- wait -Iwhat_to_tell- a -Iwhat_to_tell- moment -Iwhat_to_tell-',
					'to -Bwhat_to_tell- wait -Iwhat_to_tell- a  -Iwhat_to_tell- bit -Iwhat_to_tell-', 'to -Bwhat_to_tell- come -Iwhat_to_tell- here -Iwhat_to_tell-']

tasks = []
tasks_take = []
tasks_follow = []
tasks_answer = []
tasks_find = []
tasks_guide = []
tasks_tell = []
tasks = []
tasks_take = []
tasks_follow = []
tasks_answer = []
tasks_find = []
tasks_guide = []
tasks_tell = []
tasks_go = []
tasks_grasp = []
tasks_meet = []

#------------------------------------------GO----------------------------------------------

for l in range(9000):

	for location in locations:

		location = location.replace('location', 'destination')

		task = 'go to the ' + location

		tasks_go.append(task)

		task = 'move to the ' + location

		tasks_go.append(task)		


#----------------------------------------GRASP---------------------------------------------

for objet in objects_a:

	task = 'grasp a ' + objet

	tasks_grasp.append(task)

	task = 'pick a ' + objet

	tasks_grasp.append(task)

	task = 'pick up a ' + objet

	tasks_grasp.append(task)


	for location in locations:

		location = location.replace('location', 'destination')

		task = 'grasp a ' + objet + ' at the ' + location

		tasks_grasp.append(task)

		task = 'pick a ' + objet + ' at the ' + location

		tasks_grasp.append(task)

		task = 'pick up a ' + objet + ' at the ' + location

		tasks_grasp.append(task)


for objet in objects_an:

	task = 'grasp an ' + objet

	tasks_grasp.append(task)

	task = 'pick an ' + objet

	tasks_grasp.append(task)

	task = 'pick up an ' + objet

	tasks_grasp.append(task)


	for location in locations:

		location = location.replace('location', 'destination')

		task = 'grasp an ' + objet + ' at the ' + location

		tasks_grasp.append(task)

		task = 'pick an ' + objet + ' at the ' + location

		tasks_grasp.append(task)

		task = 'pick up an ' + objet + ' at the ' + location

		tasks_grasp.append(task)


for objet in objects_the:

	task = 'grasp the ' + objet

	tasks_grasp.append(task)

	task = 'pick the ' + objet

	tasks_grasp.append(task)

	task = 'pick up the ' + objet

	tasks_grasp.append(task)


	for location in locations:

		location = location.replace('location', 'destination')

		task = 'grasp the ' + objet + ' at the ' + location

		tasks_grasp.append(task)

		task = 'pick the ' + objet + ' at the ' + location

		tasks_grasp.append(task)

		task = 'pick up the ' + objet + ' at the ' + location

		tasks_grasp.append(task)


for objet in objects_some:

	task = 'grasp some ' + objet

	tasks_grasp.append(task)

	task = 'pick some ' + objet

	tasks_grasp.append(task)

	task = 'pick up some ' + objet

	tasks_grasp.append(task)


	for location in locations:

		location = location.replace('location', 'destination')

		task = 'grasp some ' + objet + ' at the ' + location

		tasks_grasp.append(task)

		task = 'pick some ' + objet + ' at the ' + location

		tasks_grasp.append(task)

		task = 'pick up some ' + objet + ' at the ' + location

		tasks_grasp.append(task)


for objet in objects_a_bottle_of:

	task = 'grasp a bottle of ' + objet

	tasks_grasp.append(task)

	task = 'pick a bottle of ' + objet

	tasks_grasp.append(task)

	task = 'pick up a bottle of ' + objet

	tasks_grasp.append(task)


	for location in locations:

		location = location.replace('location', 'destination')

		task = 'grasp a bottle of ' + objet + ' at the ' + location

		tasks_grasp.append(task)

		task = 'pick a bottle of ' + objet + ' at the ' + location

		tasks_grasp.append(task)

		task = 'pick up a bottle of ' + objet + ' at the ' + location

		tasks_grasp.append(task)


for objet in objects_a_glass_of:

	task = 'grasp a glass of ' + objet

	tasks_grasp.append(task)

	task = 'pick a glass of ' + objet

	tasks_grasp.append(task)

	task = 'pick up a glass of ' + objet

	tasks_grasp.append(task)


	for location in locations:

		location = location.replace('location', 'destination')

		task = 'grasp a glass of ' + objet + ' at the ' + location

		tasks_grasp.append(task)

		task = 'pick a glass of ' + objet + ' at the ' + location

		tasks_grasp.append(task)

		task = 'pick up a glass of ' + objet + ' at the ' + location

		tasks_grasp.append(task)


for objet in objects_a_can_of:

	task = 'grasp a can of ' + objet

	tasks_grasp.append(task)

	task = 'pick a can of ' + objet

	tasks_grasp.append(task)

	task = 'pick up a can of ' + objet

	tasks_grasp.append(task)


	for location in locations:

		location = location.replace('location', 'destination')

		task = 'grasp a can of ' + objet + ' at the ' + location

		tasks_grasp.append(task)

		task = 'pick a can of ' + objet + ' at the ' + location

		tasks_grasp.append(task)

		task = 'pick up a can of ' + objet + ' at the ' + location

		tasks_grasp.append(task)


for objet in objects_a_cup_of:

	task = 'grasp a cup of ' + objet

	tasks_grasp.append(task)

	task = 'pick a cup of ' + objet

	tasks_grasp.append(task)

	task = 'pick up a cup of ' + objet

	tasks_grasp.append(task)


	for location in locations:

		location = location.replace('location', 'destination')

		task = 'grasp a cup of ' + objet + ' at the ' + location

		tasks_grasp.append(task)

		task = 'pick a cup of ' + objet + ' at the ' + location

		tasks_grasp.append(task)

		task = 'pick up a cup of ' + objet + ' at the ' + location

		tasks_grasp.append(task)


for objet in objects_a_piece_of:

	task = 'grasp a piece of ' + objet

	tasks_grasp.append(task)

	task = 'pick a piece of ' + objet

	tasks_grasp.append(task)

	task = 'pick up a piece of ' + objet

	tasks_grasp.append(task)


	for location in locations:

		location = location.replace('location', 'destination')

		task = 'grasp a piece of ' + objet + ' at the ' + location

		tasks_grasp.append(task)

		task = 'pick a piece of ' + objet + ' at the ' + location

		tasks_grasp.append(task)

		task = 'pick up a piece of ' + objet + ' at the ' + location

		tasks_grasp.append(task)


#-----------------------------------------MEET---------------------------------------------
for l in range(10):

	for name in names_female:

		task = 'meet ' + name

		tasks_meet.append(task)

		for location in locations:

			location = location.replace('location', 'destination')

			task = 'meet ' + name + ' at the ' + location

			tasks_meet.append(task)


	for name in names_male:

		task = 'meet ' + name

		tasks_meet.append(task)

		for location in locations:

			location = location.replace('location', 'destination')

			task = 'meet ' + name + ' at the ' + location

			tasks_meet.append(task)

#-----------------------------------------TAKE---------------------------------------------

for objet in objects_a:

	task = 'bring me -Bperson- a ' + objet
	
	tasks_take.append(task)

	task = 'give me -Bperson- a ' + objet
	
	tasks_take.append(task)

	task = 'deliver me -Bperson- a ' + objet

	tasks_take.append(task)

	for location in locations:

		location = location.replace('location', 'destination')

		task = 'take a ' + objet + ' to the ' + location

		tasks_take.append(task)

		task = 'deliver a ' + objet + ' to the ' + location

		tasks_take.append(task)

		task = 'put a ' + objet + ' to the ' + location

		tasks_take.append(task)


	for name in names_female:

		task = 'take a ' + objet + ' to ' + name

		tasks_take.append(task)

		task = 'deliver a ' + objet + ' to ' + name
	
		tasks_take.append(task)

		task = 'give a ' + objet + ' to ' + name

		tasks_take.append(task)

	for name in names_male:

		task = 'take a ' + objet + ' to ' + name

		tasks_take.append(task)

		task = 'deliver a ' + objet + ' to ' + name
	
		tasks_take.append(task)

		task = 'give a ' + objet + ' to ' + name

		tasks_take.append(task)


for objet in objects_an:

	task = 'bring me -Bperson- an ' + objet
	
	tasks_take.append(task)

	task = 'give me -Bperson- an ' + objet
	
	tasks_take.append(task)

	task = 'deliver me -Bperson- an ' + objet
	
	tasks_take.append(task)

	for location in locations:

		location = location.replace('location', 'destination')

		task = 'take an ' + objet + ' to the ' + location

		tasks_take.append(task)		

		task = 'deliver an ' + objet + ' to the ' + location

		tasks_take.append(task)

		task = 'put an ' + objet + ' to the ' + location

		tasks_take.append(task)


	for name in names_female:

		task = 'take an ' + objet + ' to ' + name
	
		tasks_take.append(task)	

		task = 'deliver an ' + objet + ' to ' + name
	
		tasks_take.append(task)

		task = 'give an ' + objet + ' to ' + name

		tasks_take.append(task)

	for name in names_male:

		task = 'take an ' + objet + ' to ' + name

		tasks_take.append(task)

		task = 'deliver an ' + objet + ' to ' + name
	
		tasks_take.append(task)

		task = 'give an ' + objet + ' to ' + name

		tasks_take.append(task)


for objet in objects_some:

	task = 'bring me -Bperson- some ' + objet
	
	tasks_take.append(task)

	task = 'give me -Bperson- some ' + objet
	
	tasks_take.append(task)

	task = 'deliver me -Bperson- some ' + objet
	
	tasks_take.append(task)

	for location in locations:

		location = location.replace('location', 'destination')

		task = 'take some ' + objet + ' to the ' + location

		tasks_take.append(task)		

		task = 'deliver some ' + objet + ' to the ' + location

		tasks_take.append(task)

		task = 'put some ' + objet + ' to the ' + location

		tasks_take.append(task)


	for name in names_female:

		task = 'take some ' + objet + ' to ' + name
	
		tasks_take.append(task)	

		task = 'deliver some ' + objet + ' to ' + name
	
		tasks_take.append(task)

		task = 'give some ' + objet + ' to ' + name

		tasks_take.append(task)

	for name in names_male:

		task = 'take some ' + objet + ' to ' + name

		tasks_take.append(task)

		task = 'deliver some ' + objet + ' to ' + name
	
		tasks_take.append(task)

		task = 'give some ' + objet + ' to ' + name

		tasks_take.append(task)


for objet in objects_the:

	task = 'bring me -Bperson- the ' + objet
	
	tasks_take.append(task)

	task = 'give me -Bperson- the ' + objet
	
	tasks_take.append(task)

	task = 'deliver me -Bperson- the ' + objet
	
	tasks_take.append(task)

	for location in locations:

		location = location.replace('location', 'destination')

		task = 'take the ' + objet + ' to the ' + location

		tasks_take.append(task)		

		task = 'deliver the ' + objet + ' to the ' + location

		tasks_take.append(task)

		task = 'put the ' + objet + ' to the ' + location

		tasks_take.append(task)


	for name in names_female:

		task = 'take the ' + objet + ' to ' + name
	
		tasks_take.append(task)	

		task = 'deliver the ' + objet + ' to ' + name
	
		tasks_take.append(task)

		task = 'give the ' + objet + ' to ' + name

		tasks_take.append(task)

	for name in names_male:

		task = 'take the ' + objet + ' to ' + name

		tasks_take.append(task)

		task = 'deliver the ' + objet + ' to ' + name
	
		tasks_take.append(task)

		task = 'give the ' + objet + ' to ' + name

		tasks_take.append(task)


for objet in objects_a_bottle_of:

	task = 'bring me -Bperson- a bottle of ' + objet
	
	tasks_take.append(task)

	task = 'give me -Bperson- a bottle of ' + objet
	
	tasks_take.append(task)

	task = 'deliver me -Bperson- a bottle of ' + objet
	
	tasks_take.append(task)

	for location in locations:

		location = location.replace('location', 'destination')

		task = 'take a bottle of ' + objet + ' to the ' + location

		tasks_take.append(task)		

		task = 'deliver a bottle of ' + objet + ' to the ' + location

		tasks_take.append(task)

		task = 'put a bottle of ' + objet + ' to the ' + location

		tasks_take.append(task)


	for name in names_female:

		task = 'take a bottle of ' + objet + ' to ' + name
	
		tasks_take.append(task)	

		task = 'deliver a bottle of ' + objet + ' to ' + name
	
		tasks_take.append(task)

		task = 'give a bottle of ' + objet + ' to ' + name

		tasks_take.append(task)

	for name in names_male:

		task = 'take a bottle of ' + objet + ' to ' + name

		tasks_take.append(task)

		task = 'deliver a bottle of ' + objet + ' to ' + name
	
		tasks_take.append(task)

		task = 'give a bottle of ' + objet + ' to ' + name

		tasks_take.append(task)


for objet in objects_a_glass_of:

	task = 'bring me -Bperson- a glass of ' + objet
	
	tasks_take.append(task)

	task = 'give me -Bperson- a glass of ' + objet
	
	tasks_take.append(task)

	task = 'deliver me -Bperson- a glass of ' + objet
	
	tasks_take.append(task)

	for location in locations:

		location = location.replace('location', 'destination')

		task = 'take a glass of ' + objet + ' to the ' + location

		tasks_take.append(task)		

		task = 'deliver a glass of ' + objet + ' to the ' + location

		tasks_take.append(task)

		task = 'put a glass of ' + objet + ' to the ' + location

		tasks_take.append(task)


	for name in names_female:

		task = 'take a glass of ' + objet + ' to ' + name
	
		tasks_take.append(task)	

		task = 'deliver a glass of ' + objet + ' to ' + name
	
		tasks_take.append(task)

		task = 'give a glass of ' + objet + ' to ' + name

		tasks_take.append(task)

	for name in names_male:

		task = 'take a glass of ' + objet + ' to ' + name

		tasks_take.append(task)

		task = 'deliver a glass of ' + objet + ' to ' + name
	
		tasks_take.append(task)

		task = 'give a glass of ' + objet + ' to ' + name

		tasks_take.append(task)


for objet in objects_a_can_of:

	task = 'bring me -Bperson- a can of ' + objet
	
	tasks_take.append(task)

	task = 'give me -Bperson- a can of ' + objet
	
	tasks_take.append(task)

	task = 'deliver me -Bperson- a can of ' + objet
	
	tasks_take.append(task)

	for location in locations:

		location = location.replace('location', 'destination')

		task = 'take a can of ' + objet + ' to the ' + location

		tasks_take.append(task)		

		task = 'deliver a can of ' + objet + ' to the ' + location

		tasks_take.append(task)

		task = 'put a can of ' + objet + ' to the ' + location

		tasks_take.append(task)


	for name in names_female:

		task = 'take a can of ' + objet + ' to ' + name
	
		tasks_take.append(task)	

		task = 'deliver a can of ' + objet + ' to ' + name
	
		tasks_take.append(task)

		task = 'give a can of ' + objet + ' to ' + name

		tasks_take.append(task)

	for name in names_male:

		task = 'take a can of ' + objet + ' to ' + name

		tasks_take.append(task)

		task = 'deliver a can of ' + objet + ' to ' + name
	
		tasks_take.append(task)

		task = 'give a can of ' + objet + ' to ' + name

		tasks_take.append(task)


for objet in objects_a_cup_of:

	task = 'bring me -Bperson- a cup of ' + objet
	
	tasks_take.append(task)

	task = 'give me -Bperson- a cup of ' + objet
	
	tasks_take.append(task)

	task = 'deliver me -Bperson- a cup of ' + objet
	
	tasks_take.append(task)

	for location in locations:

		location = location.replace('location', 'destination')

		task = 'take a cup of ' + objet + ' to the ' + location

		tasks_take.append(task)		

		task = 'deliver a cup of ' + objet + ' to the ' + location

		tasks_take.append(task)

		task = 'put a cup of ' + objet + ' to the ' + location

		tasks_take.append(task)


	for name in names_female:

		task = 'take a cup of ' + objet + ' to ' + name
	
		tasks_take.append(task)	

		task = 'deliver a cup of ' + objet + ' to ' + name
	
		tasks_take.append(task)

		task = 'give a cup of ' + objet + ' to ' + name

		tasks_take.append(task)

	for name in names_male:

		task = 'take a cup of ' + objet + ' to ' + name

		tasks_take.append(task)

		task = 'deliver a cup of ' + objet + ' to ' + name
	
		tasks_take.append(task)

		task = 'give a cup of ' + objet + ' to ' + name

		tasks_take.append(task)


#-----------------------------------------FOLLOW---------------------------------------------
for l in range(60):

	for name in names_male:

		task = 'follow me -Bperson'

		tasks_follow.append(task)

		task = 'follow ' + name

		tasks_follow.append(task)

		task = 'go after ' + name

		tasks_follow.append(task)

		task = 'come after ' + name

		tasks_follow.append(task)

		task = 'go with ' + name

		tasks_follow.append(task)


	for name in names_female:

		task = 'follow ' + name

		tasks_follow.append(task)

		task = 'go after ' + name

		tasks_follow.append(task)

		task = 'come after ' + name

		tasks_follow.append(task)

		task = 'go with ' + name

		tasks_follow.append(task)


#.......................................GUIDE-----------------------------------------------

for name in names_male:

	for location in locations:

		location = location.replace('location', 'destination')

		task = 'guide ' + name + ' to the ' + location

		tasks_guide.append(task)

		task = 'accompany ' + name + ' to the ' + location

		tasks_guide.append(task)

		task = 'take ' + name + ' to the ' + location

		tasks_guide.append(task)		

		for location2 in locations:

			location2 = location2.replace('location', 'source')

			task = 'guide ' + name + ' from the ' + location2 + ' to the ' + location

			tasks_guide.append(task)

			task = 'accompany ' + name + ' from the ' + location2 + ' to the ' + location

			tasks_guide.append(task)

			task = 'take ' + name +  ' from the ' + location2 + ' to the ' + location

			tasks_guide.append(task)	


for name in names_female:

	for location in locations:

		location = location.replace('location', 'destination')

		task = 'guide ' + name + ' to the ' + location

		tasks_guide.append(task)

		task = 'accompany ' + name + ' to the ' + location

		tasks_guide.append(task)

		task = 'take ' + name + ' to the ' + location

		tasks_guide.append(task)	

		for location2 in locations:

			location2 = location2.replace('location', 'source')

			task = 'guide ' + name + ' from the ' + location2 + ' to the ' + location

			tasks_guide.append(task)

			task = 'accompany ' + name + ' from the ' + location2 + ' to the ' + location

			tasks_guide.append(task)

			task = 'take ' + name +  ' from the ' + location2 + ' to the ' + location

			tasks_guide.append(task)	


#.......................................FIND-----------------------------------------------


for objet in objects_a:

	for location in locations:

		location = location.replace('location', 'destination')

		task = 'find a ' + objet + ' in the ' + location

		tasks_find.append(task)

		task = 'look for a ' + objet + ' in the ' + location

		tasks_find.append(task)

		task = 'locate a ' + objet + ' in the ' + location

		tasks_find.append(task)

		task = 'find a ' + objet + ' at the ' + location

		tasks_find.append(task)

		task = 'look for a ' + objet + ' at the ' + location

		tasks_find.append(task)

		task = 'locate a ' + objet + ' at the ' + location

		tasks_find.append(task)


for objet in objects_the:

	for location in locations:

		location = location.replace('location', 'destination')

		task = 'find the ' + objet + ' in the ' + location

		tasks_find.append(task)

		task = 'look for the ' + objet + ' in the ' + location

		tasks_find.append(task)

		task = 'locate the ' + objet + ' in the ' + location

		tasks_find.append(task)

		task = 'find the ' + objet + ' at the ' + location

		tasks_find.append(task)

		task = 'look for the ' + objet + ' at the ' + location

		tasks_find.append(task)

		task = 'locate the ' + objet + ' at the ' + location

		tasks_find.append(task)


for objet in objects_an:

	for location in locations:

		location = location.replace('location', 'destination')

		task = 'find an ' + objet + ' in the ' + location

		tasks_find.append(task)

		task = 'look for an ' + objet + ' in the ' + location

		tasks_find.append(task)

		task = 'locate an ' + objet + ' in the ' + location

		tasks_find.append(task)

		task = 'find an ' + objet + ' at the ' + location

		tasks_find.append(task)

		task = 'look for an ' + objet + ' at the ' + location

		tasks_find.append(task)

		task = 'locate an ' + objet + ' at the ' + location

		tasks_find.append(task)


for objet in objects_some:

	for location in locations:

		location = location.replace('location', 'destination')

		task = 'find some ' + objet + ' in the ' + location

		tasks_find.append(task)

		task = 'look for some ' + objet + ' in the ' + location

		tasks_find.append(task)

		task = 'locate some ' + objet + ' in the ' + location

		tasks_find.append(task)

		task = 'find some ' + objet + ' at the ' + location

		tasks_find.append(task)

		task = 'look for some ' + objet + ' at the ' + location

		tasks_find.append(task)

		task = 'locate some ' + objet + ' at the ' + location

		tasks_find.append(task)


for objet in objects_a_cup_of:

	for location in locations:

		location = location.replace('location', 'destination')

		task = 'find a cup of ' + objet + ' in the ' + location

		tasks_find.append(task)

		task = 'look for a cup of ' + objet + ' in the ' + location

		tasks_find.append(task)

		task = 'locate a cup of ' + objet + ' in the ' + location

		tasks_find.append(task)	

		task = 'find a cup of ' + objet + ' at the ' + location

		tasks_find.append(task)

		task = 'look for a cup of ' + objet + ' at the ' + location

		tasks_find.append(task)

		task = 'locate a cup of ' + objet + ' at the ' + location

		tasks_find.append(task)


for objet in objects_a_can_of:

	for location in locations:

		location = location.replace('location', 'destination')

		task = 'find a can of ' + objet + ' in the ' + location

		tasks_find.append(task)

		task = 'look for a can of ' + objet + ' in the ' + location

		tasks_find.append(task)

		task = 'locate a can of ' + objet + ' in the ' + location

		tasks_find.append(task)

		task = 'find a can of ' + objet + ' at the ' + location 

		tasks_find.append(task)

		task = 'look for a can of ' + objet + ' at the ' + location

		tasks_find.append(task)

		task = 'locate a can of ' + objet + ' at the ' + location

		tasks_find.append(task)


for objet in objects_a_glass_of:

	for location in locations:

		location = location.replace('location', 'destination')

		task = 'find a glass of ' + objet + ' in the ' + location

		tasks_find.append(task)

		task = 'look for a glass of ' + objet + ' in the ' + location

		tasks_find.append(task)

		task = 'locate a glass of' + objet + ' in the ' + location

		tasks_find.append(task)

		task = 'find a glass of ' + objet + ' at the ' + location

		tasks_find.append(task)

		task = 'look for a glass of ' + objet + ' at the ' + location

		tasks_find.append(task)

		task = 'locate a glass of ' + objet + ' at the ' + location

		tasks_find.append(task)


for objet in objects_a_bottle_of:

	for location in locations:

		location = location.replace('location', 'destination')

		task = 'find a bottle of ' + objet + ' in the ' + location

		tasks_find.append(task)

		task = 'look for a bottle of ' + objet + ' in the ' + location

		tasks_find.append(task)

		task = 'locate a bottle of ' + objet + ' in the ' + location

		tasks_find.append(task)

		task = 'find a bottle of ' + objet + ' at the ' + location

		tasks_find.append(task)

		task = 'look for a bottle of ' + objet + ' at the ' + location

		tasks_find.append(task)

		task = 'locate a bottle of ' + objet + ' at the ' + location

		tasks_find.append(task)



#--------------------------------------------ANSWER-------------------------------------
for l in range(20):

	for name in names_male:

		task = 'answer a question to ' + name

		tasks_answer.append(task)

		task = 'answer to ' + name

		tasks_answer.append(task)


		for location in locations:

			location = location.replace('location', 'destination')

			task = 'answer a question to ' + name + ' at the ' + location

			tasks_answer.append(task)

			task = 'answer to ' + name + ' at the ' + location

			tasks_answer.append(task)
			

	for name in names_female:

		task = 'answer a question to ' + name

		tasks_answer.append(task)

		for location in locations:

			location = location.replace('location', 'destination')

			task = 'answer a question to ' + name + ' at the ' + location

			tasks_answer.append(task)

			task = 'answer to ' + name + ' at the ' + location

			tasks_answer.append(task)

	for location in locations:

			location = location.replace('location', 'destination')

			task = 'answer a question to the person at the ' + location

			tasks_answer.append(task)

			task = 'answer a question to someone at the ' + location

			tasks_answer.append(task)

			task = 'answer a question to anyone at the ' + location

			tasks_answer.append(task)

			task = 'answer to the person at the ' + location

			tasks_answer.append(task)

			task = 'answe to someone at the ' + location

			tasks_answer.append(task)

			task = 'answer to anyone at the ' + location

			tasks_answer.append(task)


#---------------------------------------------TELL-------------------------------------

for w in what_to_tell_to:
	
	for name in names_female:

		task = 'tell ' + w + ' to ' + name

		tasks_tell.append(task)

		for location in locations:

			location = location.replace('location', 'destination')

			task = 'tell ' + w + ' to ' + name + ' at the ' + location

			tasks_tell.append(task)


	for name in names_male:

		task = 'tell ' + w + ' to ' + name

		tasks_tell.append(task)

		for location in locations:

			location = location.replace('location', 'destination')

			task = 'tell ' + w + ' to ' + name + ' at the ' + location

			tasks_tell.append(task)


for w in what_to_tell_about:

	for name in names_male:

		task = 'tell me -Bperson- ' + w + ' of ' + name

		tasks_tell.append(task)

	for name in names_female:

		task = 'tell me -Bperson- ' + w + ' of ' + name

		tasks_tell.append(task)

	for name in names_male:

		task = 'tell me -Bperson- ' + w + ' of ' + name

		tasks_tell.append(task)

	for name in names_female:

		task = 'tell me -Bperson- ' + w + ' of ' + name

		tasks_tell.append(task)

sentences = []
outputs = []


for i in range(18000):

	task = tasks_tell[i]

	tasks.append(task)

	task = tasks_take[i]

	tasks.append(task)

	task = tasks_find[i]

	tasks.append(task)
	
	task = tasks_follow[i]

	tasks.append(task)
	
	task = tasks_answer[i]

	tasks.append(task)

	task = tasks_guide[i]

	tasks.append(task)

	task = tasks_go[i]

	tasks.append(task)

	task = tasks_meet[i]

	tasks.append(task)

	task = tasks_grasp[i]

	tasks.append(task)

random.shuffle(tasks)

for v in range(100000):	

	task = tasks[v].split(' ')

	sentence = []
	output = []

	for h in range(len(task)):
		if not task[h].startswith('-'):
			sentence.append(task[h])
			if h < len(task)-1:
				if task[h+1].startswith('-'):
					l = task[h+1]
					l = l.replace('-', '')
					output.append(l)
				else:
					output.append('O')
			else:
				output.append('O')

	sentences.append(sentence)

	outputs.append(output)

with open('inputs_slot_filling', 'wb') as inputs_file:
	pickle.dump(sentences, inputs_file)

with open('outputs_slot_filling', 'wb') as outputs_file:
	pickle.dump(outputs, outputs_file)	

print(len(sentences))