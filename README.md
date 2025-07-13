# 🎵 MoodTune

Welcome to **MoodTune**! This guide walks you through setting up, using, and enjoying features of our application to create playlists tailored to your mood.

---

## 📚 Table of Contents

- [Introduction](#introduction)
- [Getting Started](#getting-started)
  - [Requirements](#requirements)
  - [Setting Up MoodTune](#setting-up-moodtune)
- [Accessing MoodTune](#accessing-moodtune)
- [Using MoodTune](#using-moodtune)
  - [Playlist Generation](#playlist-generation)
  - [Playlist Conversion](#playlist-conversion)
- [Tips and Best Practices](#tips-and-best-practices)
- [Visual Usage Examples](#visual-usage-examples)
- [Credits](#credits)

---

## 🧠 Introduction

**MoodTune** creates personalized playlists that match your emotional state, environment, and activity.

With MoodTune, you can:
- Generate playlists based on mood, energy level, and environment
- Convert playlists between Spotify and YouTube Music
- Save and export playlists for cross-platform enjoyment

> 🚧 **Note:** Frontend development is currently in progress. We're working on implementing a visual interface with graph-based song relationship visualizations.

---

## 🚀 Getting Started

### ✅ Requirements

You’ll need the following:

- A terminal/command line interface (CLI)
- Git installed
- Python 3.x
- pip (Python package installer)
- Internet access
- A web browser (preferably Chrome)

---

### 🛠️ Setting Up MoodTune

1. **Clone the Repository**

   ```bash
   git clone https://github.com/raorjun/MoodTune.git
   ```

2. **Navigate to the Project Directory**

   ```bash
   cd MoodTune
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Create the `.env` File**

   Inside the `config` directory, check `setup.py`, and create a `.env` file with the following content:

   ```env
   SPOTIFY_CLIENT_ID=5930b8014b5047b496f94084ad6d1eb2
   SPOTIFY_CLIENT_SECRET=f04b80b7b7f24760a5e7ee79f3ad4101
   SPOTIFY_USERNAME=316oak3pknl6fpqzstpw4z4kskti
   ```

---

## 💻 Accessing MoodTune

1. Open your terminal
2. Navigate to the folder where you cloned MoodTune
3. All interactions happen through the terminal — no browser UI is required

---

## 🎧 Using MoodTune

### 🎼 Playlist Generation

To create a custom playlist:

1. Navigate to the backend folder:

   ```bash
   cd backend
   ```

2. Run the generator:

   ```bash
   python generator.py
   ```

3. Provide the following inputs when prompted:
   - **Seed Playlist URL**
   - **Seed Platform** (spotify or youtube)
   - **Target Energy** (e.g., calm or energetic)
   - **Target Valence** (e.g., happy or gloomy)
   - **Activity** (e.g., workout, study)
   - **Environment** (e.g., gym, home)
   - **Number of Songs**
   - **Playlist Name** (optional)

4. 🎉 After generation, a new link will be displayed. Paste it into your browser to view your playlist.

5. 📊 Optionally, a visualization of song relationships will also be shown.

---

### 🔁 Playlist Conversion

To convert a playlist between Spotify and YouTube Music:

1. Navigate to the backend folder:

   ```bash
   cd backend
   ```

2. Run the converter:

   ```bash
   python converter.py
   ```

3. Provide the following:
   - **Target Platform** (spotify or youtube)
   - **Playlist URL**

4. ✅ A link to the converted playlist will be displayed.

---

## 💡 Tips and Best Practices

- Ensure your **seed playlist is public**
- Try different combinations of **energy**, **valence**, **activity**, and **environment**
- Save generated or converted playlists to your personal account

---

## 🖼️ Visual Usage Examples

👉 [View Examples on Google Drive](https://drive.google.com/drive/folders/14DHbQ6ubRU19QNuc3-DYvnkC-rhaGiFq?usp=sharing)

---

## 🙌 Credits

MoodTune was created by:

- **Arjun Rao**
- **Sai Yadavalli**

> 🧠 This project actively uses key data structures such as heaps/priority queues and linked lists in its core logic. We're also integrating graph data structures for enhanced visualizations in the frontend.

Thank you for using MoodTune to enhance your music experience!

---
