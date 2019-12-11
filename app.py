from bson.objectid import ObjectId
from flask import Flask, render_template, request, redirect, url_for
import os
from word_probability import pick_one_word, calc_probability, convert_histogram
from word_frequency import get_words
from dictogram import Dictogram
from create_sentence import created_sentence


app = Flask(__name__)

# def create_random_sentence(sen_length):
#     dict_histogram = Dictogram(get_words())
#     sentence = ""
#     while sen_length != 0:
#         if sen_length == 1:
#             sentence += dict_histogram.sample()
#         else:
#             sentence += (dict_histogram.sample() + " ")
#         sen_length -= 1
#
#     return sentence

@app.route('/')
def index():
    """Return homepage."""
    generate_sentence = created_sentence()
    sentence = generate_sentence.make_sentence(True)
    return render_template("index.html", sentence=sentence)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))
