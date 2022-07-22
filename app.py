from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
import stories


app = Flask(__name__)

app.config['SECRET_KEY'] = "oh-so-secret"
debug = DebugToolbarExtension(app)

# routes
@app.route('/')
def homepage():
    return render_template('homepage.html', prompts=stories.story.prompts)


@app.route('/story', methods=["POST"])
def story():
    text = stories.story.generate(request.form)
    return render_template('story.html', text=text)




