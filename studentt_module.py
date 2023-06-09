
class Studentt:
    num_of_stds = 0
    def __init__(self, name, age, city):
        self.marks = []
        self.st_sum = 0
        self.name = name
        self.age = age
        self.city = city
        Studentt.num_of_stds +=1

        #عملت مصفوفة عشان اخزن فيها العلامات قد ما بدي بدون ما تنحذف اي علامة في ال override

    def add_mark(self, mark):
       self.marks.append(mark)
       self.st_sum += mark

    def get_all_marks(self):
        for mark in self.marks:
            print(f'mark = {mark}')

    def calculate_avg(self):
        if len(self.marks)==0:
            print('there are no marks')
            return -1

        st_avg = self.st_sum/len(self.marks)
        return st_avg

st1 = Studentt("samah", "gaza", 19)
print(st1.name)
print(st1.age)
print(st1.city)
st1.add_mark(90)
st1.add_mark(80)
st1.add_mark(75)
st1.get_all_marks()
print(Studentt.num_of_stds)


