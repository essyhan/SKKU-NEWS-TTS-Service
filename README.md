# 🎙️ SKKU News TTS & Summarization Service

## 📌 Project Overview
While the internet provides vast amounts of information, the visually impaired often face significant barriers to accessing digital news content. This project addresses this digital divide by developing a **Text-to-Speech (TTS) and News Summarization Application** specifically designed for Sungkyunkwan University (SKKU) students. 

The program automatically crawls school news, extracts core keywords and sentences, and converts the summarized text into audio (MP3) files. This allows visually impaired students to easily access campus news and enables non-impaired students to consume news efficiently while multitasking.

## 🛠️ Tech Stack & Methodology
*   **Web Crawling:** `BeautifulSoup`, `re` (Scraping SKKU news portal and text cleaning) 
*   **Natural Language Processing (NLP):** `kiwipiepy` (Sentence splitting and text normalization) 
*   **Text Summarization:** `krwordrank` (Extractive summarization for key sentences and keywords) 
*   **Text-to-Speech (TTS):** `gTTS` (Google Text-to-Speech), `pygame` (Audio playback) 
*   **GUI & Accessibility:** `tkinter` (Designed to support keyboard shortcuts with audio guidance for visually impaired users) 

## 💡 How It Works
1.  **Category Selection:** Users select a news category (e.g., General, Faculty, Students) via keyboard inputs guided by voice prompts .
2.  **Data Extraction:** The system crawls the selected article using `BeautifulSoup` and cleans the HTML tags .
3.  **NLP & Summarization:** The text is normalized and parsed. `krwordrank` identifies high-weight words and extracts the most crucial sentences .
4.  **Audio Output:** The system plays the summarized core sentences (or the full text) using `gTTS` and `pygame` .
