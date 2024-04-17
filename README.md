### TalkMate: Multilingual AI Assistant

TalkMate is a web-based AI assistant that can communicate with users in multiple languages. It provides a seamless conversational experience, allowing users to interact with it through voice input and receive responses in text and audio formats.

![Screenshot 2024-04-17 183745](https://github.com/Rafe2001/TalkMate-Multilingual-AI-Assistant/assets/108533597/65b8217c-5a67-4e96-baff-2766454b370a)
![image](https://github.com/Rafe2001/TalkMate-Multilingual-AI-Assistant/assets/108533597/e51b21a9-3ac8-4805-bfc4-5ce6d7e65fdb)
![image](https://github.com/Rafe2001/TalkMate-Multilingual-AI-Assistant/assets/108533597/57c65023-1c79-4ae7-826e-79df0d2833e9)

#### Features:
- **Multilingual Support**: TalkMate supports multiple languages, enabling users to converse with the AI assistant in their preferred language.
- **Voice Input**: Users can speak to TalkMate using their microphone, and the assistant will convert their speech into text for processing.
- **Text-to-Speech Conversion**: TalkMate can convert its responses into speech audio files, allowing users to listen to the assistant's replies.
- **Web Interface**: The AI assistant is accessible through a web interface, making it easy to use across different devices and platforms.
- **Streamlined Interaction**: With intuitive buttons and text input fields, TalkMate offers a user-friendly interface for interacting with the AI assistant.

#### Technologies Used:
- **SpeechRecognition**: Enables speech recognition functionality for capturing user input via microphone.
- **gTTS (Google Text-to-Speech)**: Provides text-to-speech conversion capabilities for generating audio responses.
- **Google Generative AI**: Utilizes Google's Generative AI models, such as Gemini, for natural language processing tasks.
- **Flask**: Powers the backend server for handling HTTP requests and serving web pages.
- **Streamlit**: Facilitates the creation of the web-based user interface for TalkMate.
- **Python-dotenv**: Manages environment variables, including sensitive information like API keys.

#### Usage:
1. Open the TalkMate web application in your browser.
2. Click on the "Ask me..." button to activate the AI assistant.
3. Speak into your microphone to provide input or type your message in the text input field.
4. TalkMate will process your input and generate a response.
5. You can view the response in the text area and listen to it as an audio file.
6. Optionally, download the speech audio file for offline listening.

#### Installation:
1. Clone the TalkMate repository to your local machine.
2. Install the required dependencies listed in the `requirements.txt` file using `pip install -r requirements.txt`.
3. Run the Flask server by executing `python main.py`.
4. Access the TalkMate web interface in your browser at `http://localhost:5000`.

#### Future Enhancements:
- Support for additional languages and dialects.
- Integration with third-party APIs for expanded functionality.
- Enhanced user interface with more interactive elements and customization options.

#### License:
This project is licensed under the [License Name] License - see the [LICENSE.md](LICENSE.md) file for details.
