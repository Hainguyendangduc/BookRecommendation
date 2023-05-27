import streamlit as st
import pandas as pd
import pickle
from random import randint

books = pd.read_csv('df_2.csv')
df_1 = pickle.load(open('df_1.pkl', 'rb'))


def recommendation(title):
    recommendations = pd.DataFrame(df_1.nlargest(11, title)['title'])
    recommendations = recommendations[recommendations['title'] != title]
    list_name = recommendations['title'].values.tolist()

    add_img = []
    for name in list_name:
        add_img.append(books[books['title'] == name]['image_url'].iloc[0])

    return list_name, add_img


st.title('Content Based Book Recommendation System ')

with st.container():
    select = st.selectbox(
        'Which book would you like to choose?',
        books['title'].values)

    st.write('You selected:', select)

    if st.button('Recommend'):
        col = ["a", "b", "c", "d", "e"]

        list_books, list_imgs = recommendation(select)

        col = st.columns(5)
        with st.container():
            for i in range(5):
                c = col[i]
                with c:
                    st.text(list_books[i])
                    st.image(list_imgs[i])

        with st.container():
            col = st.columns(5)
            for i in range(5):
                c = col[i]
                with c:
                    st.text(list_books[i+5])
                    st.image(list_imgs[i+5])


with st.container():
    st.header('Books')

    colb = ['a', 'b', 'c', 'd', 'e']
    for i in range(10):
        with st.container():
            colb = st.columns(5)
            for c in colb:
                index = randint(0, len(books))
                book = books.iloc[index]
                with c:
                    st.text(book.title)
                    st.image(book.image_url)



