from faker import Faker
from Staff import Staff
from Pt import Pt
from Treatment import Treatment
import random
import uuid

def generate_staff(num_staff):
        jobs = ['CNA', 'MD', 'RN']
        fake = Faker()
        staff = []
        for i in range(num_staff):
            staff_id = str(uuid.uuid4())
            person = Staff(staff_id, fake.last_name(), fake.first_name(), \
            random.choice(jobs), str(random.randint(1, 5))) #ward num    
            staff.append(person)
        return staff

def generate_pt(num_pt):
        fake = Faker()
        pt = []
        for i in range(num_pt):
            pt_id = str(uuid.uuid4())
            patient = Pt(pt_id, fake.last_name(), fake.first_name(), \
            fake.ssn(), str(random.randint(1, 5)))     
            pt.append(patient)
        return pt

def generate_treatment(num_treatment):
    fake = Faker()
    drugs = ['Edrotriene', 'Doctosyn', 'Acitrepan', 'Accupion',\
    'Cure For Cancer', 'Pentodox Amiotrol', 'Limb Regeneration',\
    'MakeYoungAgainderall', 'Morphine' ]
    treatment = []
    for i in range(num_treatment):
        name = random.choice(drugs)
        time_administered = str(fake.date())
        drug = Treatment(name, time_administered)
        treatment.append(drug)
    return treatment
