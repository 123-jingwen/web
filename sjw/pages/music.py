import streamlit as st

st.set_page_config(page_title='萌宠之家',page_icon='🦦')

images= [{'url': 'https://modernvet.com/wp-content/uploads/2022/11/catsleepoutside.jpg',
          'parm':'橘猫'
        },
         {'url':'https://cdn.pixabay.com/photo/2022/01/29/16/13/cat-6977896_960_720.jpg',
          'parm':'圆润猫'
        },
         {'url':'https://www.ncl.ac.uk/media/wwwnclacuk/pressoffice/images/kitten-standard.jpg',
          'parm':'幼猫'
                }

]
if 'ind' not in st.session_state:
    st.session_state['ind']=0

def nextImg():
    st.session_state['ind']=(st.session_state['ind']+1) % len(images)
st.image(images[st.session_state['ind']]['url'],caption=images[st.session_state['ind']]['parm'])
def lastImg():
    st.session_state['ind']=(st.session_state['ind']-1) % len(images)
col1,col2=st.columns(2)   
with col2:
   st.button('下一张',on_click=nextImg,use_container_width=True)
with col1:
   st.button('上一张',on_click=lastImg,use_container_width=True)


