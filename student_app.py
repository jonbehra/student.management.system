import streamlit as st

# ----- PAGE CONFIG -----
st.set_page_config(
    page_title="Student Management System",
    page_icon="🎓",
    layout="centered"
)

# ----- DATABASE -----
if "students" not in st.session_state:
    st.session_state.students = ["yugesh", "kishor", "gajen", "Gopi"]

students = st.session_state.students

# ----- UI -----
st.title("🎓 Student Management System")
st.caption("Web-based application using Streamlit")

st.divider()

# ----- ADD STUDENT -----
st.subheader("Add Student")
new_student = st.text_input("Student Name")

if st.button("Add Student"):
    if new_student.strip() == "":
        st.warning("Please enter a student name")
    elif new_student in students:
        st.error("Student already exists")
    else:
        students.append(new_student)
        st.success(f"Student '{new_student}' added successfully")

st.divider()

# ----- SEARCH STUDENT -----
st.subheader("Search Student")
search_name = st.text_input("Search Name", key="search")

if st.button("Search"):
    if search_name in students:
        st.success(f"Student '{search_name}' found")
    else:
        st.error(f"Student '{search_name}' not found")

st.divider()

# ----- STUDENT LIST -----
st.subheader("Student List")

if students:
    for student in students:
        col1, col2 = st.columns([4, 1])
        col1.write(student)
        if col2.button("❌", key=student):
            students.remove(student)
            st.experimental_rerun()
else:
    st.info("No students available")

st.divider()
st.caption("Developed with Python & Streamlit")
