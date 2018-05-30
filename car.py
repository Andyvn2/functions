class Car(object):
	def __init__(self, price,speed, fuel, mileage, tax):
		self.price= price
		self.speed=speed
		self.fuel= fuel
		self.mileage= mileage
		if tax>15000:
			self.tax= "%15"
		else:
			self.tax= "%12"

	def display_all(self):
		print "Price:$"+self.price, 
		print "Speed:"+self.speed, "Fuel:"+self.fuel, "Milage:"+self.mileage, "Tax:"+self.tax


car1= Car("17000", "520mph", "Not Full", "45mpg", 0)
car2= Car("12000", "10mph", "Full", "115mpg", 0)
car3= Car("11000", "80mph", "Full", "15mpg", 0)
car4= Car("19000", "40mph", "Not Full", "35mpg", 0)
car5= Car("15000", "50mph", "Full", "12mpg", 0)
car6= Car("9000", "20mph", "Not Full", "15mpg", 0)

car1.display_all()
car2.display_all()
car3.display_all()
car4.display_all()
car5.display_all()
car6.display_all()
