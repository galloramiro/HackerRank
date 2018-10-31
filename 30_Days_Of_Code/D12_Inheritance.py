class Person:                                                           # Clase madre
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)


class Student(Person):                                                  # Defino la nueva clase que hereda de Person
    def __init__(self,firstName, lastName, idNumber, scores):           
        Person.__init__(self, firstName, lastName, idNumber)            # Indico que los valores firstName, lastName e idNumber los va a tomar de person __init__
        self.scores = scores                                            #  y el score de lo que le pasen

    def calculate(self):                                                
        sum = 0                                                         # Declaro la variable para sumar los valores de score
        for score in scores:                                            
            sum += score                                                # Sumo cada valor a sum
        average = sum/len(scores)                                       # Saco el promedio

        if average < 40:                                                # Luego lo paso por el condicional para poder colocarlo. 
            return 'T'
        elif average < 55:
            return 'D'
        elif average < 70:
            return 'P'
        elif average < 80:
            return 'A'
        elif average < 90:
            return 'E'
        else:
            return 'O'