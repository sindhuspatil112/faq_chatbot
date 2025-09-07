
from flask import Flask, render_template, request, jsonify
from transformers import pipeline

app = Flask(__name__)

chatbot = pipeline("text-generation", model="distilgpt2")



faqs = {
    "programs": "Iron Lady offers leadership programs focused on women empowerment, confidence building, and workplace growth.",
    "duration": "The program duration varies, but most leadership programs run for 8–12 weeks.",
    "mode": "The programs are conducted online with live interactive sessions.",
    "certificate": "Yes, participants receive a certificate upon successful completion.",
    "mentors": "The mentors include experienced corporate leaders, certified coaches, and industry experts."
}
def ask_local_model(question):
    try:
        response = chatbot(question, max_length=100, num_return_sequences=1)
        # response is a list of dicts like [{'generated_text': '...'}]
        if isinstance(response, list) and "generated_text" in response[0]:
            return response[0]["generated_text"]
        return str(response)
    except Exception as e:
        return f"⚠️ Error using local model: {e}"


    # if response.status_code == 200:
    #     data = response.json()
    #     print("HF response:", data)  # debug print

    #     # Case 1: list with generated_text
    #     if isinstance(data, list) and "generated_text" in data[0]:
    #         return data[0]["generated_text"]

    #     # Case 2: direct dict (some models)
    #     if isinstance(data, dict) and "generated_text" in data:
    #         return data["generated_text"]

    #     # If no text found, return raw response
    #     return str(data)
    # elif response.status_code == 503:  # model loading
    #     return "⏳ The model is loading, please try again in a few seconds..."
    # elif response.status_code == 504:  # timeout
    #     return "⚠️ The request timed out. Please try again."
    # else:
    #     return f"Error: {response.status_code} - {response.text}"



@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message", "").lower()
    
    if "program" in user_message:
        answer = faqs["programs"]
    elif "duration" in user_message:
        answer = faqs["duration"]
    elif "online" in user_message or "offline" in user_message or "mode" in user_message:
        answer = faqs["mode"]
    elif "certificate" in user_message:
        answer = faqs["certificate"]
    elif "mentor" in user_message or "coach" in user_message:
        answer = faqs["mentors"]
    else:
        answer = ask_local_model(user_message)

    return jsonify({"reply": answer})

if __name__ == "__main__":
    app.run(debug=True)
