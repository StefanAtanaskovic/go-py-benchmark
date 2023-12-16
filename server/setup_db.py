import sqlite3


def setup_db():
    connection = sqlite3.connect("server_db.db")

    cursor = connection.cursor()

    cursor.execute("""
                    drop table if exists items;
                   """)

    cursor.execute("""
                   create table items (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        title text not null,
                        description text not null
                       )
                   """)

    cursor.execute("""
        INSERT INTO items VALUES
            (1, 'Monty Python and the Holy Grail', "jklasdfja asdklfajsdf asdlfklasdjf" ),
            (2, 'Monty Python and the Holy Grail', "jklasdfja asdklfajsdf asdlfklasdjf" ),
            (3, 'Monty Python and the Holy Grail', "jklasdfja asdklfajsdf asdlfklasdjf" ),
            (4, 'Monty Python and the Holy Grail', "jklasdfja asdklfajsdf asdlfklasdjf" ),
            (5, 'Monty Python and the Holy Grail', "jklasdfja asdklfajsdf asdlfklasdjf" ),
            (6, 'Monty Python and the Holy Grail', "jklasdfja asdklfajsdf asdlfklasdjf" ),
            (7, 'Monty Python and the Holy Grail', "jklasdfja asdklfajsdf asdlfklasdjf" ),
            (8, 'Monty Python and the Holy Grail', "jklasdfja asdklfajsdf asdlfklasdjf" ),
            (9, 'Monty Python and the Holy Grail', "jklasdfja asdklfajsdf asdlfklasdjf" ),
            (10, 'Monty Python and the Holy Grail', "jklasdfja asdklfajsdf asdlfklasdjf" )
    """)

    connection.commit()
    connection.close()
