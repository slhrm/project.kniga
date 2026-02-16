import streamlit as st

books = [
"Game of Thrones",
"The Wheel of Time",
"The First Law",
"Lord of the Rings",
"The Name of the Wind"
]

st.title("Book Checker App")
st.write("Enter a book title to check if it exist in the database.")

user_input = st.text_input("Book Title")

if st.button("Check Book"):
  if user_input.strip() == "":
    st.warning("Please enter a book title.")
  elif user_input in books:
    st.success("The book exists in the database!")
  else:
    st.error("The book is NOT in the database.")

new_book = st.text_input("Add book")
if st.button1("Add a book")
