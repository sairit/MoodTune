from ytmusicapi import setup

# Generate authentication JSON file for YouTube Music
setup(
    filepath="backend/config/browser.json", 
    headers_raw="""""" # Headers for YouTube Music API authentication
)
