# import the streamlit library
import streamlit as st
from PIL import Image 
# give a title to our app
st.title('Welcome to BIRTHDAY WISH generator')
 
#take NAME input
name = st.text_input("Enter your name (IN CAPITAL LETTERS)")
if(name == 'KUSHAGRA CHOUDHURY'):
    st.text("HAPPY BIRTHDAY\n"+name)
    st.text("THANK YOU FOR BEING A ___________ SENIOR AND A FRIEND")
    st.success("HONEST")
 
    # success
    st.info("INFLUENTIAL")
    
    # success
    st.warning("TRUSTWORTHY")
    
    # success
    st.error("OBLIGING")
   
    img = Image.open("picture.jpg")
 
# display image using streamlit
# width is used to set the width of an image
    st.image(img, width=500)
    st.title("*HAPPY BIRTHDAY!!*")
    st.text("You are my favourite human ")
    st.text("I will forever cherish the time that we spent together")
    st.text("I don't know about the future,we will be in touch or not but i promise you ,you will receive a upgraded version of a web page wish")
    st.text("every year on your birthday !!!")
    st.text("You have a great smile. KEEP SMILING!! and all the best for your placements")
    st.markdown("*EVEN IF THE WORLD TURNS AGAINST YOU ,REMEMBER I BELIEVE IN YOU ,TRUST YOU  AND I'M ALWAYS THERE FOR YOU*")
    
    
    st.text("REVIEWS?")
    # multi select box
 
    # first argument takes the box title
    # second argument takes the options to show
    OPTIONS = st.selectbox("OPTIONS: ",
                            ['WORST', 'EXCELAAAANNTTTT', 'THEEKTHAK'])
    
    
    st.write("YOUR REVIEW IS IT WAS:",OPTIONS)
elif(name == 'KUSHAGRA'):
    st.text("HAPPY BIRTHDAY\n"+name)
    
    st.text("THANK YOU FOR BEING A ___________ SENIOR AND A FRIEND")
    st.success("HONEST")
 
    # success
    st.info("INFLUENTIAL")
    
    # success
    st.warning("TRUSTWORTHY")
    
    # success
    st.error("OBLIGING")
   
    img = Image.open("picture.jpg")
 
# display image using streamlit
# width is used to set the width of an image
    st.image(img, width=300)
    st.title("*HAPPY BIRTHDAY!!*")
    st.text("You are my favourite human ")
    st.text("I will forever cherish the time that we spent together")
    st.text("I don't know about the future,we will be in touch or not but i promise you ,you will receive a upgraded version of a web page wish")
    st.text("every year on your birthday !!!")
    st.text("You have a great smile. KEEP SMILING!! and all the best for your placements")
    st.markdown("*EVEN IF THE WORLD TURNS AGAINST YOU ,REMEMBER I BELIEVE IN YOU ,TRUST YOU  AND I'M ALWAYS THERE FOR YOU*")
    
    
    st.text("REVIEWS?")
    # multi select box
 
    # first argument takes the box title
    # second argument takes the options to show
    OPTIONS = st.selectbox("OPTIONS: ",
                            ['WORST', 'EXCELAAAANNTTTT', 'THEEKTHAK'])
    
    
    st.write("YOUR REVIEW IS IT WAS:",OPTIONS)

 

    
st.text("------------DESIGNED BY SHAILI--------------")
 