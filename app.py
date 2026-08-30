
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

@app.route("/image", methods=["GET", "POST"])
def image_analysis():
    if request.method == "POST":
        # Handle uploaded image
        uploaded_file = request.files.get("image")
        if uploaded_file and uploaded_file.filename:
            # Save to static/uploads (ensure directory exists)
            import os
            upload_dir = os.path.join(app.root_path, "static", "uploads")
            os.makedirs(upload_dir, exist_ok=True)
            save_path = os.path.join(upload_dir, uploaded_file.filename)
            uploaded_file.save(save_path)
            # For now, just display the uploaded image and a placeholder result
            rel_path = f"uploads/{uploaded_file.filename}"
            return render_template("image_result.html", image_path=rel_path)
        else:
            return render_template("image_form.html", error="Please select an image to upload.")
    # GET request – show upload form
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
