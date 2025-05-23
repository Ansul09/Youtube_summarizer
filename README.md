# Youtube_summarizer
🎥 YouTube Video Summarizer using OpenAI & Streamlit
This project is a YouTube video summarizer built with Streamlit, OpenAI GPT, and the YouTube Transcript API. It allows users to input a YouTube video URL, automatically fetches the transcript, and generates a concise, point-based summary using OpenAI's GPT model — helping users save time while retaining all key insights.

✨ Features:

  🧠 Generates concise summaries of YouTube videos in under 250 words

  📄 Extracts transcripts automatically using the video URL

  🤖 Uses OpenAI's GPT model to identify and summarize key points

  🎞 Displays the video thumbnail for quick visual reference

  🔐 Secure API key management via .env file

🛠️ Tech Stack:

  Streamlit – for building the interactive web UI

  OpenAI GPT-3.5 – for generating natural language summaries

  YouTube Transcript API – to extract transcripts from video links

  python-dotenv – for managing API keys securely

🚀 How It Works:

  User inputs a YouTube video URL.

  The app fetches the transcript using youtube-transcript-api.

  The transcript is passed to the OpenAI GPT API along with a prompt.

  A detailed, bullet-point style summary is generated and displayed.
