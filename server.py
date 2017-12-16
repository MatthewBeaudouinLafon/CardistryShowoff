"""
A Flask server to run Showoff

author : Matthew Beaudouin-Lafon
date   : 2017-11-19
license: MIT
"""
import os
from random import sample
from categories import categories, modifiers

from flask import Flask, render_template, request
app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0 # Deal with CSS getting cached during dev

# TODO: Taunting Modify button

@app.route('/', methods=['GET', 'POST'])
def main():
	category = ''
	modifier = ''
	if request.method == 'POST':
		print(request.form)
		if request.form.get('new_category', None):
			category = sample(list(categories), 1)[0]
			modifier = ''
		elif request.form.get('new_modifier', None):
			category = request.form.get('current_category', None)
			modifier = sample(modifiers - categories[category], 1)[0] if category != None else ''


	return render_template(
			'showoff.html',
			category=category,
			modifier=modifier)


@app.route('/rules')
def rules():
	return "Rules"


@app.route('/about')
def about():
	return "About"


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    host = os.environ.get('HOST', '127.0.0.1')
    app.run(host=host, debug=True, port=port)
