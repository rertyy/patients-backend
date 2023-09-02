Frontend repo at https://github.com/rertyy/patients-frontend
Backend repo at https://github.com/rertyy/patients-backend

Hosted on https://patients-api-gik9.onrender.com

Testing instructions:
1. Clone this repository `git clone https://github.com/rertyy/patients-backend`
2. Run `pip install -r requirements.txt`
3. Setup a [MongoDB Atlas](https://www.mongodb.com/atlas/database) database
4. Make a `.env` file and add in `DBCONN=mongodb+srv://<username>:<password>@<database>.mongodb.net/?retryWrites=true&w=majority`, replacing username, password and database with your own values
5. Run `python3 reset_data.py` in the terminal to migrate the database and populate the collection 
6. Use `flask run` in the terminal to start the server on http://127.0.0.1/5000

Available endpoints:
1. `/health`: GET always returns 200 OK
2. `/patients`: GET returns a list of patients
3. `/patients/{id}/notes` POST to save patient notes to database