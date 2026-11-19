import streamlit as st
import pickle
import pandas as pd
movies = pickle.load(open('movies.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))
def recommend(movie):
    movie_index = movies[movies['title']== movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)),reverse = True, key = lambda x: x[1])[1:6]
    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies
st.set_page_config(page_title = 'Movie Recommender', page_icon ="Movie", layout ="centered")
st.markdown("""
    <style>
    .stApp{
    background-color: #141414;
    color: #FFFFFF;
    }
    h1 {
    color: #E50914;
    text-align: center;
    font-weight: 800;
    letter-spacing: 1px;
    }
    p, label{
    color: #E5E5E5 ! important:
    }
    .stButton > button {
    background-color: #E50914;
    color: white;
    font-size: 18px;
    font-weight: bold;
    width: 100%;
    border-radius: 5px;
    border: none;}
    .stButton>button:hover{
    background-color: #B20710;
    }
    .movie-card{
    background-color: #222222;
    padding: 15px;
    border-radius: 8px;
    border-left: 5px solid #E50914;
    margin-bottom: 10px;
    font-size: 18px;
    font-weight: bold;
    color: #FFFFFF;
    }
    </style>
""",unsafe_allow_html =True)
st.title("MOVIE RECOMMENDER SYSTEM")
st.write("Select your favourite movie and see best five similar movies")
st.markdown("-----")
selected_movie = st.selectbox("Select a movie:", movies['title'].values)
if st.button("Recommend Movies"):
    recommendations = recommend(selected_movie)
    st.subheader(f" Beacause you watched'{selected_movie}':")
    for idx, movie_name in enumerate(recommendations, 1):
        st.markdown(f'<div class = "movie-card"> {idx}.{movie_name}</div>', unsafe_allow_html =True)
