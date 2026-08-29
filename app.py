
from flask import Flask, render_template, request

from services.query_router import route_question


app = Flask(__name__)


# ==================================================
# HOME
# ==================================================

@app.route("/")
def home():
    return render_template("home.html")


# ==================================================
# TEXT ANALYSIS
# ==================================================

@app.route("/text", methods=["GET", "POST"])
def text_analysis():

    if request.method == "POST":

        question = request.form.get("question", "").strip()

        if not question:
            return render_template(
                "text_form.html",
                error="Please enter a question."
            )

        result = route_question(question)

        return render_template(
            "result.html",
            question=question,
            result=result
        )

    return render_template("text_form.html")


# ==================================================
# IMAGE ANALYSIS
# ==================================================

@app.route("/image")
def image_analysis():
    return render_template("image_form.html")


# ==================================================
# RUN
# ==================================================

if __name__ == "__main__":
    app.run(
        debug=True,
        host="127.0.0.1",
        port=5000
    )
