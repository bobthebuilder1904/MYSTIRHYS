import streamlit as st
import streamlit.components.v1 as components
# Display an image
st.image("logo_letter.png")

# Create an expander that works like a dropdown
with st.expander("Coin tricks"):
    st.subheader("Coin setup")
    st.write("You will start by taking your magic coins and slamming one at a time on the table with the ring connected. You will see the fake stack of quarters and stack the real one on top. After you do this with both your setup is complete.")
    st.subheader("Appearing Coins")
    st.write("For this trick you will take the ring and one of the caps with the fake and real coins inside. You will show the spectator the seemlessly empty cap. You will take the ring and place it on top of the cap. You will slam the ring and cap which are still connected on the table. You will see the spectators amazement as you show them the cap looks the same.")
	
st.video("https://youtube.com/shorts/qmNS8L4ED_M?si=Xv4z6rUi4joFWT5b")
video_iframe = """
<iframe width="560" height="315" src="https://youtube.com/shorts/qmNS8L4ED_M?si=Xv4z6rUi4joFWT5b; picture-in-picture" allowfullscreen></iframe>
"""

# Embed the iframe
components.html(video_iframe, height=315)