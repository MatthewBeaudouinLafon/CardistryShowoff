"""
A Flask server to run Showoff

author: Matthew Beaudouin-Lafon
date  : 2017-11-19
license: MIT
"""
import os
from random import sample
from categories import categories, modifiers

from flask import Flask, render_template, request, g
app = Flask(__name__)

# TODO: Make using g work
# with app.app_context():
# 	setattr(g, 'current_category', '') #TODO: Consider not doing global?

@app.route('/', methods=['GET', 'POST'])
def main():
	category = ''
	modifier = ''
	if request.method == 'POST':
		print(request.form)
		if request.form.get('new_category', None):
			# print("New Category")
			category = sample(list(categories), 1)[0]
			# setattr(g, 'current_category', category)
			modifier = ''
		elif request.form.get('new_modifier', None):
			# category = getattr(g, "current_category", None)
			category = request.form.get('new_modifier', None)
			category = category[7:] # I ... I'm sorry
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
