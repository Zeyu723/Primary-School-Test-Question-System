from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/grade1/math")
def grade1_math():
    return render_template("grade1_math.html")

@app.route("/grade1/english")
def grade1_english():
    return render_template("grade1_english.html")

@app.route("/grade2/math")
def grade2_math():
    return render_template("grade2_math.html")

@app.route("/grade2/english")
def grade2_english():
    return render_template("grade2_english.html")

@app.route("/grade3/math")
def grade3_math():
    return render_template("grade3_math.html")

@app.route("/grade3/english")
def grade3_english():
    return render_template("grade3_english.html")

@app.route("/grade4/math")
def grade4_math():
    return render_template("grade4_math.html")

@app.route("/grade4/english")
def grade4_english():
    return render_template("grade4_english.html")

@app.route("/grade5/math")
def grade5_math():
    return render_template("grade5_math.html")

@app.route("/grade5/math/gate")
def grade5_math_gate():
    return render_template("grade5_math_gate.html")

@app.route("/grade5/english")
def grade5_english():
    return render_template("grade5_english.html")

@app.route("/grade5~6/english")
def grade5_6_english():
    return render_template("grade5~6_english.html")

@app.route("/grade6/math")
def grade6_math_gate():
    return render_template("grade6_math.html")

@app.route("/grade6/english")
def grade6_english():
    return render_template("grade6_english.html")

@app.route("/unlock/your/potential/english")
def unlock_potential_english():
    return render_template("unlock_potential_english.html")
    
@app.route("/unlock/your/potential/math")
def unlock_potential_math():
    return render_template("unlock_potential_math.html")

@app.route("/about")
def about():
    return render_template("about.html")
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # 从环境变量读取 Render 提供的端口
    app.run(host="0.0.0.0", port=port)