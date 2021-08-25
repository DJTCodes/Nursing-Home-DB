class Staff:
    def __init__(self, staff_id, last_name, first_name, job_title, wardnum):
        self.staff_id = staff_id
        self.last_name = last_name
        self.first_name = first_name
        self.job_title = job_title
        self.wardnum = wardnum

    def print_self(self):
        string = self.staff_id + ' ' + self.firstname + ' ' \
            + self.lastname + ' ' + self.job + ' ' + self.wardnum
        print(string)

