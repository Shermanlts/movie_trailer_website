import fresh_tomatoes
import media

# ************************Movie data is below**********
# Movie data formatting is as follows:
# movie_variable = media.Movie(
#   "movie name",
#   "movie desription",
#   "link to movie poster",
#   "link to movie video",
#   "link to movie imdb page")
#
# IMPORTANT! Make sure to add or remove movies from the movies variable
# before running

oceans_11 = media.Movie(
    "Ocean's 11",
    "Danny Ocean and his eleven accomplices plan to rob three Las Vegas"
    " casinos simultaneously.",
    "https://upload.wikimedia.org/wikipedia/en/6/68/Ocean%27s_Eleven_2001_Poster.jpg",  # noqa
    "https://www.youtube.com/watch?v=b_bzUIbE5jo",
    "http://www.imdb.com/title/tt0240772/?ref_=nv_sr_1")
american_president = media.Movie(
    "The American President",
    "Comedy-drama about a widowed U.S. president and a lobbist who fall"
    " in love.",
    "https://upload.wikimedia.org/wikipedia/en/f/f2/The_American_President_%28movie_poster%29.jpg",  # noqa
    "https://www.youtube.com/watch?v=YMXUfXnd3_U",
    "http://www.imdb.com/title/tt0112346/?ref_=nv_sr_1")
princess_bride = media.Movie(
    "The Princess Bride",
    "While home sick in bed, a young boy's grandfather reads him a story"
    " called The Princess Bride.",
    "https://upload.wikimedia.org/wikipedia/en/d/db/Princess_bride.jpg",
    "https://www.youtube.com/watch?v=VYgcrny2hRs",
    "http://www.imdb.com/title/tt0093779/?ref_=nv_sr_1")
shawshank_redemption = media.Movie(
    "The Shawshank Redemption",
    "Two imprisoned men bond over a number of years, finding solace and"
    " eventual redemption through acts of common decency.",
    "https://upload.wikimedia.org/wikipedia/en/8/81/ShawshankRedemptionMoviePoster.jpg",  # noqa
    "https://www.youtube.com/watch?v=6hB3S9bIaco",
    "http://www.imdb.com/title/tt0111161/?ref_=nv_sr_1")
red_octrober = media.Movie(
    "The Hunt for Red October",
    "In November 1984, the Soviet Union's best submarine captain in their"
    " newest sub violates orders and heads for the USA.",
    "https://upload.wikimedia.org/wikipedia/en/3/36/The_Hunt_for_Red_October_movie_poster.png",  # noqa
    "https://www.youtube.com/watch?v=3C2tE7vjdHk",
    "http://www.imdb.com/title/tt0099810/?ref_=nv_sr_2")
blazing_saddles = media.Movie(
    "Blazing Saddles",
    "To ruin a western town, a corrupt political boss appoints a black"
    " sheriff, who promplty becomes his most formidable adversary.",
    "https://upload.wikimedia.org/wikipedia/en/7/7b/Blazing_saddles_movie_poster.jpg",  # noqa
    "https://www.youtube.com/watch?v=VKayG1TrfuE",
    "http://www.imdb.com/title/tt0071230/?ref_=nv_sr_1")
movies = [oceans_11, american_president, princess_bride, shawshank_redemption,
          red_octrober, blazing_saddles]

# ************************************page build trigger below***************
fresh_tomatoes.open_movies_page(movies)
