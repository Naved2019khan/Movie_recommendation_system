from http.client import responses
from urllib import response
import streamlit as st
import pickle
import pandas as pd
import requests

def fect_poster(movie_id):
    res = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=6bbdcf53caf7fbf7b7dd32d0c390b501&language=en-US'.format(movie_id))
    data =res.json()
    print(data)
    return "https://image.tmdb.org/t/p/w500/"+ data["poster_path"]

movie_list=pickle.load(open('movie_dict.pkl','rb'))
movies=pd.DataFrame(movie_list)

sim=pickle.load(open('sim.pkl','rb'))


def recommend(movie):
    movie_index=movies[movies['title']== movie].index[0]
    dis=sim[movie_index]
    movie_list=sorted(list(enumerate(dis)),reverse=True,key=lambda x:x[1])[1:6]
    r_list=[]
    r_movie_poster=[]
    for i in movie_list:
        movie_id=movies.iloc[i[0]].id
        r_list.append(movies.iloc[i[0]].title)
        #fetch_poster from api
        r_movie_poster.append(fect_poster(movie_id))
    return r_list,r_movie_poster

st.title('Movie recommandation system')
movie_name = st.selectbox(
'Select Movie',
movies['title'].values)
if st.button('Recommend'):
    names,posters=recommend(movie_name)
    col1, col2, col3, col4, col5  = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])

    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])