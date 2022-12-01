import streamlit as st


st.title('Streamlit Tutorial App')
st.write('This is my new app')


button1 = st.button('Click me')

if button1:
    st.write('This is some text lol')

st.header('Checkbox Section')

like = st.checkbox('Do you like the app')

but2 = st.button('Submit')

if but2:
    if like:
        st.write("Thank you")

    else:
        st.write('Thanks')


st.header('Radio button Section')

animal2 = st.radio('What animal do you like?', ("Lions","Tigers","Bears"))

but3 = st.button('Submit Animal')

if but3:
    st.write(animal2)
    if animal2 == 'Lions':
        st.write('Roar')




st.header('Select button Section')

animal2 = st.selectbox('What animal do you like?', ("Lions","Tigers","Bears"))

but4 = st.button('Submit Animal2')

if but4:
    st.write(animal2)
    if animal2 == 'Lions':
        st.write('Roar')
        


st.header('Multi Select box button Section')

options = st.multiselect('What animals do you like', ['Lion','Tiger','Bear',])
but5 = st.button('Print Animals')

if but5:
    st.write(options)
    
st.header('Slider Section')

epochs_num = st.slider('How many epochs?',1,100,10)

if st.button("Slider Button"):
    st.write(epochs_num)

st.header('Text Input section')

user_text = st.text_input('Whats your fav movie?', "Harry Potter")

if st.button('Text Button'):
    st.write(user_text)


user_num = st.number_input('Fav Number')

if st.button("Number Button"):
    st.write(user_num)