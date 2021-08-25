import mysql.connector
import random
from generators import generate_staff
from generators import generate_pt
from generators import generate_treatment

#main def
def main():
    try:
        db = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = 'linkss',
        database = 'nursing_home2'
    )
    except Error as e:
        print(f"The error '{e}' has occurred.")

    mycursor = db.cursor()

    staff = generate_staff(25)
    pt = generate_pt(50)
    treatment = generate_treatment(10)
    rn_ids = []
    md_ids = []
    pt_ids = []

    for i in staff:
        #populate staff
        sql = "INSERT INTO staff VALUES (%s, %s, %s, %s, %s)"
        val = (i.staff_id, i.last_name, i.first_name, i.job_title, i.wardnum)
        mycursor.execute(sql, val)
        #populate subtables
        if i.job_title == 'MD':
            sql = "INSERT INTO md VALUES (%s)"
            val = i.staff_id
            mycursor.execute(sql,(val,))
            md_ids.append(i.staff_id)
        if i.job_title == 'RN':
            sql = "INSERT INTO rn VALUES (%s)"
            val = i.staff_id
            mycursor.execute(sql,(val,))
            rn_ids.append(i.staff_id)
        if i.job_title == 'CNA':
            sql = "INSERT INTO cna VALUES (%s)"
            val = i.staff_id
            mycursor.execute(sql, (val,))
    print("Staff tuples successfully inserted")

    for i in pt:
        sql = "INSERT INTO pt VALUES (%s, %s, %s, %s, %s)"
        val = (i.pt_id, i.last_name, i.first_name, i.social_num, i.ward_num)
        mycursor.execute(sql, val)
        pt_ids.append(i.pt_id)
    print("Patient tuples successfully inserted")

    for i in treatment:
        sql = "INSERT INTO treatment (name, time_administered, rn_id, md_id,\
             pt_id) VALUES (%s, %s, %s, %s, %s)"
        val = (i.name, i.time_administered, random.choice(rn_ids),\
             random.choice(md_ids), random.choice(pt_ids))
        mycursor.execute(sql, val)
    print("Treatment tuples successfully inserted")

    db.commit()


#init run main
if __name__ == "__main__":
   main()