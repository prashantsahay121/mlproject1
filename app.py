import streamlit as st
import pickle
import pandas as pd
import requests



def fetch_Poster(movie_id):
    response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=2e0c27fbe450ce8aa11f9e5d01e2d0dc'.format(movie_id))
    data=response.json()
    print(data)

    return "https://image.tmdb.org/t/p/w500" + data['poster_path']




def recommend(selected_movie_name):
    # Ensure the DataFrame is available in this function
    global movies_df

    # Find the index of the selected movie
    movies_index = movies_df[movies_df['title'] == selected_movie_name].index[0]
    distances = similarity[movies_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommend_movies_posters=[]
    for i in movies_list:
        movie_id=movies_df.iloc[i[0]].movie_id
        recommended_movies.append(movies_df.iloc[i[0]].title)
        #featch poster from api
        recommend_movies_posters.append(fetch_Poster(movie_id))

    return recommended_movies,recommend_movies_posters



movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies_df = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

#st.title('Movie Recommender System')

st.markdown(
    """
    <style>
    .stApp {
        background-image: url('https://t4.ftcdn.net/jpg/05/71/83/47/360_F_571834789_ujYbUnH190iUokdDhZq7GXeTBRgqYVwa.jpg');
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }
    .movie-title {
        color: #FF5733; /* Change this to your desired color */
        font-weight: bold;
        font-size: 1rem;
        white-space: nowrap; /* Ensures text remains in one line */
        overflow: hidden; /* Hides the overflow text */
        text-overflow: ellipsis; /* Adds ellipsis if text overflows */
        max-width: 100%; /* Ensure it doesn’t exceed the container width */
        display: block; /* Block-level to manage width and height better */
    }
    .stTitle {
        color: #33CFFF; /* Change this to your desired color */
        font-size: 3rem;
        text-align: center;
    }
    .stTitle_i {
        color: #33FF57; /* Change this to your desired color */
        font-size: 1rem;
        text-align: center;
    }
    .stSelectbox label {
        color: #33FF57; /* Change this to your desired color */
        font-size: 1.5rem;
    }
    .css-1d391kg {
        padding: 1rem 2rem;
    }
    .but-rad {
        border-radius: 10px;
    }
    .button-watch {
        display: flex;
        justify-content: center;
        text-decoration: none;
    }
    .button-watch button:hover {
        background-color: green; /* Background color on hover */
        color:white;
    }
    a:hover {
        text-decoration: none; /* This removes the underline on hover */
    }
    </style>
    """,
    unsafe_allow_html=True
)


st.markdown('<h1 class="stTitle">Movie Recommender System</h1>', unsafe_allow_html=True)


selected_movie_name = st.selectbox(
    "Select a movie:",
    (movies_df['title'].values),
)
# selected_movie_name = st.selectbox(
#     "Select a movie:",
#     (movies_df['title'].values),
# )

if st.button("Recommend"):
    names,posters = recommend(selected_movie_name)
    url = ["https://www.hotstar.com/in/home?ref=%2Fin"]

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
      st.markdown(f'<div class="movie-title">{names[0]}</div>', unsafe_allow_html=True)
      st.image(posters[0])
      st.markdown(f'<a class="button-watch" href="{url[0]}" target="_blank"><button class="but-rad">Watch Now</button></a>', unsafe_allow_html=True)

    with col2:
      st.markdown(f'<div class="movie-title">{names[1]}</div>', unsafe_allow_html=True)
      st.image(posters[1])
      st.markdown(f'<a class="button-watch" href="{url[0]}" target="_blank"><button class="but-rad">Watch Now</button></a>', unsafe_allow_html=True)
    with col3:
      st.markdown(f'<div class="movie-title">{names[2]}</div>', unsafe_allow_html=True)
      st.image(posters[2])
      st.markdown(f'<a class="button-watch" href="{url[0]}" target="_blank"><button class="but-rad">Watch Now</button></a>', unsafe_allow_html=True)
    with col4:
      st.markdown(f'<div class="movie-title">{names[3]}</div>', unsafe_allow_html=True)
      st.image(posters[3])
      st.markdown(f'<a class="button-watch" href="{url[0]}" target="_blank"><button class="but-rad">Watch Now</button></a>', unsafe_allow_html=True)

    with col5:
      st.markdown(f'<div class="movie-title">{names[4]}</div>', unsafe_allow_html=True)
      st.image(posters[4])
      st.markdown(f'<a class="button-watch" href="{url[0]}" target="_blank"><button class="but-rad"  >Watch Now</button></a>', unsafe_allow_html=True)
            