 
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

stories = []

@app.route('/')
def index():
    return render_template('index.html', stories=stories)

@app.route('/story/<id>')
def story(id):
    story = stories[int(id)]
    return render_template('story.html', story=story)

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        stories = [story for story in stories if story['title'] == title or story['author'] == author]
    return render_template('search.html', stories=stories)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        story = request.form['story']
        stories.append({'title': title, 'author': author, 'story': story})
        return redirect(url_for('index'))
    return render_template('add.html')

if __name__ == '__main__':
    app.run(debug=True)
