class Table:
    name = "Имя"
    dept = "Кафедра"
    role = "Преподаватель"

    # конструктор
    def __init__(self, _name = "Имя", _dept = "Кафедра", _role = "Должность"):
        self.name = _name
        self.dept = _dept
        self.role = _role

    # получение строки
    def __str__(self):
        return '%s, %s, %s' % (self.name, self.dept, self.role)

    # деструктор
    def __del__(self):
        pass

    # получение словаря
    def get_dict(self):
        return {'name': self.name, 'dept': self.dept, 'role': self.role}
