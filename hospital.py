class patient(object):
	def __init__(self, ids, name, allergies):
		print "adding patient"
		self.ids=ids
		self.name=name
		self.allergies= allergies
		self.bed_number=0
		

class hospital(object):
	def __init__(self, hospital_name):
		self.patients=[]
		self.hospital_name=hospital_name
		self.capacity=0
	def admit(self, x):
		if len(self.patients)>10:
			print "Hospital is full"
		else:
			self.patients.append(x)
			self.capacity+=1
			self.bed_number=+1
			print "Admission is complete"
		return self
	def display(self):
		print self.hospital_name, "has a capacity of ",
		print self.capacity

	def discharge(self,y):
		self.patient.pop(y)
		self.bed_number="none"


patient1= patient("1","Andy","Peanuts")
patient2= patient("2","Jontathan","Peanuts")
patient3= patient("3","Nathan","Peanuts")
patient4= patient("4","Andie","Peanuts")
patient5= patient("5","Andy","Peanuts")
patient6= patient("6","Jontathan","Peanuts")
patient7= patient("7","Nathan","Peanuts")
patient8= patient("8","Andie","Peanuts")
patient9= patient("9","Andy","Peanuts")
patient10= patient("10","Jontathan","Peanuts")
patient11= patient("11","Nathan","Peanuts")
patient12= patient("12","Andie","Peanuts")

testhospital=hospital("Oconnor")

testhospital.admit(patient1).admit(patient2).admit(patient3).admit(patient4).admit(patient5).admit(patient6).admit(patient7).admit(patient8).admit(patient9).admit(patient10).admit(patient11).display()