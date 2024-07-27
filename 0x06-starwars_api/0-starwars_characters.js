#!/usr/bin/node
import sys
import requests


def get_movie_characters(movie_id):
    # Base URL for the SWAPI films endpoint
    base_url = f"https://swapi.dev/api/films/{movie_id}/"

    try:
        # Make a GET request to fetch the movie details
        response = requests.get(base_url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        movie_data = response.json()

        # Extract the list of character URLs
        character_urls = movie_data.get('characters', [])
        
        # Fetch and print each character name
        for url in character_urls:
            char_response = requests.get(url)
            char_response.raise_for_status()
            char_data = char_response.json()
            print(char_data['name'])
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
    except KeyError:
        print("Invalid Movie ID or data format has changed.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <Movie ID>")
        sys.exit(1)
    
    movie_id = sys.argv[1]
    get_movie_characters(movie_id)
