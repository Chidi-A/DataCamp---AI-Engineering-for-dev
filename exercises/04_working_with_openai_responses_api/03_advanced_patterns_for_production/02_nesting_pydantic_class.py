# Define the SimilarMovie class
class SimilarMovie(BaseModel):
    title: str = Field(description="Title of a similar movie")
    similarity_reason: str = Field(description="Why this movie is similar")

# Define the DetailedMovieRecommendation class
class DetailedMovieRecommendation(BaseModel):
    title: str = Field(description="The movie title")
    genre: str = Field(description="Primary genre")
    vibe: str = Field(description="One-word vibe: cozy, thrilling, emotional, or fun")
    why: str = Field(description="One sentence explaining why this matches")
    similar_movies: list[SimilarMovie] = Field(description="Other movies with similar themes or style")

# Create a structured response for movie recommendation
response = client.responses.parse(
    model="gpt-5.4-mini",
    instructions="You are a knowledgeable movie recommender.",
    input="Recommend a movie for someone who loved Inception and wants something mind-bending",
    text_format=DetailedMovieRecommendation
)

# Extract the parsed recommendation
recommendation = response.output_parsed

print(f"Title: {recommendation.title}")
print(f"\nSimilar movies:")
for movie in recommendation.similar_movies:
    print(f"- {movie.title}: {movie.similarity_reason}")