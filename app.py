from flask import Flask, render_template, request
from langdetect import detect

app = Flask(name)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/index1')
def result():
    # Process result data if needed
    return render_template('index1.html')


@app.route('/detect_language', methods=['POST'])
def detect_language():
    input_text = request.form['input_text']
    detected_language = detect(input_text)
    return render_template('index1.html', detected_language=detected_language)

if name == 'main':
    app.run(debug=True)
