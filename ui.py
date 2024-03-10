from email_messenger.messenger import sendmessage
import api
import os
import streamlit as st
from dotenv import load_dotenv
import common.prompt
import time


# Load environment variables
load_dotenv()
api_host = os.environ.get("HOST", "api")
api_port = int(os.environ.get("PORT", 8080))

# Streamlit UI elements
st.title("Gmail + Whatsapp Smart Messenger")

fail = 0
try: import pyautogui
except : fail =1

if fail == 1:
    import webbrowser as web
    question1 = st.text_input(
        "Anything you wanna convey? Type it in !!",
        placeholder="Type Here",
        key="query"
    )

    email = st.text_input(
        "Email:",
        placeholder="Type in here"
    )

    phone = st.text_input(
        "Phone No:",
        placeholder="Type in here"
    )

    if question1 and email and phone:
        url = f'http://{api_host}:{api_port}/'
        data = {"query": question1}

        embedded_query = api.embed_query(question1)
        response = common.prompt.prompt(embedded_query)
        sendmessage(email, response)

        if response:
            st.write("### Okay,Forwarding the following through Gmail and Whatsapp\n")
            st.write(response)
            time.sleep(10)
            web.open(f"https://web.whatsapp.com/send?phone={phone}&text={response}")
        else:
            st.error(f"Failed to send data to backend. Status code: {response.status_code}")
    elif question1 and email and not phone:
        url = f'http://{api_host}:{api_port}/'
        data = {"query": question1}

        embedded_query = api.embed_query(question1)
        response = common.prompt.prompt(embedded_query)
        sendmessage(email, response)

        if response:
            st.write("### Okay,Forwarding the following through Gmail\n")
            st.write(response)
        else:
            st.error(f"Failed to send data to Pathway API. Status code: {response.status_code}")
    elif question1 and phone and not email:
        url = f'http://{api_host}:{api_port}/'
        data = {"query": question1}

        embedded_query = api.embed_query(question1)
        response = common.prompt.prompt(embedded_query)

        if response:
            st.write("### Okay,Forwarding the following through Whatsapp\n")
            st.write(response)
            time.sleep(10)
            web.open(f"https://web.whatsapp.com/send?phone={phone}&text={response}")
        else:
            st.error(f"Failed to send data to backend. Status code: {response.status_code}")
    elif question1 and not email and not phone:
        url = f'http://{api_host}:{api_port}/'
        data = {"query": question1}

        embedded_query = api.embed_query(question1)
        response = common.prompt.prompt(embedded_query)

        if response:
            st.write("### Answer\n")
            st.write(response)
            st.write("\n If you are satisfied with the response, you might prefer to email or Whatsapp this.")
        else:
            st.error(f"Failed to send data to Pathway API. Status code: {response.status_code}")

elif fail == 0:
    import whatsapp_messenger.messenger
    question1 = st.text_input(
        "Anything you wanna convey? Type it in !!",
        placeholder="Type Here",
        key="query2"
    )

    email = st.text_input(
        "Email:",
        placeholder="Type in here",
        key="email2"
    )

    phone = st.text_input(
        "Phone No:",
        placeholder="Type in here"
    )

    if question1 and email and phone:
        url = f'http://{api_host}:{api_port}/'
        data = {"query": question1}

        embedded_query = api.embed_query(question1)
        response = common.prompt.prompt(embedded_query)
        sendmessage(email, response)

        if response:
            st.write("### Okay,Forwarding the following through Gmail and Whatsapp\n")
            st.write(response)
            time.sleep(10)
            whatsapp_messenger.messenger.sendmessage(phone, response)
        else:
            st.error(f"Failed to send data to backend. Status code: {response.status_code}")
    elif question1 and email and not phone:
        url = f'http://{api_host}:{api_port}/'
        data = {"query": question1}

        embedded_query = api.embed_query(question1)
        response = common.prompt.prompt(embedded_query)
        sendmessage(email, response)

        if response:
            st.write("### Okay,Forwarding the following through Gmail\n")
            st.write(response)
        else:
            st.error(f"Failed to send data to Pathway API. Status code: {response.status_code}")
    elif question1 and phone and not email:
        url = f'http://{api_host}:{api_port}/'
        data = {"query": question1}

        embedded_query = api.embed_query(question1)
        response = common.prompt.prompt(embedded_query)

        if response:
            st.write("### Okay,Forwarding the following through Whatsapp\n")
            st.write(response)
            time.sleep(10)
            whatsapp_messenger.messenger.sendmessage(phone, response)
        else:
            st.error(f"Failed to send data to backend. Status code: {response.status_code}")
    elif question1 and not email and not phone:
        url = f'http://{api_host}:{api_port}/'
        data = {"query": question1}

        embedded_query = api.embed_query(question1)
        response = common.prompt.prompt(embedded_query)

        if response:
            st.write("### Answer\n")
            st.write(response)
            st.write("\n If you are satisfied with the response, you might prefer to email or Whatsapp this.")
        else:
            st.error(f"Failed to send data to Pathway API. Status code: {response.status_code}")
