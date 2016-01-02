class Parent():
    def __init__(self, last_name, eye_color):
        print("I made some shit up here about parent construction")
        self.last_name = last_name
        self.eye_color = eye_color

    def show_info(self):
        print("Last Name - " + self.last_name)
        print("Hair Color - " + self.eye_color)


class Child(Parent):
    def __init__(self, last_name, eye_color, number_of_toys):
        print("Child shit I made up here")
        Parent.__init__(self, last_name, eye_color)
        self.number_of_toys = number_of_toys 


billy_borzo = Parent("Euba", "paisley")
billy_borzo.show_info()
juba_borzo = Child("Euba", "electric blue", "5")
juba_borzo.show_info()
