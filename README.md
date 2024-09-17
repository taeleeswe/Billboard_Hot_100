#  Billboard Music Playlist Project

This project scrapes the Billboard Hot 100 chart for a specific date and automatically creates a Spotify playlist with the top songs from that chart. It uses the Spotify API for authentication and playlist creation, and BeautifulSoup for web scraping.

## Features
- Scrapes Billboard's Hot 100 chart for a given date.
- Searches for the songs on Spotify and collects their URIs.
- Automatically creates a new private Spotify playlist with the collected songs.

## Technologies Used
- **Python**: Core programming language.
- **BeautifulSoup**: For web scraping Billboard's Hot 100 chart.
- **Spotify API**: For authentication and playlist management.
- **Spotipy**: Python library for interacting with the Spotify API.
- **dotenv**: To load environment variables from a `.env` file.

## Setup Instructions

### 1. Clone the repository

- git clone https://github.com/your-username/music-playlist-project.git
- cd billboard_music-playlist-project

### 2. Install Dependencies

 - pip install -r requirements.txt

### 3. Set Up Environment Variables

Create a .env file in the root directory with the following:
- CLIENT_ID=your_spotify_client_id
- CLIENT_SECRET=your_spotify_client_secret

### 4. Run the Script
- python script.py

## How it Works
1. **Input Date**: The user is asked to input a date in the format YYYY-MM-DD to select which Billboard chart to scrape.
2. **Scraping Billboard**: BeautifulSoup is used to scrape song titles from Billboard's Hot 100 for the given date.
3. **Spotify Authentication**: The script uses Spotipy to authenticate the user via the Spotify API.
4. **Search Songs on Spotify**: For each song scraped from Billboard, the script searches for a matching track on Spotify.
5. **Create Playlist**: After collecting the URIs of the tracks, a new private playlist is created in the user's Spotify account.
6. **Add Songs to Playlist**: The songs are added to the newly created playlist.
  
