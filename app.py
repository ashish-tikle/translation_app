import streamlit as st
from googletrans import Translator

# Function to translate text
def translate_text(text, from_lang, to_lang):
    # Initialize Translator object
    translator = Translator()

    # Translate text
    translated_text = translator.translate(text, src=from_lang, dest=to_lang)

    # Return translated text
    return translated_text.text


# Streamlit app layout
def main():
    st.title("Simple Translation App")

    # Language selection
    from_lang = st.selectbox("From Language", ["English"])
    to_lang = st.selectbox("To Language", ["German", "Italian"])

    # Domain selection (currently not implemented)
    domain = st.selectbox("Domain", ["Technology"])

    # Input text
    input_text = st.text_area("Enter text to translate")

    # Translate button
    if st.button("Translate"):
        if input_text:
            translated_text = translate_text(input_text, from_lang, to_lang)
            st.success(translated_text)
        else:
            st.warning("Please enter text to translate.")

if __name__ == "__main__":
    main()
