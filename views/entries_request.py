import sqlite3
import json
from models import Entry

        
def get_all_entries():
    # Open a connection to the database
    with sqlite3.connect("./kennel.sqlite3") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT *
        FROM entry 
        """)

        # Initialize an empty list to hold all entries representations
        entries = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create an animal instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # Animal class above.
            entry = Entry(row['id'], row['entries'], row['concepts'],
                            row['mood_id'], row['date'])

            entries.append(entry.__dict__)

    # Use `json` package to properly serialize list as JSON
    return json.dumps(entries)

def get_single_entry(id):
    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
        SELECT *
        FROM entry a
        WHERE a.id = ?
        """, ( id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create an location instance from the current row
        entry = Entry(data['id'], data['entries'], data['concepts'], ['mood_id'], data['date'])

        return json.dumps(entry.__dict__)
    
    
def get_search_entry(searchTerm):
        with sqlite3.connect("./kennel.sqlite3") as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()

            # Use a ? parameter to inject a variable's value
            # into the SQL statement.
            db_cursor.execute("""
            SELECT *
            FROM entry a
            CONTAINS searchTerm = ?
            """, ( searchTerm, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create an location instance from the current row
        entry = Entry(data['id'], data['entries'], data['concepts'], ['mood_id'], data['date'])

        return json.dumps(entry.__dict__)
    
    
def delete_entry(id):
    with sqlite3.connect("./kennel.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM entry
        WHERE id = ?
        """, (id, ))