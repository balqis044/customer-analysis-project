from flask import Flask, request, render_template
import os
from analysis import run_analysis

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

@app.route("/", methods=["GET", "POST"])
def index():
    table = None

    if request.method == "POST":
        file = request.files['file']

        if file:
            filepath = os.path.join("uploads", file.filename)
            file.save(filepath)

            result = run_analysis(filepath)
            table = result.to_html(classes='table')

    return render_template("index.html", table=table)

if __name__ == "__main__":
    app.run(debug=True)