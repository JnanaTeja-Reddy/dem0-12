import streamlit as st
st.set_page_config(page_title='Cats')
st.header("Types of Cats")
col1, col2 = st.columns(2)
with col1:
  st.subheader("Persian Cat")
  st.image("./car.jpg", caption="Persian Cat", width=300)
  st.write("Persian cats are cute")
with col2:
  st.subheader("Ragdoll Cat")
  st.image("./ntr.jpg", caption="Ragdoll Cat", width=300)
  st.write("Ragdoll cats are proud")
