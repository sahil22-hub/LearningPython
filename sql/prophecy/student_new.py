import csv
from os import path
import sqlite3

fileName = "students.csv"
dbName = "new_student.db"


def main():
    std = []

    with open(fileName, "r") as file:
        # Create reader
        reader = csv.DictReader(file)

        # Iterate over CSV file, saving students in a list
        for row in reader:
            std.append(row)

    # Create a connection to the database
    conn = sqlite3.connect(dbName)

    # Create a cursor object to interact with the database
    db = conn.cursor()

    for student in std:
        db.execute(
            "INSERT OR IGNORE INTO students (id, student_name) VALUES (?, ?)",
            (student["id"],
             student["student_name"])
        )
        db.execute(
            "INSERT OR IGNORE INTO houses (house, head) VALUES (?, ?)",
            (student["house"],
             student["head"])
        )
        db.execute(
            "INSERT OR IGNORE INTO assignments (student_id, house_id) VALUES (?, ?)",
            (student["id"],
             student["house"])
        )

    print(f"The  {dbName} it's been loaded with the students data")
    return 0


if __name__ == "__main__":
    main()
