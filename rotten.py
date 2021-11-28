import os
import json
from urllib import request, parse
import argparse


# Movie argument parsing
parser = argparse.ArgumentParser(description='Movie CLI Parser')
parser.add_argument(
    "--movie",
    type=str,
    help="Movie name to be checked in DB",
    required=True
) 
args = parser.parse_args()

# Obtain API key from envs 
apikey = os.getenv("OMDB_API_KEY")

if apikey:
    url_key_suffix = f"&apikey={apikey}"
    response = request.urlopen(f"https://www.omdbapi.com/?t={parse.quote(args.movie)}" + url_key_suffix) 
    movie_data = json.loads(response.read())
    rt_rating = None

    if 'Ratings' in movie_data:
        for rating in movie_data['Ratings']:
            if rating['Source'] == "Rotten Tomatoes":
                rt_rating = rating['Value']

    if rt_rating:
        print(f"Rotten Tomatoes rating for {args.movie} is: {rt_rating}")

    else:
        print("No such movie or related Rotten Tomatoes rating found!")

else:
     print("API key missing - please set environment variable OMDB_API_KEY")
