ffrom flask import Flask, render_template,request,redirect,url_for
import pymysql

app = Flask(__name__)

db = pymysql.connect(host="127.0.0.1", port=3306, user="madang", passwd="madang", db="madangdb", charset="utf8")
cur = db.cursor()

@app.route('/')
def index():
    sqlstring = "SELECT * FROM Book"
    cur.execute(sqlstring)

    book_list = cur.fetchall()
    return render_template('booklist.html', book_list=book_list)

@app.route('/view')
def getTicket():
   id=request.args.get('id')
   sqlstring = "SELECT * FROM BOOK WHERE bookid='"+id+"'"
   cur.execute(sqlstring)

   book = cur.fetchall()
   return render_template('bookview.html', book=book)

@app.route('/insert')
def insertForm():
    return render_template('bookinsert.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        bookid = request.form['bookid']
        bookname = request.form['bookname']
        publisher = request.form['publisher']
        price = request.form['price']
        sql = "insert into book(bookid, bookname, publisher, price) values (%s, %s, %s, %s)"
        cur.execute(sql,(bookid, bookname, publisher, price))
        db.commit()
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run('0.0.0.0', port=5001)
