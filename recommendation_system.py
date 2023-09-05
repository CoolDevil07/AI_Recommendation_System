
import numpy as np

user_item_matrix = np.array([
    [5, 4, 0, 0, 0],
    [0, 0, 4, 5, 0],
    [4, 0, 5, 0, 0],
    [0, 0, 0, 2, 4],
    [0, 3, 0, 0, 5]
])

def recommend_movies(user_id, user_item_matrix, num_recommendations=3):
   
    user_similarities = np.dot(user_item_matrix, user_item_matrix[user_id]) / (np.linalg.norm(user_item_matrix, axis=1) * np.linalg.norm(user_item_matrix[user_id]))

    similar_users = np.argsort(user_similarities)[::-1]

    recommendations = []

    unrated_movies = np.where(user_item_matrix[user_id] == 0)[0]

   
    for user in similar_users:
        for movie in unrated_movies:
            if user_item_matrix[user][movie] > 0:
                recommendations.append((movie, user_item_matrix[user][movie]))
                if len(recommendations) >= num_recommendations:
                    break
        if len(recommendations) >= num_recommendations:
            break

    recommendations.sort(key=lambda x: x[1], reverse=True)

    recommended_movie_ids = [movie_id for movie_id, _ in recommendations]

    return recommended_movie_ids


user_id = 0  # User for whom we want to recommend movies
recommendations = recommend_movies(user_id, user_item_matrix, num_recommendations=3)

movie_titles = ["Movie A", "Movie B", "Movie C", "Movie D", "Movie E"]


print(f"Recommended movies for User {user_id}:")
for i, movie_id in enumerate(recommendations):
    print(f"{i + 1}. {movie_titles[movie_id]}")
