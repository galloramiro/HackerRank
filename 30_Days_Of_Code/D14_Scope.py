class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = 0                                  # El valor final lo dejo en el init

    def computeDifference(self):                                    
        min_element = 101                                           # Establezco los número limitantes 
        max_element = 0
        for element in self.__elements:                             # Para cada número en la lista le pido que lo compare y lo agregue
            if element < min_element:
                min_element = element
            if element > max_element:
                max_element = element

        self.maximumDifference = max_element - min_element          # Modifico el valor de init con el resultado. 

