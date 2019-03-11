"""
randomsite package init.

Maxwell Morgan <mjmor@umich.edu>
"""
import flask

app = flask.Flask(__name__)

import randomsite.api # noqa: E402 pylint: disable=wrong-import-position
import randomsite.views # noqa: E402 pylint: disable=wrong-import-position

if __name__ == "__main__":
	app.run(host="0.0.0.0")