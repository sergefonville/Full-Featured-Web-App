from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author': 'Serge Fonville',
        'title': 'Blog Post 1',
        'content': 'First blog post',
        'date_posted': 'September 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second blog post',
        'date_posted': 'September 21, 2018'
    }
]


@app.route('/')
@app.route('/home')
def hello():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title='About')


if __name__ == '__main__':
    app.run(debug=True)
