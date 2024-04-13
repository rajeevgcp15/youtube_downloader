import streamlit as st
from pytube import YouTube
#YouTube('https://youtu.be/2lAe1cqCOXo').streams.first().download()
#yt = YouTube('http://youtube.com/watch?v=2lAe1cqCOXo')
#st.download_button(label = "downloaded_file", data = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download())
def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()
    except:
        print("An error has occurred")
    print("Download is completed successfully")


link = st.input("Enter the YouTube video URL: ")
if st.button("Click to Download File"):
    Download(link)
