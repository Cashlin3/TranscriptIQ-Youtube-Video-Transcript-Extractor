"

## 🛠️ Tech Stack

| Layer | Tools |
|---|---|
| Frontend / App | Streamlit |
| Transcript Retrieval | `youtube-transcript-api` |
| URL Parsing | Python string handling |
| Environment | Python 3 |

---

## ⚙️ How It Works (Details)

1. **URL Input** — user pastes any standard YouTube video URL (`youtube.com/watch?v=...` or `youtu.be/...`).
2. **Video ID Extraction** — the app parses the URL to isolate the unique video ID, handling both common YouTube URL formats.
3. **Transcript Fetching** — calls the YouTube Transcript API to retrieve English captions for that video ID.
4. **Text Assembly & Display** — individual caption entries are joined into one continuous block of text and displayed in a scrollable text area.

---

## 🚀 Getting Started

```bash
git clone https://github.com/Cashlin3/youtube-transcript-viewer.git
cd youtube-transcript-viewer
pip install streamlit youtube-transcript-api
streamlit run app.py
```

---

## ⚠️ Limitations

- Only fetches **English** transcripts — videos without English captions (auto-generated or manual) will return an error
- Videos with captions disabled entirely will show "Transcript not available"
- Timestamps are stripped in the final output — only continuous text is shown

---

## 🔮 Future Improvements

- Add **multi-language** transcript support with a language selector
- Preserve and display **timestamps** alongside text for easier navigation
- Add a **download as .txt / .srt** button
- Add **AI-powered summarization** of the fetched transcript
- Handle YouTube Shorts URLs and playlist links

---

## 👤 Contributors

| Person | Role | Contributions |
|---|---|---|
| **Cashlin** ([@Cashlin3](https://github.com/Cashlin3)) | Developer | URL parsing logic, transcript retrieval integration, and Streamlit app development |

---





