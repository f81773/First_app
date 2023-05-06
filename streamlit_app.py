import openai
import streamlit as st
from pathlib import Path
import configparser


fpath = Path('config.txt')
cfg_reader = configparser.ConfigParser()
cfg_reader.read(str(fpath))
openai.api_key = cfg_reader.get('API_KEY','OPENAI_API_KEY')


def suggest_career_from_chatgpt(prompt):
    prompt = f"Based on your interests and skills, suggest a career path: {prompt}"
    try:
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            temperature=0.5,
            max_tokens=1024,
            n=1,
            stop=None,
            timeout=15,
        )
        career = response.choices[0].text.strip()
    except Exception as e:
        st.error(f"Error processing suggestion: {e}")
        career = None
    return career

st.title("Smart career counseling app")

model = "text-davinci-002"

text1 = st.text_input("What are your primary interests and passions?", placeholder="Try to write a complete sentece")
text2 = st.text_input("What are your top skills and areas of expertise?", placeholder="Try to write a complete sentece")
text3 = st.text_input("What type of work environment do you prefer?", placeholder="Try to write a complete sentece")
text4 = st.text_input("What is your preferred work schedule (e.g. full-time, part-time, flexible hours)?", placeholder="Try to write a complete sentece")
text5 = st.text_input("Do you have any specific career goals or aspirations?", placeholder="Try to write a complete sentece")
text6 = st.text_input("What kind of tasks or activities do you enjoy most?", placeholder="Try to write a complete sentece")
text7 = st.text_input("What are your strongest personality traits?", placeholder="Try to write a complete sentece")
text8 = st.text_input("Are you comfortable working independently or do you prefer working as part of a team?:", placeholder="Try to write a complete sentece")
text9 = st.text_input("What is your educational background and level of experience in the workforce?", placeholder="Try to write a complete sentece")
text10 = st.text_input("What are your salary expectations and desired benefits?", placeholder="Try to write a complete sentece")

prompt = [text2, text3, text4, text5, text6, text7, text8, text9, text10]

if st.button("submit"):
    with st.spinner("processing"):
        suggest = suggest_career_from_chatgpt(prompt)
        if suggest is not None:
            st.success("data sent")
        else:
            st.error("Failed to get suggestion")

    st.write(f"suggested: {suggest}")
