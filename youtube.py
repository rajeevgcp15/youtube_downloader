import streamlit as st
from pytube import YouTube
#YouTube('https://youtu.be/2lAe1cqCOXo').streams.first().download()
#yt = YouTube('http://youtube.com/watch?v=2lAe1cqCOXo')
#st.download_button(label = "downloaded_file", data = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download())
def Download(link):
    st.write("Func call1")
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()
        st.write("call3")
    except:
        print("An error has occurred")
    print("Download is completed successfully")


link = st.text_input("Enter the YouTube video URL: ")
if st.button("Click to Download File"):
    st.write("hello")
    Download(link)
