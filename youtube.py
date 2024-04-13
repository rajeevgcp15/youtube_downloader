import streamlit as st
from pytube import YouTube
YouTube('https://youtu.be/2lAe1cqCOXo').streams.first().download()
yt = YouTube('http://youtube.com/watch?v=2lAe1cqCOXo')
st.download_button(yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download())
