import sqlite3 as sq

def sql_start():
    global base, cur
    base = sq.connect('photo_session.db') # создаст если нет
    cur = base.cursor()
    if base:
        print('Data base connected OK')
    base.execute('CREATE TABLE IF NOT EXISTS menu(img TEXT, name TEXT PRIMARY KEY, description TEXT, price TEXT)')
    base.commit()

async def sql_add_command(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO menu VALUES (?,?,?,?)', tuple(data.values())) # картеж для sqlite  надо
        base.commit()


