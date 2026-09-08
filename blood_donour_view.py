import pymysql
import datetime

class BloodDonorManager:
    def __init__(self):

        self.connection=pymysql.connect(
            host="localhost",
            user="root",
            password="Luminar@1234",
            database="blood_db"
        )

        print("Connected")


    def post(self,**kwargs):
        try:
            self.cursor=self.connection.cursor()

            query="insert into donor(name,blood_group,phone,city,last_donation) values(%s,%s,%s,%s,%s)"

            values=[v for v in kwargs.values()]
            self.cursor.execute(query,values)
            self.connection.commit()
            print("Donor added successfully")

        except Exception as e:
            print(e)

    def get(self):
        try:
            self.cursor=self.connection.cursor()
            query="select * from donor"
            self.cursor.execute(query)
            records=self.cursor.fetchall()
            for data in records:
                print(data)
        except Exception as e:
            print(e)

    def retrieve(self,id=None):       # default arg-id
        try:
            self.cursor=self.connection.cursor()
            query="select * from donor where id=%s"

            values=(id,)

            self.cursor.execute(query,values)
            record=self.cursor.fetchone()
            print(record)
        except Exception as e:
            print(e)

    def delete(self,id=None):
        try:
            self.cursor=self.connection.cursor()
            query="select * from donor where id=%s"
            values=(id,)
            self.cursor.execute(query,values)

            record=self.cursor.fetchone()
            if record != None:
                query="delete from donor where id=%s"
                self.cursor.execute(query,values)
                self.connection.commit()
                print("donor deleted")
            else:
                print("donor not found")

        except Exception as e:
            print(e)


donor_instance=BloodDonorManager()      #creating an object.No meed to call an obj as its already inside constructor

# donor_instance.post(name="Surya",blood_group="AB+",phone="945697983",city="Kochi",last_donation=datetime.datetime.today())
# donor_instance.post(name="Ann",blood_group="A+",phone="949794567",city="Kaloor",last_donation=datetime.datetime.today())
# donor_instance.post(name="Athira",blood_group="B+",phone="7736860528",city="Tvm",last_donation=datetime.datetime.today())

donor_instance.get()

print("------------Retreive using id--------------")

donor_instance.retrieve(id=10)

print("-----------delete operation-------------")
donor_instance.delete(id=7)
donor_instance.get()
