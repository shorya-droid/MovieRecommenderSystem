import pandas as pd
import streamlit as st
import pickle


def recommend(movie):
    try:
        index_of_the_movie = movie_list[movie_list['title'] == movie].index[0]
        distances = similarity[index_of_the_movie]

        movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

        recommended_movies = []
        for i in movies_list:
            movie_id = i[0]
            recommended_movies.append(movie_list.iloc[i[0]].title)
        return recommended_movies
    except IndexError:
        st.write("Movie not found or an error occurred.")
        return []

movie_list = pickle.load(open('movie1.pkl', 'rb'))
movie_list = pd.DataFrame(movie_list)

similarity = pickle.load(open('similarity.pkl', 'rb'))
st.title('Movie Recommendation System')

selected_movie_name = st.selectbox(
    'Browse 5000+ Global Movies',
    movie_list['title'].values)

if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)
