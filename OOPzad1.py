import statistics


class student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_passed(self, name, marks):
        if statistics.mean(marks) > 50:
            return True
        else:
            return False


adam = student('Adam', [50, 55, 60])
tomasz = student('Tomasz', [40, 30, 45])

print(adam.is_passed(adam.name, adam.marks))
print(tomasz.is_passed(tomasz.name, tomasz.marks))
