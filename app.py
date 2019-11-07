from bson.objectid import ObjectId
from flask import Flask, render_template, request, redirect, url_for
import os
from word_probability import pick_one_word, calc_probability, convert_histogram


app = Flask(__name__)

@app.route('/')
def index():
    """Return homepage."""
    return pick_one_word(calc_probability(convert_histogram()))
    # word_probability.pick_one_word(word_probability.calc_probability(word_probability.convert_histogram()))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))
