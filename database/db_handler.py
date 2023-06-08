import json
import sqlite3
import os.path

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "RugramDB.db")


def Login(login, passw):
    con = sqlite3.connect(db_path)
    cur = con.cursor()

    cur.execute(f'SELECT * FROM users WHERE login="{login}";')
    value = cur.fetchall()

    if value != [] and value[0][2] == passw:
        print("Успешная авторизация!")
        ret = True
    else:
        print("Проверьте правильность ввода данных")
        ret = False

    cur.close()
    con.close()
    return ret


def Register(login, passw, image, bio):
    con = sqlite3.connect(db_path)
    cur = con.cursor()

    ret = False

    cur.execute(f'SELECT * FROM users WHERE login="{login}";')
    value = cur.fetchall()

    if value != []:
        print('Такой ник уже используется')
        ret = False
    elif value == []:
        sqlite_insert_blob_query = """INSERT INTO users
                                              (login, password, image, bio) VALUES (?, ?, ?, ?)"""

        photo = convert_to_binary_data(image)
        data_tuple = (login, passw, photo, bio)
        cur.execute(sqlite_insert_blob_query, data_tuple)
        print("Вы успешно зарегистрированы")
        ret = True
        con.commit()

    cur.close()
    con.close()
    return ret


def getProfileInfo(login):
    con = sqlite3.connect(db_path)
    cur = con.cursor()

    cur.execute(f'SELECT * FROM users WHERE login="{login}";')
    value = list(cur.fetchall())

    cur.close()
    con.close()
    res = []
    for el in value[0]:
        res.append(el)
    # res[7] = json.loads(res[7])
    # print(res)
    return res


def convert_to_binary_data(filename):
    # Преобразование данных в двоичный формат
    with open(filename, 'rb') as file:
        blob_data = file.read()
    return blob_data


def write_to_file(data, filename):
    # Преобразование двоичных данных в нужный формат
    with open(filename, 'wb') as file:
        file.write(data)


def getPosts(login, fav=False):
    con = sqlite3.connect(db_path)
    cur = con.cursor()

    if fav:
        cur.execute(f'SELECT favorites FROM users WHERE login="{login}";')
    else:
        cur.execute(f'SELECT posts FROM users WHERE login="{login}";')
    value = cur.fetchall()

    cur.close()
    con.close()

    if value[0][0] == '':
        return [[]]
    tmp = list(value[0])
    res = []
    for el in tmp:
        res.append(json.loads(el))

    return res


def addPost(login, post, fav=False):
    con = sqlite3.connect(db_path)
    cur = con.cursor()

    res = getPosts(login, fav)
    if len(res[0]) == 0:
        res[0] = [post]
    else:
        res[0].append(post)

    if fav:
        cur.execute('UPDATE users SET favorites=? WHERE login=?;', (json.dumps(res[0]), login))
    else:
        cur.execute('UPDATE users SET posts=? WHERE login=?;', (json.dumps(res[0]), login))
    con.commit()

    cur.close()
    con.close()


def addPosts(login, posts, fav=False):
    con = sqlite3.connect(db_path)
    cur = con.cursor()

    if fav:
        cur.execute('UPDATE users SET favorites=? WHERE login=?;', (json.dumps(posts), login))
    else:
        cur.execute('UPDATE users SET posts=? WHERE login=?;', (json.dumps(posts), login))
    con.commit()

    cur.close()
    con.close()


def editProfile(login, name, passw, bio):
    con = sqlite3.connect(db_path)
    cur = con.cursor()

    ret = False
    cur.execute(f'SELECT * FROM users WHERE login="{name}";')
    value = cur.fetchall()

    if value != [] and login != name:
        ret = False
    else:
        cur.execute('UPDATE users SET login=?, password=?, bio=? WHERE login=?;', (name, passw, bio, login))
        con.commit()
        ret = True

    cur.close()
    con.close()

    return ret

def Find(name):
    con = sqlite3.connect(db_path)
    cur = con.cursor()

    ret = False

    cur.execute(f'SELECT * FROM users WHERE login="{name}";')
    value = cur.fetchall()

    if value != []:
        ret = True

    cur.close()
    con.close()

    return ret


def getSubscriptions(login):
    con = sqlite3.connect(db_path)
    cur = con.cursor()

    cur.execute(f'SELECT subscriptions FROM users WHERE login="{login}";')
    value = list(cur.fetchall())

    cur.close()
    con.close()
    res = []
    for el in value[0]:
        if el != '':
            res.append(json.loads(el))
    return res[0]


def getSubscribers(login):
    con = sqlite3.connect(db_path)
    cur = con.cursor()

    cur.execute(f'SELECT subscribers FROM users WHERE login="{login}";')
    value = list(cur.fetchall())

    cur.close()
    con.close()
    res = []
    for el in value[0]:
        if el != '':
            res.append(json.loads(el))
    return res[0]


def subscribe(main, sub):
    con = sqlite3.connect(db_path)
    cur = con.cursor()

    msubs = getSubscriptions(main)
    ssubs = getSubscribers(sub)
    msubs.append(sub)
    ssubs.append(main)

    print(msubs)
    print(ssubs)

    cur.execute('UPDATE users SET subscriptions=? WHERE login=?;', (json.dumps(msubs), main))
    con.commit()

    cur.execute('UPDATE users SET subscribers=? WHERE login=?;', (json.dumps(ssubs), sub))
    con.commit()

    cur.close()
    con.close()


def unsubscribe(main, sub):
    con = sqlite3.connect(db_path)
    cur = con.cursor()

    msubs = getSubscriptions(main)
    ssubs = getSubscribers(sub)
    msubs.remove(sub)
    ssubs.remove(main)

    print(msubs)
    print(ssubs)

    cur.execute('UPDATE users SET subscriptions=? WHERE login=?;', (json.dumps(msubs), main))
    con.commit()

    cur.execute('UPDATE users SET subscribers=? WHERE login=?;', (json.dumps(ssubs), sub))
    con.commit()

    cur.close()
    con.close()

