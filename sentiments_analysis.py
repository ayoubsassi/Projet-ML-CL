"""
# Create a form to group text_input and button together
with st.form("sentiment_form"):
    # Text input for user
    text = st.text_input("Enter your sentence!")

    # Button to perform sentiment analysis
    submit_button = st.form_submit_button("Submit")

# Perform sentiment analysis when the form is submitted
if submit_button:
    # Perform sentiment analysis
    result = classification(text)
    
    # Display the result
    st.write(f"Sentiment: {result[0]['label']} (Confidence: {result[0]['score']:.2f})")"""

from transformers import pipeline
import streamlit as st
import speech_recognition as sr

# create pipeline for sentiment analysis
classification = pipeline('sentiment-analysis')

#print(classification("Palestine is a nice country"))

st.title("Sentiment Analysis Platform")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
#for message in st.session_state.messages:
    #with st.chat_message(message["role"]):
        #st.markdown(message["content"])


# Define the custom CSS
custom_css = """
<style>
.mic_button {
    position: fixed;
    bottom: 715px;
    left: 33px;
}
</style>
"""

text=st.text_input("Enter your sentence !")

# Text input widget to allow users to write
#user_input = st.text_area("Write something here:")
result=classification(text)

# Button to submit the text
button_submit=st.button("Submit")
if button_submit:
    #st.success(f"You submitted: {text}")
    st.write(f"Sentiment: {result[0]['label']} (Confidence: {result[0]['score']:.2f})")



# Speak button
mic_button= st.button("🎙️", help='Click on the button to Speak', key="mic_button")
if mic_button:
    # Apply the custom CSS
    st.markdown(custom_css, unsafe_allow_html=True)
    st.markdown('<div class="mic_button">Button Clicked!</div>', unsafe_allow_html=True)

    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        st.info("Speak your prompt...")
        audio = recognizer.listen(source)
        st.success("Recording completed!")
        st.info("Processing...")
        st.text_input(audio)
        

    try:
        prompt = recognizer.recognize_google(audio)
        voc=classification(prompt)
        st.write(f"Sentiment: {voc[0]['label']} (Confidence: {voc[0]['score']:.2f})")
    except sr.UnknownValueError:
        st.error("Sorry, I couldn't understand your speech.")
    except sr.RequestError as e:
        st.error(f"Could not request results from Google Speech Recognition service; {e}")
st.write("</div>", unsafe_allow_html=True)







