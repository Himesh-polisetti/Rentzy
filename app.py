import streamlit as st
import pandas as pd
from modifydb import *

st.set_page_config(page_title="Rentzy", layout="wide")

# ---------------- SESSION ----------------
if "page" not in st.session_state:
    st.session_state.page = "home"
if "user" not in st.session_state:
    st.session_state.user = None
if "role" not in st.session_state:
    st.session_state.role = None

# ---------------- HOME ----------------
def home():
    st.title("🏠 Rentzy")
    st.write("Peer-to-peer rental platform")

    if st.button("Get Started"):
        st.session_state.page = "auth"
        st.rerun()

# ---------------- AUTH ----------------
def auth():
    st.title("Login / Signup")

    role = st.radio("Role", ["Owner", "Consumer"])
    name = st.text_input("Name")
    mobile = st.text_input("Mobile")
    email = st.text_input("Email")
    aadhar = st.text_input("Aadhar")

    if st.button("Continue"):
        if not all([name, mobile, email, aadhar]):
            st.error("Fill all fields")
        else:
            user = get_user_by_mobile(mobile)
            if not user:
                add_user(name, mobile, email, aadhar, role)
                user = get_user_by_mobile(mobile)

            st.session_state.user = user
            st.session_state.role = role
            st.session_state.page = "dashboard"
            st.rerun()

# ---------------- DASHBOARD ----------------
def dashboard():
    user = st.session_state.user

    st.title(f"Welcome {user['name']} 👋")

    tabs = st.tabs(["Browse", "Add Item", "Requests"])

    # -------- Browse --------
    with tabs[0]:
        st.subheader("Available Items")
        items = get_items()

        for item in items:
            st.write(item)

            if st.session_state.role == "Consumer":
                if st.button("Request", key=item["id"]):
                    add_request(item["id"], user["name"], item["owner"])
                    st.success("Requested!")

    # -------- Add Item --------
    with tabs[1]:
        if st.session_state.role != "Owner":
            st.warning("Only owners can add items")
        else:
            name = st.text_input("Item Name")
            category = st.selectbox("Category", ["Electronics", "Furniture"])
            location = st.text_input("Location")
            rent = st.number_input("Rent")

            if st.button("Add Item"):
                add_item(name, category, location, rent, user["name"])
                st.success("Item added!")

    # -------- Requests --------
    with tabs[2]:
        requests = get_requests_for_user(user["name"])

        for r in requests:
            st.write(r)

            if r["owner"] == user["name"] and r["status"] == "Pending":
                if st.button("Approve", key=f"a{r['id']}"):
                    update_request_status(r["id"], "Approved")
                    st.rerun()

                if st.button("Reject", key=f"r{r['id']}"):
                    update_request_status(r["id"], "Rejected")
                    st.rerun()

# ---------------- ROUTER ----------------
if st.session_state.page == "home":
    home()
elif st.session_state.page == "auth":
    auth()
else:
    dashboard()