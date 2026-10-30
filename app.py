from flask import Flask, render_template, request, jsonify

app = Flask(
    __name__,
    template_folder="templates",
    static_folder="templates/static",
    static_url_path="/static"
)

# College enquiry responses
college_data = {
    "admission": (
        "Admission Enquiry",
        "Welcome to our college! Admissions are available for eligible students. "
        "You can contact the admission department for application forms, "
        "important dates and counselling details."
    ),

    "course": (
        "Courses Offered",
        "Our college offers various programs including B.Tech in Computer "
        "Science, Mechanical Engineering, Civil Engineering, Electrical "
        "Engineering and other branches. Contact the college for the latest list."
    ),

    "fee": (
        "Fee Structure",
        "The fee depends on the selected course and category. "
        "Please contact the accounts department for the latest fee structure."
    ),

    "eligibility": (
        "Eligibility",
        "For B.Tech admission, students generally need to have passed "
        "10+2 with the required subjects and meet applicable admission criteria."
    ),

    "placement": (
        "Placement Information",
        "Our placement department helps students with training, internships "
        "and campus recruitment opportunities."
    ),

    "scholarship": (
        "Scholarship Information",
        "Eligible students may apply for scholarships according to "
        "government and institutional rules."
    ),

    "contact": (
        "Contact Information",
        "For college enquiries, please contact the college administration "
        "or visit the official college website."
    )
}


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()

    if not data or not data.get("message", "").strip():
        return jsonify({
            "reply": "Please type your question first."
        }), 400

    message = data["message"].lower().strip()

    # Find matching enquiry
    for keyword, response in college_data.items():
        if keyword in message:
            return jsonify({
                "reply": response[1]
            })

    # Additional keyword matching
    if "hi" in message or "hello" in message or "hey" in message:
        reply = "Hello! Welcome to College Enquiry Bot. How can I help you?"

    elif "course" in message or "branch" in message:
        reply = college_data["course"][1]

    elif "fee" in message or "fees" in message:
        reply = college_data["fee"][1]

    elif "admission" in message:
        reply = college_data["admission"][1]

    else:
        reply = (
            "Sorry, I could not understand your question. "
            "Please ask about Admission, Courses, Fees, Eligibility, "
            "Placement or Scholarship."
        )

    return jsonify({"reply": reply})


@app.route("/health")
def health():
    return jsonify({
        "status": "online",
        "message": "College Enquiry Bot backend is running!"
    })


if __name__ == "__main__":
    app.run(debug=True)