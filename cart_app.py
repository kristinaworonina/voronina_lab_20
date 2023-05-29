import streamlit as st

# Завдати сайдбар
st.sidebar.title('Shopping Cart')

# Завдати заголовок
st.header('Items in Cart')

# Створити порожній лист предметів в корзині
items = []

# Вивести предмети в корзині
placeholder = st.empty()
with placeholder.container():
    for item in items:
        st.write(item)

# Завдати поле вводу назви
item_name = st.text_input('Item name')

# Завдати кнопки додання та видалення
add_button_col, remove_button_col = st.columns(2)
with add_button_col:
    add_button = st.button('Add item')
with remove_button_col:
    remove_button = st.button('Remove item')

# Додавати предмет до корзини при нажатті на кнопку додання
if add_button:
    items.append(item_name)
    with placeholder.container():
        for item in items:
            st.write(item)

# Вилучати існуючий предмет з корзини при нажатті на кнопку видалення
if remove_button:
    if item_name in items:
        items.remove(item_name)
        with placeholder.container():
            for item in items:
                st.write(item)

