from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    connect = sqlite3.connect('books.db')
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()
    connect.close()
    return render_template("index.html", books=books)

@app.route ('/add', methods=["GET", 'POST'])
def add_book():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        pages = request.form['pages']
        status = request.form['status']

        connect = sqlite3.connect('books.db')
        cursor = connect.cursor()


        cursor.execute("INSERT INTO books (title, author, pages, status) VALUES (?, ?, ?, ?)", (title, author, pages, status))
        connect.commit()
        connect.close()
        return redirect('/')
    return render_template("add_book.html")

@app.route('/delete/<int:id>')
def delete_book(id):
    
    connect = sqlite3.connect('books.db')
    cursor = connect.cursor()

    cursor.execute("DELETE FROM books WHERE id= ?", (id,))
    connect.commit()
    connect.close()

    return redirect('/')


@app.route('/search', methods=['GET', 'POST'])
def search():
    books = []
    if request.method == 'POST':
        keyword = request.form['keyword']
        connect = sqlite3.connect('books.db')
        cursor = connect.cursor()

        cursor.execute("SELECT * FROM books WHERE title LIKE ?", ('%' + keyword + '%',))
        books = cursor.fetchall()

        connect.close()

        return render_template("search.html", books = books)
    return render_template("search.html", books=books)

    
if __name__ == '__main__':
    app.run(debug=True)

