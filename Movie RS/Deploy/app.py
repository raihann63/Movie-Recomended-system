import streamlit as st
import pickle
import pandas as pd
import requests


# ✅ Step 1: Load DataFrame from pickle
movies_df = pickle.load(open('movies.pkl', 'rb'))  # এটা DataFrame
similarity = pickle.load(open('similarity.pkl', 'rb'))


# ✅ Step 2: Recommendation function
def recommend(movie):
    movie_index = movies_df[movies_df['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_indices = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    for i in movie_indices:
        movie_id = i[0]
        #fetch poster from API
        recommended_movies.append(movies_df.iloc[i[0]].title)

    return recommended_movies

# ✅ Step 3: Streamlit UI
st.title("🎬 Movie Recommended System")

selected_movie_name = st.selectbox(
    "Select a movie",
    movies_df['title'].values  # শুধু title list দেখাও
)

if st.button("Recommended"):
    recommendation = recommend(selected_movie_name)
    st.subheader("Top 5 Recommended Movies:")
    for i in recommendation:
        st.write(i)
