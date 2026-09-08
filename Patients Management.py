import pymysql
import datetime

class Patients_Management:
    def __init__(self):
        self.connection = pymysql.connect(
            host="localhost",
            user="root",
            password="Luminar@1234",
            database="patients_db"
        )

    def get_object(self,id=None):
        try:
            self.cursor=self.connection.cursor()
            query="select * from patients where id=%s"
            values=(id,)

            self.cursor.execute(query,values)
            record=self.cursor.fetchone()
            return record
        except Exception as e:
            return None


    def post(self,**kwargs):
        try:
            self.cursor=self.connection.cursor()

            query="insert into patients(name,gender,phone,city,date_today) values(%s,%s,%s,%s,%s)"
            values=[v for v in kwargs.values()]

            self.cursor.execute(query,values)
            self.connection.commit()
            print("Added..!")
        except Exception as e:
            print(e)

    def get(self):
        try:
            self.cursor=self.connection.cursor()
            query="select * from patients"
            self.cursor.execute(query)
            records=self.cursor.fetchall()
            for data in records:
                print(data)
        except Exception as e:
            print(e)

    def retrieve(self,id=None):
        try:
            self.cursor=self.connection.cursor()
            query="select * from patients where id=%s"
            values=(id,)
            self.cursor.execute(query,values)
            record=self.cursor.fetchone()

            if record:
                print(record)
            else:
                print("Not found")
        except Exception as e:
            print(e)


    def delete(self,id=None):
        try:
            record=self.get_object(id=id)
            values=(id,)

            if record!=None:
                query="delete from patients where id=%s"
                self.cursor.execute(query,values)
                self.connection.commit()
                print("Donor deleted")
            else:
                print("Donor not found")
        except Exception as e:
            print(e)

    def put(self,id=None,**kwargs):
        try:
            record=self.get_object(id=id)
            if record!=None:
                self.cursor=self.connection.cursor()
                placeholder=""
                for k in kwargs.keys():
                    placeholder+=k + "=%s, "

                placeholder=placeholder.rstrip(", ")

                query=f"update patients set {placeholder} where id=%s"
                values=[v for v in kwargs.values()]
                values.append(id)

                self.cursor.execute(query,values)
                self.connection.commit()

                print("Updated !")
            else:
                print("Patient not found")

        except Exception as e:
            print(e)

instance=Patients_Management()
# instance.post(name="lilly",gender="female",phone="364782374",city="Kochi",date_today=datetime.datetime.today())
# instance.post(name="malu",gender="female",phone="984572374",city="Tvm",date_today=datetime.datetime.today())
# instance.post(name="ram",gender="male",phone="784967274",city="Kollam",date_today=datetime.datetime.today())

print("-----------Get Datas-------------")
instance.get()

print("------------Retrieve a data-------------")
instance.retrieve(2)

print("--------------delete a data------------")
instance.delete(id=1)
instance.get()

print("---------------Updating-------------")
instance.put(2,city="Kayamkulam")
instance.get()