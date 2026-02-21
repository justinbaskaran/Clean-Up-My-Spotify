# 🎧 Spotify Cleaner

Ever opened Spotify and thought:

> "Who is this?"  
> "When did I follow this artist?"  
> "Why is this playlist still here?"

Spotify makes it easy to add music, playlists, and artists, but it doesn’t make it easy to clean up your library. This Python 3 script gives you a simple, programmatic way to audit and declutter your Spotify account.

It is designed to be **lightweight, fully scriptable, and easy to run** from your terminal.

---

## 🧹 Features

This script allows you to:

- **View followed artists** – See all the artists you currently follow.  
- **Review saved tracks** – Inspect all saved songs in your library.  
- **Inspect playlists** – List all playlists you own or follow.  
- **Unfollow artists in bulk** – Remove artists you no longer listen to.  
- **Remove saved tracks** – Delete tracks from your library in bulk.  
- **Clean up playlists** – Remove unwanted tracks from your playlists.  
- **Regain control** – Keep your Spotify library organized and clutter-free.  

> ⚡ This is intended as a **developer-friendly, scriptable tool**, not a GUI application.

---

## ⚙️ Requirements

- Python 3.x (tested with Python 3.9+)  
- A **Spotify Developer account**  
- A registered **Spotify application** for OAuth  
- Python packages:
  - `spotipy` – Spotify Web API Python client  
  - `python-dotenv` – Load environment variables from `.env`  

---

## 🔐 Spotify Developer Setup

To connect this script to your Spotify account:

1. Go to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/).  
2. Log in with your Spotify account and create a new application.  
3. Copy your:
   - `CLIENT_ID`  
   - `CLIENT_SECRET`  
4. Add a **Redirect URI** (example):
