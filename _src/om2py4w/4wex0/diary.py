import sqlite3
from bottle import route, run,debug

@route('/diary')
def diary():
    conn = sqlite3.connect('diary.db')
    c = conn.cursor()
    c.execute("SELECT id, task FROM diary WHERE status LIKE '1'")
    result = c.fetchall()
    return str(result)

debug(True)
run(reloader=True)