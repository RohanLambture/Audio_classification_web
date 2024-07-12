# Audio Classification Streamlit App

This is a Streamlit web application for audio classification. The app allows users to upload an audio file and predict its class using a pre-trained deep learning model. Additionally, users can listen to sample audio clips from different categories.

## Features

- **Home Page**: Introduction to the audio classification process and overview of the app.
- **Predict Audio Class**: Upload a WAV audio file and predict its class.
- **Sample Audios**: Listen to sample audio clips from different categories.

## Getting Started

### Prerequisites

- Python 
- Required Python libraries: `streamlit`, `base64`, `pandas`, `numpy`, `librosa`, `tensorflow`

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/RohanLambture/Audio_classification_web.git
    cd Audio_classification_web
    ```

2. Install the required libraries:
    ```bash
    pip install -r requirements.txt
    ```

### Running the App

1. Make sure the pre-trained model (`model.h5`) and the necessary image files (`sidebar4.jpg`, `bg3.jpg`, `img1.png`) are in the project directory.

2. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```

3. Open your web browser and navigate to `http://localhost:8501` to view the app.

## File Structure

- `app.py`: The main Streamlit app code.
- `model.h5`: The pre-trained TensorFlow model for audio classification.
- `sidebar4.jpg`, `bg3.jpg`, `img1.png`: Image files used in the app for styling and display.
- `.wav` files: Sample audio files used for demonstration.
- `requirements.txt`: List of required Python libraries.
- `vercel.json`: Configuration file for deploying on Vercel (if applicable).

## Usage

### Home Page

The Home page provides an overview of the audio classification process and the app. It includes a brief description and some background information on audio classification.

### Predict Audio Class

1. Navigate to the "Predict Audio Class" page using the sidebar.
2. Upload a WAV audio file using the file uploader.
3. Click the "Predict" button to see the predicted audio class.

### Sample Audios

1. Navigate to the "Sample Audios" page using the sidebar.
2. Select a class from the dropdown menu to listen to a sample audio clip of that category.

## Authors

- Rohan Lambture ([GitHub](https://github.com/RohanLambture), [LinkedIn](https://www.linkedin.com/in/rohan-lambture-281884255/))
- Qazi Talha Ali ([GitHub](https://github.com/Qazi-Talha-Ali-087), [LinkedIn](https://www.linkedin.com/in/qazi-talha-ali-5a5646255))



