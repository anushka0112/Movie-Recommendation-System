import streamlit as st
import pickle
import pandas as pd

movie_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movie_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    'Select a movie:',
    movies['title'].values
)


# Function to recommend movies
def recommend(movie_title):

    movie_index = movies[movies['title'] == movie_title].index[0]
    recommended_movies=[]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    for i in movies_list:
        movie_id=i[0]

        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies


# Button to trigger the recommendation
if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)
    st.write('Here are some movies you might like:')
    for title in recommendations:
        st.write(title)
