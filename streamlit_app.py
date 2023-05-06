import openai
import streamlit as st

openai.api_key = "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"

def suggest_career_from_chatgpt(prompt):
    prompt = f"Based on your interests and skills, suggest a career path: {prompt}"
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
    return career

st.title("Smart career counseling app")
model = "text-davinci-002"
prompt = st.text_input("Enter Text:", value="write something")

if st.button("submit"):
    with st.spinner("processing"):
        suggest = suggest_career_from_chatgpt(prompt)
        st.success("data sent")

    st.write(f"suggested: {suggest}")
