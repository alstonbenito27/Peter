# -*- coding: utf-8 -*-
"""Day 5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1IkLS6erl4LeH5EJ22U-Hjg0HHqBSALXU
"""

pip install streamlit

import streamlit as st

# Commented out IPython magic to ensure Python compatibility.
# %%writefile our_application.py
# import streamlit as st
# 
# st.write("Hello Peter")

! wget -q -O - ipv4.icanhazip.com

! streamlit run our_application.py & npx localtunnel --port 8501
