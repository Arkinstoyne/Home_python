@app.route('/add_post', methods=['POST'])
def add_post():
    author = request.form['author']
    title = request.form['title']
    content = request.form['content']

    conn = get_db_connection()
    conn.execute('INSERT INTO posts (title, content, author) VALUES (?, ?, ?)',
                 (title, content, author))
    conn.commit()
    conn.close()

    return redirect(url_for('index'))




@app.route('/')
def index():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    return render_template('index.html', posts=posts)


@app.route('/post/<int:post_id>/comment', methods=['POST'])
def add_comment(post_id):
    author = request.form['author']
    content = request.form['content']

    conn = get_db_connection()
    conn.execute('INSERT INTO comments (post_id, content, author) VALUES (?, ?, ?)',
                 (post_id, content, author))
    conn.commit()
    conn.close()

    return redirect(url_for('post', post_id=post_id))
