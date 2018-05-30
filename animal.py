class animal(object):
	def __init__(self, name):
		self.name= name
		self.health= 0
		self.dragons= False
	def walk(self):
		self.health-=1
		print "walking...."
		return self
	def run(self):
		self.health-=5
		print "running....."
		return self
	def display_health(self):
		if self.dragons==True:
			print "i am a dragon"
		print self.health, "health"
class dog(animal):
	def __init__(self, name):
		super(dog, self).__init__(self)
		self.health=150
		self.dragons=False
	def animal_type(self):
		print self.health
		print "Dog"
	def pet(self):
		self.health+=5
		print "petting"
		return self
class dragon(animal):
	def __init__(self, name):
		super(dragon, self).__init__(self)
		self.health=170
		self.dragons=True
	def animal_type(self):
		print "dragon"
	def fly():
		health-=10
		return self
	def displayhealth(display_health):
		print "I am a dragon"
		return self

dog1 = dog("Bella")
dragon1 = dragon("Bello")
dog1.walk().walk().walk().run().run().display_health()


