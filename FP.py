import psycopg2 
import customtkinter as ctk
from CTkTable import *
from CTkMessagebox import CTkMessagebox

connection = None
cursor = None
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("dark-blue")

root = ctk.CTk()
root.geometry("720x720")

def addUser(userid, location, age):
    try: 
        connection = psycopg2.connect(user="postgres",
                                    password="password",
                                    host="127.0.0.1",
                                    port="5432",
                                    database="db_FinalProject")
        cursor = connection.cursor()

        insert_script = 'INSERT INTO userData (userid, location, age) VALUES (%s, %s, %s)'
        insert_value = (userid, location, age)
        cursor.execute(insert_script, insert_value);

        connection.commit()
    except Exception as e:
        print(e)
    finally:
        if cursor is not None:
            cursor.close()
        if connection is not None:
            connection.close()

def searchDatabase(isbn):
    try: 
        connection = psycopg2.connect(user="postgres",
                                    password="password",
                                    host="127.0.0.1",
                                    port="5432",
                                    database="db_FinalProject")
        cursor = connection.cursor()

        search_script = '''SELECT * FROM Rating WHERE ISBN LIKE %s;'''
        insert_value = (isbn)
        insert_value=[isbn+'%']
        cursor.execute(search_script, insert_value)
        result = cursor.fetchall()

        connection.commit()
        return result
    except Exception as e:
        print(e)
    finally:
        if cursor is not None:
            cursor.close()
        if connection is not None:
            connection.close()

def addBook(isbnid, title):
    try: 
        connection = psycopg2.connect(user="postgres",
                                    password="password",
                                    host="127.0.0.1",
                                    port="5432",
                                    database="db_FinalProject")
        cursor = connection.cursor()
        insert_script = 'INSERT INTO book (isbnid, title) VALUES (%s, %s);'
        insert_value = (isbnid, title)
        cursor.execute(insert_script, insert_value);

        connection.commit()
    except Exception as e:
        print(e)
    finally:
        if cursor is not None:
            cursor.close()
        if connection is not None:
            connection.close()

def addAuthor(author):
    try: 
        connection = psycopg2.connect(user="postgres",
                                    password="password",
                                    host="127.0.0.1",
                                    port="5432",
                                    database="db_FinalProject")
        cursor = connection.cursor()
        insert_script = """INSERT INTO author (authorname) VALUES (%s)"""
        insert_value = (author,)
        cursor.execute(insert_script, insert_value);

        connection.commit()
    except Exception as e:
        print(e)
    finally:
        if cursor is not None:
            cursor.close()
        if connection is not None:
            connection.close()

def addPublisher(publisher):
    try: 
        connection = psycopg2.connect(user="postgres",
                                    password="password",
                                    host="127.0.0.1",
                                    port="5432",
                                    database="db_FinalProject")
        cursor = connection.cursor()
        insert_script = 'INSERT INTO publisher (publishername) VALUES (%s);'
        insert_value = (publisher,)
        cursor.execute(insert_script, insert_value);

        connection.commit()
    except Exception as e:
        print(e)
    finally:
        if cursor is not None:
            cursor.close()
        if connection is not None:
            connection.close()

def clear_widgets():
    for widget in root.winfo_children():
        widget.destroy()

def home_page():
    clear_widgets()

    label = ctk.CTkLabel(root, text="Welcome to Review GUI", font=("Arial", 18))
    label.pack(pady=20)

    btn_food_journal = ctk.CTkButton(root, text="Add User", command=add_user_page)
    btn_food_journal.pack(pady=10)

    btn_check_journal = ctk.CTkButton(root, text="Check Review", command=check_ratings)
    btn_check_journal.pack(pady=10)

    btn_book_page = ctk.CTkButton(root, text="Add Book", command=add_book_page)
    btn_book_page.pack(pady=10)

