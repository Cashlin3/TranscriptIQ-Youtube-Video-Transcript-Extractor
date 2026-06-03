import streamlit as st
from youtube_transcript_api import YouTubeTranscriptApi

def get_video_id(url):
    """Extract video ID from YouTube URL"""
    if "watch?v=" in url:
        return url.split("watch?v=")[-1].split("&")[0]
    elif "youtu.be/" in url:
        return url.split("youtu.be/")[-1].split("?")
    else:
        return None

def fetch_transcript(video_id):
    """Fetch transcript for a given YouTube video ID"""
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['en'])
        full_text = " ".join([entry['text'] for entry in transcript])
        return full_text
    except Exception as e:
        return None

# Streamlit UI
st.title("YouTube Video Transcript Viewer")

url = st.text_input("Paste YouTube Video URL here:")

if url:
    video_id = get_video_id(url)
    if not video_id:
        st.error("Invalid YouTube URL")
    else:
        st.write("Fetching transcript...")
        transcript = fetch_transcript(video_id)
        if transcript is None:
            st.error("Transcript not available for this video.")
        else:
            st.subheader("Transcript (English)")
            st.text_area("", transcript, height=400)