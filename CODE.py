import streamlit as st
from dotenv import load_dotenv
import os
import openai
from youtube_transcript_api import YouTubeTranscriptApi

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

prompt = """
You are a Youtube video summarizer. You will be taking the transcript text
and summarizing the entire video and providing the important summary in points
within 250 words. Please provide the summary of the text given here:
"""

def extract(youtube_video_url):
    try:
        video_id = youtube_video_url.split("=")[1]
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
        transcript = ""
        for item in transcript_list:
            transcript += item['text'] + " "
        return transcript
    except Exception as e:
        raise e

def generate_chatgpt_content(transcript_text, prompt):
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt + transcript_text}
    ]
)
    return response['choices'][0]['message']['content']

st.title("YouTube Transcript to Detailed Notes Converter")
youtube_link = st.text_input("Enter YouTube Video URL")

if youtube_link:
    video_id = youtube_link.split("=")[1]
    st.image(f"http://img.youtube.com/vi/{video_id}/0.jpg", use_column_width=True)

if st.button("Get detailed notes"):
    transcript_text = extract(youtube_link)
    if transcript_text:
        summary = generate_chatgpt_content(transcript_text, prompt)
        st.markdown("## Detailed Notes")
        st.text(summary)
