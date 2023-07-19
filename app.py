import streamlit as st
import pickle
import requests

page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
background-image: url("https://repository-images.githubusercontent.com/275336521/20d38e00-6634-11eb-9d1f-6a5232d0f84f");
background-size: cover;
}
[data-testid="stHeader"] {
background-color: rgba(0, 0, 0, 0);
}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=d3b9ac0af55375a554447ba2a8e2cf0c&language=en-US'.format(movie_id))
    data = response.json()
    if data['poster_path'] is not None:
        return 'https://image.tmdb.org/t/p/w500/' + data['poster_path']
    else:
        return None

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x:x[1])[1:7]
    recommend_movies = []
    recommended_movies_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].id
        recommend_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommend_movies, recommended_movies_posters

def top_15_movies():
    recommend_movies = []
    recommended_movies_posters = []
    for i in top_movies.index:
        movie_id = top_movies['id'][i]
        recommend_movies.append(top_movies['title'][i])
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommend_movies, recommended_movies_posters

movies = pickle.load(open('movies.pkl','rb'))
top_movies = pickle.load(open('top_movies.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

st.title('TMDb Movie Recommender System')

movies_name = movies['title'].values
selected_movie_name = st.selectbox('Pick a Movie', movies_name)


if st.button('Recommend Similar Movies'):
    
    st.title('Top Picks For You')
    names,posters = recommend(selected_movie_name)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image(posters[0])
        st.markdown('<b>{}</b>'.format(names[0]), unsafe_allow_html=True)
    with col2:
        st.image(posters[1])
        st.markdown('<b>{}</b>'.format(names[1]), unsafe_allow_html=True)
    with col3:
        st.image(posters[2])
        st.markdown('<b>{}</b>'.format(names[2]), unsafe_allow_html=True)

    st.title('You Might Also Like')
    col4, col5, col6 = st.columns(3)
    with col4:
        st.image(posters[3])
        st.markdown('<b>{}</b>'.format(names[3]), unsafe_allow_html=True)
    with col5:
        st.image(posters[4])
        st.markdown('<b>{}</b>'.format(names[4]), unsafe_allow_html=True)
    with col6:
        st.image(posters[5])
        st.markdown('<b>{}</b>'.format(names[5]), unsafe_allow_html=True)

else:
    st.title('Top Rated Movies')
    names,posters = top_15_movies()

    col1, col2, col3 = st.columns(3)
    with col1:
        st.image(posters[0])
        st.markdown('<b>{}</b>'.format(names[0]), unsafe_allow_html=True)
    with col2:
        st.image(posters[1])
        st.markdown('<b>{}</b>'.format(names[1]), unsafe_allow_html=True)
    with col3:
        st.image(posters[2])
        st.markdown('<b>{}</b>'.format(names[2]), unsafe_allow_html=True)

    col4, col5, col6 = st.columns(3)
    with col4:
        st.image(posters[3])
        st.markdown('<b>{}</b>'.format(names[3]), unsafe_allow_html=True)
    with col5:
        st.image(posters[4])
        st.markdown('<b>{}</b>'.format(names[4]), unsafe_allow_html=True)
    with col6:
        st.image(posters[5])
        st.markdown('<b>{}</b>'.format(names[5]), unsafe_allow_html=True)

    col7, col8, col9 = st.columns(3)
    with col7:
        st.image(posters[6])
        st.markdown('<b>{}</b>'.format(names[6]), unsafe_allow_html=True)
    with col8:
        st.image(posters[7])
        st.markdown('<b>{}</b>'.format(names[7]), unsafe_allow_html=True)
    with col9:
        st.image(posters[8])
        st.markdown('<b>{}</b>'.format(names[8]), unsafe_allow_html=True)

    col10, col11, col12 = st.columns(3)
    with col10:
        st.image(posters[9])
        st.markdown('<b>{}</b>'.format(names[9]), unsafe_allow_html=True)
    with col11:
        st.image(posters[10])
        st.markdown('<b>{}</b>'.format(names[10]), unsafe_allow_html=True)
    with col12:
        st.image(posters[11])
        st.markdown('<b>{}</b>'.format(names[11]), unsafe_allow_html=True)

    col13, col14, col15 = st.columns(3)
    with col13:
        st.image(posters[12])
        st.markdown('<b>{}</b>'.format(names[12]), unsafe_allow_html=True)
    with col14:
        st.image(posters[13])
        st.markdown('<b>{}</b>'.format(names[13]), unsafe_allow_html=True)
    with col15:
        st.image(posters[14])
        st.markdown('<b>{}</b>'.format(names[14]), unsafe_allow_html=True)