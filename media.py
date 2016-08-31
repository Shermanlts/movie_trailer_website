class Movie():
	"""The Movie class is used to store information on movies"""

	def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube,imdb_link):
		"""The init function holds the various variables for the Movie Class"""
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube
		self.imdb_link = imdb_link
