class Student :
    def __init__(self, name, hometown, age, height, favourite_icecream_flavour):
        self.name=name
        self.hometown=hometown
        self.age=age
        self.height=height
        self.favourite_icecream_flavour=favourite_icecream_flavour
    def print_summary(self):
        print(" student info: name - " + str(self.name) + " hometown - " + str(self.hometown) +
              " age - " + str(self.age) + " height - " + str(self.height) + " favourite_icecream_flavour - " + str(self.favourite_icecream_flavour))
    def get_giraffe_gap(self):
        return 500-float(self.height)
    
