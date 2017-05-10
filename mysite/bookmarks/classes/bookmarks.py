class Bookmarks(object):
    def __init__(self, student_owner):
        self.student_owner = student_owner
        self.list_marks = []

    def __str__(self):
        return "OWNER: {}".format(self.student_owner)

    def __repr__(self):
        return self.__str__()

    def add_mark(self, n):
        return self.list_marks.append(n)
