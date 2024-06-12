import streamlit as st
import functions

todos = functions.get_todos()

def add_todos():
    new_todo = st.session_state["todo"] + "\n"
    todos.append(new_todo)
    functions.write_todos(todos)
    st.session_state["todo"] = ''

st.title('Todo App')

for index,item in enumerate(todos):
    checkbox = st.checkbox(item,key=item)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[item]
        st.session_state["todo"] = ''
        st.experimental_rerun()

st.text_input(label='',placeholder='Add To Do....',on_change=add_todos,key="todo")