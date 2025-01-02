import streamlit as st

with st.form(key='my_form'):
    header = st.header('my form ')
    number_1 = st.text_input('Enter Frist name:')
    number_2 = st.text_input('Enter 2nd name:')
    agree =st.checkbox('I agree')
    choice =st.radio('choise one number :',['1','2','3'])
    select_box =st.selectbox('Choose an option:', ['Option A', 'Option B', 'Option C'])
    options = st.multiselect('Pick multiple options:', ['A', 'B', 'C', 'D'])        
    date = st.date_input('Pick a date:')
    uploaded_file = st.file_uploader('Choose a file')
    submit_button = st.form_submit_button(label='Submit')    

if submit_button: 
    if choice and select_box and options and uploaded_file:
            sum = number_1 + number_2
            st.write(f"User name is  {sum} ")
            st.write(f"your choice is :{choice} and selectbox is {select_box} and options are {options}")
            st.write('File uploaded:', uploaded_file.name)
            st.write('Selected date:', date)
            st.balloons()
            st.write("you agreed thankyou")    
    else:
        st.write("please also chack the chackbox")


st.sidebar.markdown("# Main page 🎈")
