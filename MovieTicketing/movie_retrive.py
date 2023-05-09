from py_filecoin_api_client import FilecoinAPI


def retrieve_movie(cid, output_path):
  # Create a FilecoinAPI instance
  filecoin_api = FilecoinAPI()

  # Download the movie from the Filecoin network
  filecoin_api.download_file(cid, output_path)


# Provide the CID of the movie and the output path
cid = 'your-movie-cid'
output_path = '/path/to/output/movie.mp4'

# Retrieve the movie
retrieve_movie(cid, output_path)
