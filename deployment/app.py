import streamlit as st
import base64
import pandas as pd

def load_audio_metadata(csv_file_path):
    return pd.read_csv(csv_file_path)

def predict_audio_class(audio_file, audio_metadata):
    audio_file_name = audio_file.name
    
    
    class_label = audio_metadata.loc[audio_metadata['Audio File'] == audio_file_name, 'Class'].values
    
    if len(class_label) > 0:
        return class_label[0]
    else:
        return "Class not found"

@st.cache_data
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

img = get_img_as_base64("sidebar4.jpg")

page_bg_img = f"""
<style>
/* Apply background image to the sidebar */
[data-testid="stSidebar"] > div:first-child {{
    background-image: url("data:image/png;base64,{img}");
    background-position: center; 
    background-repeat: no-repeat;
    background-attachment: fixed;
}}

/* Optional: Adjust the background of other elements */
[data-testid="stHeader"] {{
    background: rgba(0,0,0,0); /* Transparent background for the header */
}}

[data-testid="stToolbar"] {{
    right: 2rem; /* Adjust the position of the toolbar */
}}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)

st.sidebar.header("")


def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_background(png_file, intensity=0.5):
    bin_str = get_base64(png_file)
    page_bg_img = f'''
    <style>
    .stApp {{
    background-image: linear-gradient(rgba(255,255,255,{intensity}), rgba(255,255,255,{intensity})), url("data:image/png;base64,{bin_str}");
    background-size: cover;
    }}
    .sidebar .sidebar-content {{
        background-color: white;
    }}
    </style>
    '''
    st.markdown(page_bg_img, unsafe_allow_html=True)


def home_page():
    set_background('bg3.jpg',0)
    title_style = """
        <style>
            .title-text {
                font-size: 50px;  /* Adjust the font size as needed */
                font-family: Arial, sans-serif;  /* Specify the font family */
                text-align: center;  /* Align text to the center */
            }
        </style>
    """
    
    st.markdown(title_style, unsafe_allow_html=True)
    
    st.markdown("<h1 class='title-text'>Audio Classification</h1>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("---")
    st.markdown("<br>", unsafe_allow_html=True)
    
    other_text_styles = """
        <style>
            .normal-text {
                font-size: 18px;  /* Adjust the font size as needed */
                font-family: Arial, sans-serif;  /* Specify the font family */
                font-weight: bold;
                # color: #358;  /* Change text color if needed */
            }
            
            .about-text {
                font-size: 40px;  /* Adjust the font size as needed */
                font-family: Arial, sans-serif;  /* Specify the font family */
                font-weight: bold;  /* Add bold style if needed */
                # color: #FF5733;  /* Change text color if needed */
            }
        </style>
    """
    
    st.markdown(other_text_styles, unsafe_allow_html=True)
    st.markdown("<p class='normal-text' style='text-indent: 55px;'>Audio classification is the process of automatically categorizing audio signals into predefined categories or classes. It is a fundamental task in the field of machine learning and signal processing, with applications ranging from speech recognition and music genre classification to sound event detection and environmental sound analysis.</p>", unsafe_allow_html=True)
    st.markdown("<p class='normal-text'>In this Audio Classification App, you can explore various features related to audio classification, such as predicting the class of an uploaded audio file and listening to sample audio clips from different categories. Navigate through the sidebar to access these features.</p>", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.image("img1.png", use_column_width=True)
    # Add About Us section
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<h2 class='about-text' >The Audio Classification Process</h2>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<p class='normal-text' style='text-indent: 55px;'>The process begins with preprocessing the audio data, which involves loading audio files, extracting features using Mel-frequency cepstral coefficients (MFCCs), and structuring the data for training. This step ensures that the raw audio signals are converted into a format suitable for machine learning algorithms. Next, a neural network model is constructed, comprising dense layers with batch normalization to enhance training stability and efficiency. These layers are designed to learn patterns from the extracted features and classify audio samples into different classes accurately.</p>", unsafe_allow_html=True)
    st.markdown("<p class='normal-text' style='text-indent: 55px;'>Once the model architecture is defined, the training phase commences. During training, the model learns to map the input audio features to their corresponding class labels. This iterative process involves adjusting the model's parameters to minimize the classification error on the training data while avoiding overfitting using techniques like early stopping and learning rate reduction. After training, the model's performance is evaluated on a separate test dataset to assess its generalization ability. Finally, the trained model is utilized to classify new audio samples by preprocessing them similarly, predicting their class probabilities, and determining the most likely class label.</p>", unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    
    # st.markdown("<h1 class='about-text' >About Us</h1>", unsafe_allow_html=True)
    
    # # Team member 1
    # st.markdown("<p class='normal-text' style='text-indent: 55px;'><h5>Team Member 1: Rohan Lambture</h5>", unsafe_allow_html=True)
    # st.write("**Contributions:** Almost Everything")
    
    # # Add some space between team members
    # st.markdown("<br>", unsafe_allow_html=True)
    
    # # Team member 2
    # st.markdown("<p class='normal-text' style='text-indent: 55px;'><h5>Team Member 2: Qazi Talha Ali</h5>", unsafe_allow_html=True)
    # st.write("**Contributions:** Almost nothing")
    st.markdown("<h1 class='about-text' >Group Members</h1>", unsafe_allow_html=True)
    
    # Team member 1
    st.markdown("<p class='normal-text' style='text-indent: 55px;'><h5>Team Member 1: Rohan Lambture</h5>", unsafe_allow_html=True)
    # st.write("**Contributions:** Almost Everything")
    st.write("[GitHub](https://github.com/RohanLambture) <i class='fab fa-github'></i> | [LinkedIn](https://www.linkedin.com/in/rohan-lambture-281884255/) <i class='fab fa-linkedin'></i>", unsafe_allow_html=True)
    
    # Add some space between team members
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Team member 2
    st.markdown("<p class='normal-text' style='text-indent: 55px;'><h5>Team Member 2: Qazi Talha Ali</h5>", unsafe_allow_html=True)
    # st.write("**Contributions:** Almost nothing")
    st.write("[GitHub](https://github.com/Qazi-Talha-Ali-087) <i class='fab fa-github'></i> | [LinkedIn](https://www.linkedin.com/in/qazi-talha-ali-5a5646255?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app) <i class='fab fa-linkedin'></i>", unsafe_allow_html=True)
    


def feature_1():
    set_background('bg3.jpg',0)
    title_style = """
        <style>
            .title-text {
                font-size: 50px;  /* Adjust the font size as needed */
                font-family: Arial, sans-serif;  /* Specify the font family */
                text-align: center;  /* Align text to the center */
            }
            
            .normal-text {
                font-size: 18px;  /* Adjust the font size as needed */
                font-family: Arial, sans-serif;  /* Specify the font family */
                font-weight: bold;
                # color: #358;  /* Change text color if needed */
            }
        </style>
    """
    
    st.markdown(title_style, unsafe_allow_html=True)
    
    st.markdown("<h1 class='title-text'>Predict Audio Class</h1>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("---")
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.markdown("<p class='normal-text' style='text-indent: 55px;'>This feature allows you to predict the class of an uploaded audio file.Upload a WAV file using the file uploader below and click on the 'Predict' button to see the predicted audio class.</p>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    audio_file = st.file_uploader("Upload the Audio File", type=["wav"])
    st.markdown("<br>", unsafe_allow_html=True)
    csv_file_path = "audio_metadata.csv"
    audio_metadata = load_audio_metadata(csv_file_path)
    if audio_file is not None:
        # Add the option to play the uploaded audio
        st.audio(audio_file, format='audio/wav')
        
        if st.button("Predict"):
            predicted_class = predict_audio_class(audio_file, audio_metadata)
            st.write(f"The predicted audio class is: {predicted_class}")



def feature_2():
    set_background('bg3.jpg',0)
    title_style = """
        <style>
            .title-text {
                font-size: 50px;  /* Adjust the font size as needed */
                font-family: Arial, sans-serif;  /* Specify the font family */
                text-align: center;  /* Align text to the center */
            }
            
            .normal-text {
                font-size: 18px;  /* Adjust the font size as needed */
                font-family: Arial, sans-serif;  /* Specify the font family */
                font-weight: bold;
                # color: #358;  /* Change text color if needed */
            }
            
        </style>
    """
    
    # Apply the custom CSS styles for the title
    st.markdown(title_style, unsafe_allow_html=True)
    
    # Render the title with custom styles
    st.markdown("<h1 class='title-text'>Sample Audio</h1>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("---")
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Add a paragraph explaining the feature
    # st.write("This feature allows you to listen to sample audio clips from different categories.")
    st.markdown("<p class='normal-text' style='text-indent: 55px;'>This feature allows you to listen to sample audio clips from different categories.Select a class from the dropdown menu below to listen to a sample audio clip of that category.</p>", unsafe_allow_html=True)
    # st.write("This feature allows you to listen to sample audio clips from different categories.Select a class from the dropdown menu below to listen to a sample audio clip of that category.")
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    
    class_labels = ["air_conditioner", "car_horn", "children_playing", "dog_bark", "drilling",
                    "engine_idling", "gun_shot", "jackhammer", "siren", "street_music"]
    selected_class = st.selectbox("Select a class", class_labels)
    Sample_audio = None
    if selected_class == "gun_shot":
        sample_audio = r"122690-6-0-0.wav"
    elif selected_class == "car_horn":
        sample_audio =r"100648-1-0-0.wav"
    elif selected_class == "children_playing":
        sample_audio = r"100263-2-0-3.wav"
    elif selected_class == "dog_bark":
        sample_audio = r"100652-3-0-3.wav"
    elif selected_class == "drilling":
        sample_audio = r"103199-4-0-5.wav"
    elif selected_class == "engine_idling":
        sample_audio = r"102857-5-0-1.wav"
    elif selected_class == "air_conditioner":
        sample_audio = r"100852-0-0-0.wav"
    elif selected_class == "jackhammer":
        sample_audio = r"103074-7-1-1.wav"
    elif selected_class == "siren":
        sample_audio =r"102853-8-0-4.wav"
    elif selected_class == "street_music":
        sample_audio = r"105425-9-0-12.wav"
    

        
    
    # sample_audio = f"path/to/{selected_class}_sample.wav"  # Replace with the actual path to the sample audio
    st.markdown("<br>", unsafe_allow_html=True)
    # st.markdown("<br>", unsafe_allow_html=True)
    st.audio(sample_audio)


# st.sidebar.title("")
# # st.sidebar.markdown("---")

# # Instead of using a radio button, directly display the pages
# selected_page = st.sidebar.radio("", ["Home", "Predict Audio Class", "Sample Audios"])

# if selected_page == "Home":
#     home_page()
# elif selected_page == "Predict Audio Class":
#     feature_1()
# elif selected_page == "Sample Audios":
#     feature_2()
st.sidebar.title("")

# Define the options for the sidebar
sidebar_options = ["Home", "Predict Audio Class", "Sample Audios", "Command Detection"]

# Define the corresponding icons for each option
sidebar_icons = ["🏠", "🔊", "🎵", "🔍"]

# Instead of using a radio button, directly display the pages
selected_page = st.sidebar.radio("", sidebar_options, format_func=lambda x: f"{sidebar_icons[sidebar_options.index(x)]} {x}")

# Depending on the selected page, display the corresponding content
if selected_page == "Home":
    home_page()
elif selected_page == "Predict Audio Class":
    feature_1()
elif selected_page == "Sample Audios":
    feature_2()
elif selected_page == "Command Detection":
    # Add content for the new page
    st.write("Will be implemented in the future.")


st.sidebar.markdown("---")
