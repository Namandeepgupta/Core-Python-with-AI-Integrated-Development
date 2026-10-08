class Enrollment:

    def __init__(self, n, d, p):
        self.name = n
        self.dob = d
        self.place = p
        print(f'Emp {self.name} enrollment is done')

    def display(self):
        print(f'About {self.name} detials :- ')
        print(f'Name : {self.name} DOB : {self.dob} Place : {self.place}')
        
obj1 = Enrollment('Namandeep','25th Nov','Gorakhpur')

obj2 = Enrollment('Harsh','2nd Sep','Bengalore')

obj1.display()
obj2.display()