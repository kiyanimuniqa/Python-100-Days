class employe:
    def __init__(self,name,id):
        self.name = name
        self.id = id
    def show_details(self):
        print(f"The name of employe is: {self.name} and its ID is {self.id}")
employe1 = employe("muniqa",47767)
employe1.show_details()