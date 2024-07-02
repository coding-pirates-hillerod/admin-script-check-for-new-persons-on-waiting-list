import sqlite3


def create_and_seed_db(persons: list[tuple]) -> None:
    con = sqlite3.connect("waitinglist.db")

    cur = con.cursor()

    cur.execute("CREATE TABLE persons(person)")
    con.commit()

    cur.executemany("INSERT INTO persons VALUES(?)", persons)
    con.commit()

    con.close()


def fetch_saved_waiting_list_persons() -> list[tuple]:
    con = sqlite3.connect("waitinglist.db")

    cur = con.cursor()
    res = cur.execute("SELECT * FROM persons")

    saved_persons = res.fetchall()

    con.close()

    return saved_persons


def save_new_persons_to_db(persons: list[tuple]) -> None:
    con = sqlite3.connect("waitinglist.db")

    cur = con.cursor()
    cur.executemany("INSERT INTO persons VALUES(?)", persons)
    con.commit()

    con.close()


if __name__ == "__main__":
    con = sqlite3.connect("waitinglist.db")

    cur = con.cursor()

    res = cur.execute("SELECT * FROM persons")

    persons = res.fetchall()

    for person in persons:
        print(person[0])

    con.close()
