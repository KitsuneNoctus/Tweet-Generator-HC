from bson.objectid import ObjectId
from flask import Flask, render_template, request, redirect, url_for
import os
import word_probability

app = Flask(__name__)

@app.route('/')
def index():
    """Return homepage."""
    return word_probability.pick_one_word(word_probability.calc_probability(word_probability.convert_histogram()))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))
