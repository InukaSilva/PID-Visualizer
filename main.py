import streamlit as st
import os


def load_file(filename):
    with open(filename, 'r') as f:
        return f.read()


html_content = load_file('PID_Visualizer.html')
css_content = load_file('PID_Visualizer.css')
js_content = load_file('PID_Controller.js')


full_content = f"""<style>{css_content}</style>{html_content}<script>{js_content}</script>"""
st.components.v1.html(full_content, height=600)