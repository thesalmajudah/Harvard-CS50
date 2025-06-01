from flask import Flask, render_template, request
from personality import get_result

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/quiz', methods=["GET", "POST"])
def quiz():
    if request.method == "POST":
        selections = request.form.get("selections", "")
        result_name, result_description, result_image = get_result(selections)
        return render_template("result.html", result_name=result_name, result_description=result_description, result_image=result_image)
    return render_template("quiz.html")

if __name__ == '__main__':
    app.run(debug=True)
