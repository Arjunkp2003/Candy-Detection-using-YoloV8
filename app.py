import streamlit as st
import sqlite3
import hashlib
from PIL import Image
import tempfile
from ultralytics import YOLO

# ======================= AUTH SYSTEM ============================
def create_users_table():
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (
                    username TEXT PRIMARY KEY,
                    password TEXT
                )''')
    conn.commit()
    conn.close()

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register_user(username, password):
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    try:
        c.execute("INSERT INTO users (username, password) VALUES (?, ?)", 
                  (username, hash_password(password)))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()

def login_user(username, password):
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username = ? AND password = ?", 
              (username, hash_password(password)))
    result = c.fetchone()
    conn.close()
    return result is not None

# ======================= YOLO DETECTION =========================
def detect_candies(image_path):
    model = YOLO("best.pt")  # Or your custom model path
    results = model(image_path)[0]
    return results.plot()

# ======================= STREAMLIT UI ===========================
st.set_page_config(page_title="Candy Detection", page_icon="🍬")
create_users_table()

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

menu = st.sidebar.radio("Navigation", ["Home", "Login", "Register", "Detect Candies"])

# ------------------ HOME PAGE -------------------
if menu == "Home":
    st.title("🍬 Candy Detection with YOLOv8")
    st.write("This app lets you register, log in, and detect candies in images using a YOLOv8 model.")
    st.image("https://tse1.mm.bing.net/th?id=OIP.rxPTZ9ULq2EpV4Y-A_xiAgHaEK&pid=Api&P=0&h=180",  use_container_width=True)

# ------------------ LOGIN -----------------------
elif menu == "Login":
    st.subheader("🔐 Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if login_user(username, password):
            st.success("Login successful!")
            st.session_state.logged_in = True
            st.session_state.username = username
        else:
            st.error("Invalid credentials.")

# ------------------ REGISTER --------------------
elif menu == "Register":
    st.subheader("📝 Register")
    new_user = st.text_input("Choose a Username")
    new_password = st.text_input("Choose a Password", type="password")
    if st.button("Register"):
        if register_user(new_user, new_password):
            st.success("Registration successful. Please login.")
        else:
            st.error("Username already exists. Try another.")

# ------------------ PREDICT ---------------------
elif menu == "Detect Candies":
    if st.session_state.logged_in:
        st.subheader("🍭 Candy Detection")
        uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
        if uploaded_file:
            img = Image.open(uploaded_file)
            st.image(img, caption="Uploaded Image",  use_container_width=True)

            with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmp_file:
                img.save(tmp_file.name)
                output_img = detect_candies(tmp_file.name)
                st.image(output_img, caption="Detection Result",  use_container_width=True)
    else:
        st.warning("Please login to access the detection feature.")
