from PIL import Image
from regex import R
import requests
import streamlit as st 
from streamlit_lottie import st_lottie


#got emojis from https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title= "Gem Mint Horror", page_icon=":alien:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

#use local CSS
def local_css(file_name):
     with open(file_name) as f:
         st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/styles.css")

#---- loading animation assests and for more go to: https://lottiefiles.com/search?q=scary%20movies&category=animations
lottie_coding = load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_qm8eqzse.json")
img_contact_form = Image.open("images/New_Logo.png")

#-----header section----
with st.container():
    st.subheader("GEM MINT HORROR")
    st.title("A late night radio show for you insominacs to fuel your nightmare.")
    st.write(
    ''''''
    "Hey guys welcome to the Gem Mint Horror website where you can gain access to our show"
    "and soon youtube channel to finally let you guys have visuals and of course see me !"
    ''''''
    )
    st.write("[Listen to Podcast >](https://linktr.ee/GemMintHorror)")

# #-----what i do-----
with st.container(): #type:ignore
     st.write("---")
     left_column, right_column = st.columns(2)
     with left_column:
          st.write("What is Gem Mint Horror !")
          st.write("##")
          st.write(
         '''''
         On my Podcast i am creating a horror community by introducing other horror fans into films they havent heard of."
         "-I do this by introducing the film."
         "-Narating a scene from the film that will convince you to watch it."
         "-Than giving my opinion on what the scene and film does best !
         '''
         )
     st.write("[You can find the podcast on all the directories >] (https://linktr.ee/GemMintHorror)")

with right_column:
    st_lottie(lottie_coding, height=400, key="horror")

# #----projects----
with st.container():
     st.write("---")     
     st.header("My Projects")
     st.write("##")
     image_column, text_column = st.columns((1, 2))
    
     #inserting images
     with image_column:
         st.image(img_contact_form)
     with text_column:
         st.subheader( "The Descent")
         st.write(
             ''''
             Hey there, welcome back to your favorite late night radio show Gem Mint Horror. I'm your host Joel, here to keep you
              late night insomniacs company and hopefully find you guys a new favorite horror film that you probably never heard of.
               On tonights episode we will be discussing the 2005 British horror film... and no, you don't have to read subtitles for 
               those who have begun to roll your eyes, unless you are form international waters... here we go again. 
               The Descent directed by Neil Marshall, follows a group of women who adventure through the caves within the appellation 
               mountains. These ladies believe they are the only ones exploring the caves. Boy are they wrong! If you like this movie 
               or this episode, please let me know on the socials below! Thank you for your continuing support and 
               I'll be back with more next Friday night.

             '''''
         )
         st.markdown("[Listen to Latest Episode...](https://linktr.ee/GemMintHorror)")


# #----contact----
with st.container():
     st.write("---")
     st.header("Stay up to Date")
     st.write("##")
#     #documention: 
     contact_form = """"
     <form action="https://formsubmit.co/gemminthorror98@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false>
        <input type="text" name="name" placeholder ="your name"  required>
        <input type="email" name="email" placeholder = "your email" required>
        <textarea name = "message" placeholder ="Your message here !" required></textarea>
        <button type="submit">Send</button>
    </form>
    """

left_colum, right_column = st.columns(2)
with left_column:
     st.markdown(contact_form, unsafe_allow_html=True)

with right_column:
     st.empty()