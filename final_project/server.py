from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route('/englishToFrench')
def english_to_french():
    english_text = request.args.get('text')
    french_text = englishToFrench(english_text)
    return french_text

@app.route('/frenchToEnglish')
def french_to_english():
    french_text = request.args.get('text')
    english_text = frenchToEnglish(french_text)
    return english_text


@app.route("/")
def renderIndexPage():
    # Write the code to render template

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
