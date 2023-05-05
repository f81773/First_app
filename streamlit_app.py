import openai
import streamlit as st

openai.api_key = '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'

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
prompt = st.text_input("Enter Text:", value= "write something")

if st.button("submite"):
    with st.spinner("processing"):
        sugest = suggest_career_from_chatgpt(prompt)
        st.succes("data sent")

    st.write(f"sugetsted: {sugest}")
