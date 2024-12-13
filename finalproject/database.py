import sqlite3

def get_db_connection():
    conn=sqlite3.connect("books.db")
    conn.row_factory=sqlite3.Row
    return conn
def create_database():
    conn=sqlite3.connect("books.db")
    cursor=conn.cursor()
    cursor.execute('''
    create table if not exists books(
        id integer primary key autoincrement,
        title text,
        author_id integer,
        book_link text,
        genres text,
        average_rating real,
        published_year integer,
        foreign key (author_id) references authors(id)
        )
    ''')
    cursor.execute('''
    create table if not exists authors(
         id integer primary key autoincrement,
         name text unique
         )
    ''')
    cursor.commit()
    return conn, cursor
def insert_authors(authors, cursor):
    authors_ids={}
    for author in authors:
        cursor.execute('''
        insert or ignore into authors (name) values (?)
        ''',(author,))
        cursor.execute("select id from authors where name=?",(author,) )
        authors_ids[author]==cursor.fetchone()[0]
        return authors_ids

def insert_books(books_dictionary,authors_ids, cursor):
    for (title,author), info in books_dictionary.items():
        cursor.execute('''
        insert into books (title, author_id, book_link, genres,average_rating, published_year)
        values (?,?,?,?,?,?)
        ''',(title, authors_ids[author]), info['link'], ",".join(info["genres"]))
        float(info['avg_rating'].split()[0] if info["avg_rating"] else None), int(info['published'].split()[0] if info ["published"] else None)
def insert_data(books_dict, authors):
    conn, cursor=create_database()
    author_ids=insert_authors(authors, cursor)
    insert_books(books_dict, author_ids, cursor )
    conn.commit()
    conn.close()

if __name__=="__main__":
    from book_scraper import scrape_books
    books_dictionary, authors=scrape_books()
    insert_data(books_dictionary,authors )



