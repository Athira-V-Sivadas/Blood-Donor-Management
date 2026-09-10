import streamlit as st
from blood_donor_view_obj import BloodDonorManager

donor_instance=BloodDonorManager()

tab1,tab2=st.tabs(["ADD","VIEW"])

with tab1:
    st.title("Add new blood donor")
    name=st.text_input("Enter donor name")
    blood_group=st.text_input("Enter donor blood group")
    phone=st.text_input("Enter donor phone number")
    city=st.text_input("Enter donor city")
    last_donation=st.text_input("Enter donor's last donation date")

    if st.button("Add Donor"):
        donor_instance.post(name=name,blood_group=blood_group,phone=phone,city=city,last_donation=last_donation)
        st.success("Blood Donor added successfully")


with tab2:
    st.title("View Blood donor details")