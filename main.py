import streamlit as st
from few_shot import FewShotPosts
from post_generator import generate_post, generate_image_prompt


# Options for length and language
length_options = ["Short", "Medium", "Long"]
language_options = ["English", "Hinglish"]


# Main app layout
def main():
    st.subheader("LinkedIn Post Generator: Codebasics")

    # Create three columns for the dropdowns
    col1, col2, col3 = st.columns(3)

    fs = FewShotPosts()
    tags = fs.get_tags()
    with col1:
        # Dropdown for Topic (Tags)
        selected_tag = st.selectbox("Topic", options=tags)

    with col2:
        # Dropdown for Length
        selected_length = st.selectbox("Length", options=length_options)

    with col3:
        # Dropdown for Language
        selected_language = st.selectbox("Language", options=language_options)



    # Generate Button
    if st.button("Generate"):
        post = generate_post(selected_length, selected_language, selected_tag)
        st.subheader("Generated Post:")
        st.write(post)
        
        # Generate image prompt
        with st.spinner("Generating image prompt..."):
            image_prompt = generate_image_prompt(post, selected_tag)
        
        st.subheader("AI Image Prompt:")
        st.info(image_prompt)
        st.caption("Copy this prompt and use it with DALL-E, Midjourney, Stable Diffusion, or any AI image generator.")


# Run the app
if __name__ == "__main__":
    main()
