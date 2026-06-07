import streamlit as st
import pandas as pd

st.title(
    "Early Childhood Intervention System"
)

duration = st.slider(
    "Usage Duration",
    0,
    180,
    60
)

frequency = st.slider(
    "Usage Frequency",
    0,
    30,
    10
)

st.write(
    "Duration:",
    duration
)

st.write(
    "Frequency:",
    frequency
)
