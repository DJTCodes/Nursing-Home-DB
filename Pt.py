class Pt:
    def __init__(self, pt_id, last_name, first_name, social_num, ward_num):
        self.pt_id = pt_id
        self.last_name = last_name
        self.first_name = first_name
        self.social_num = social_num
        self.ward_num = ward_num

    def print_self(self):
        string = self.pt_id + ' ' + self.last_name + ' ' \
            + self.first_name + ' ' + self.social_num + ' ' + self.ward_num
        print(string)