def add_user_page():
    clear_widgets()

    label = ctk.CTkLabel(root, text="Add User Page", font=("Arial", 18))
    label.pack(pady=20)

    user_id_label = ctk.CTkLabel(root, text="User ID:")
    user_id_label.pack()
    user_id_entry = ctk.CTkEntry(root)
    user_id_entry.pack()

    location_id_label = ctk.CTkLabel(root, text="Location:")
    location_id_label.pack()
    location_id_entry = ctk.CTkEntry(root)
    location_id_entry.pack()

    age_label = ctk.CTkLabel(root, text="Age:")
    age_label.pack()
    age_entry = ctk.CTkEntry(root)
    age_entry.pack()

    def save_values_and_back():
        user_id = user_id_entry.get()
        location_id = location_id_entry.get()
        age = age_entry.get()

        print("User ID:", user_id)
        print("Location:", location_id)
        print("Date:", age)
        
        addUser(user_id,location_id,age)
        CTkMessagebox(title="Info", message="Successfully Created User")


    btn_save = ctk.CTkButton(root, text="Save", command=save_values_and_back)
    btn_save.pack(pady=10)
    btn_save = ctk.CTkButton(root, text="Back", command=home_page)
    btn_save.pack(pady=10)

def check_ratings():
    clear_widgets()

    label = ctk.CTkLabel(root, text="Ratings Page", font=("Arial", 18))
    label.pack(pady=20)

    user_id_label = ctk.CTkLabel(root, text="ISBN:")
    user_id_label.pack()
    user_id_entry = ctk.CTkEntry(root)
    user_id_entry.pack()

    def save_date():
        user_id = user_id_entry.get()
        print("User ID:", user_id)
        
        canvas = ctk.CTkCanvas(root)
        canvas.pack(side="left", fill="both", expand=True)
        
        scrollable_frame = ctk.CTkScrollableFrame(canvas)
        scrollable_frame.pack(expand=True, fill="both")
        
        table = CTkTable(master=scrollable_frame, values=searchDatabase(user_id))
        table.pack(expand=True, fill="both", padx=20, pady=20)
        
        def on_configure(event):
            canvas.configure(scrollregion=canvas.bbox("all"))
            canvas.itemconfig(frame_id, width=canvas.winfo_width()) 
        canvas.bind("<Configure>", on_configure)

    btn_save = ctk.CTkButton(root, text="Save", command=save_date)
    btn_save.pack(pady=10)
    btn_save = ctk.CTkButton(root, text="Back", command=home_page)
    btn_save.pack(pady=10)

def add_book_page():
    clear_widgets()

    label = ctk.CTkLabel(root, text="Add Book Page", font=("Arial", 18))
    label.pack(pady=20)

    ISBN_id_label = ctk.CTkLabel(root, text="ISBN:")
    ISBN_id_label.pack()
    ISBN_id_entry = ctk.CTkEntry(root)
    ISBN_id_entry.pack()

    Title_id_label = ctk.CTkLabel(root, text="Title:")
    Title_id_label.pack()
    Title_id_entry = ctk.CTkEntry(root)
    Title_id_entry.pack()

    author_label = ctk.CTkLabel(root, text="Author:")
    author_label.pack()
    author_entry = ctk.CTkEntry(root)
    author_entry.pack()

    publisher_label = ctk.CTkLabel(root, text="publisher:")
    publisher_label.pack()
    publisher_entry = ctk.CTkEntry(root)
    publisher_entry.pack()

    def save_values_and_back():
        ISBN_id = ISBN_id_entry.get()
        Title_id = Title_id_entry.get()
        author = author_entry.get()
        publisher = publisher_entry.get()

        print("ISBN ID:", ISBN_id)
        print("Title:", Title_id)
        print("Author:", author)
        print("Publisher:", publisher)
        
        addBook(ISBN_id,Title_id)
        addAuthor(author)
        addPublisher(publisher)
        CTkMessagebox(title="Info", message="Book Sucessfully Added")

    btn_save = ctk.CTkButton(root, text="Save", command=save_values_and_back)
    btn_save.pack(pady=10)
    btn_save = ctk.CTkButton(root, text="Back", command=home_page)
    btn_save.pack(pady=10)

home_page()
root.mainloop()