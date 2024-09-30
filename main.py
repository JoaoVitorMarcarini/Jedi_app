import streamlit as st


def principal():
    st.title('Jedi APP')
    st.subheader('Por Favor informe seus dados abaixo: ')

    name, age = jedi()

    st.write('Selecione sua categoria de Jedi que você pertence: ')
    category = st.selectbox('Categoria Jedi', ('Padawan', 'Cavaleiro', 'Mestre'))

    submit = st.button('Enviar dados')
    if submit:
        st.write('Seus dados foram enviados!')
        st.write(f'O jedi {name}, da categoria {category}, tem {age} anos.')

    st.image('rey.png', width=200)


def jedi():
    name = st.text_input('Nome do Jedi: ')
    age = st.number_input('Idade do jedi: ', value=0, step=1, min_value=0, max_value=1500)
    return name, age


if __name__ == '__main__':
    principal()