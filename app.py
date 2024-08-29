import streamlit as st

st.title("MystiRhys")
st.image("logo_letter.png")

styl = f"""
<style>
	#mystirhys{{
		font-size: 75px;
        color: gold;
	}}
	
</style>
"""
st.markdown(styl, unsafe_allow_html=True)