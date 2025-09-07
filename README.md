# faq_chatbot
Iron Lady Chatbot

This project is a simple FAQ + AI-powered chatbot built using Flask and Hugging Face Transformers.
It answers frequently asked questions about Iron Lady’s leadership programs and uses a local NLP model for open-ended queries.

🚀 Features

Predefined FAQs for quick and accurate answers.

AI-based responses using Hugging Face distilgpt2 model for unrecognized queries.

Flask backend with API endpoints.

Simple web interface (index.html) to interact with the chatbot.

🛠️ Tech Stack

Python 3.8+

Flask (Web framework)

Transformers (Hugging Face NLP models)

HTML + JavaScript (Frontend)

📂 Project Structure
.
├── app.py          # Flask backend with chatbot logic
├── templates/
   └── index.html  # Frontend UI


⚙️ Installation

Clone the repository

git clone https://github.com/sindhuspatil112/iron-lady-chatbot.git
cd iron-lady-chatbot


Create a virtual environment (recommended)

python -m venv venv
source venv/bin/activate    # macOS/Linux
venv\Scripts\activate       # Windows


Install dependencies

pip install flask transformers

▶️ Usage

Run the Flask app

python app.py


Open your browser and go to:

http://127.0.0.1:5000/


Start chatting with the bot!

📜 License

This project is licensed under the MIT License.
