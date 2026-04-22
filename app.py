import streamlit as st
import streamlit.components.v1 as components

# Page setup
st.set_page_config(
    page_title="Neon Solo Game",
    layout="wide"
)

st.title("🎮 Neon Solo Game")

# Load HTML game
with open("game.html", "r", encoding="utf-8") as f:
    html_code = f.read()

# Display game
components.html(
    html_code,
    height=600,
    scrolling=False
)
