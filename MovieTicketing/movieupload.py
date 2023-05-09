from py_filecoin_api_client import FilecoinAPI

def upload_movie(movie_path):
    # Create a FilecoinAPI instance
    filecoin_api = FilecoinAPI()

    # Upload the movie to the Filecoin network
    cid = filecoin_api.upload_file(movie_path)

    return cid

# Provide the path to the movie file
movie_path = '/path/to/movie.mp4'

# Upload the movie
cid = upload_movie(movie_path)
print(f"Movie CID: {cid}")
