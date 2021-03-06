



''' Team class. Represents
	a programming team. Has
	a copy of the problems, and their
	times for solving them.
'''
class Team:
	index = 0
	def __init__(self, name, problems):
		self.name = name	 # Name of the team
		self.problems = problems # Array of problem names
		self.solved_count = 0
		self.time = 0
		self.solved = [-1] * len(problems)  # Time problem solved. -1 if not solved.
		self.tries = [0] * len(problems)

		# Get an index
		self.index = Team.index
		Team.index += 1

	def add_problem(self):
		self.solved.append(-1)
		self.tries.append(0)



''' Problem class. Represents
	a programming problem. 

	Contains the name and url for the problem,
	as well as other meta-data
'''
class Problem:
	def __init__(self, name, url):
		self.name = name
		self.url = url

