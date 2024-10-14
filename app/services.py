import sqlite3

def registerUser(payload):
    try:
        # Create a new SQLite database if it doesn't exist
        conn = sqlite3.connect('users.db')
        c = conn.cursor()

        # Create a table named 'users' if it doesn't exist
        c.execute('''CREATE TABLE IF NOT EXISTS users
                       (id INTEGER PRIMARY KEY AUTOINCREMENT,
                       userName text NOT NULL,
                       email text NOT NULL,
                       password text NOT NULL,
                       address text NOT NULL)''')

        # Insert the new user into the 'users' table
        c.execute("INSERT INTO users (userName, email, password, address) VALUES (?, ?, ?, ?)",
                   (payload["userName"], payload["email"], payload["password"], payload["address"]))

        # Commit the changes and close the connection
        conn.commit()
        conn.close()

        return "User registered successfully"

    except sqlite3.Error as err:
        print("Something went wrong: {}".format(err))
        return "User already exists !"

def loginUser(payload):
    try:
        conn = sqlite3.connect('users.db')
        c = conn.cursor()

        # Query the 'users' table for the user with the given email and password
        c.execute("SELECT * FROM users WHERE email=? AND password=?", (payload["email"], payload["password"]))

        rowData = c.fetchone()

        if(rowData == None):
            return "Invalid Credentials !"
        else:
            return rowData

        conn.close()

    except sqlite3.Error as err:
        print("Something went wrong: {}".format(err))
        return "Invalid Credentials !"

def updateUser(payload):
    try:
        conn = sqlite3.connect('users.db')
        c = conn.cursor()

        # Update the user with the given ID
        c.execute("UPDATE users SET userName=?, email=?, password=?, address=? WHERE id=?",
                   (payload["userName"], payload["email"], payload["password"], payload["address"], payload["id"]))

        # Commit the changes and close the connection
        conn.commit()
        conn.close()

        return "User updated successfully"

    except sqlite3.Error as err:
        print("Something went wrong: {}".format(err))
        return "User update failed !"

def deleteUser(payload):
    try:
        conn = sqlite3.connect('users.db')
        c = conn.cursor()

        # Delete the user with the given ID
        c.execute("DELETE FROM users WHERE id=?", (payload[0],))

        # Commit the changes and close the connection
        conn.commit()
        conn.close()

        return "User deleted successfully"

    except sqlite3.Error as err:
        print("Something went wrong: {}".format(err))
        return "User deletion failed !"