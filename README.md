# schoolinks

## Project Installation
#### 1. Install virtualenv

```
$ pip --version
$ pip install virtualenv
```
#### 2. Install a Python 2.7 virtualenv & activate

```
$ virtualenv venv
$ source venv/bin/activate
```

#### 3. Install requirements

```
$(env) pip install -r requirements.txt
```

### 4. Run locally

```
$(env) python run.py
```
### 5. Navigate to `localhost:5000/register/texas`

## Design 

With flask, it is possible to fit this application into one file. I made the project structure as if it were a full-fledged application to reflect the organization of the files. Within our `app/` directory we have our application initialization. At this level we also have our `models.py`. 

Our forms and routing are located in the `app/main` folder. Flask has a concept of "blueprints", which is a way of organizing routes and functionality in a modular fashion. Our `app/main/views.py` has our routing logic. This takes in the requests and presents the view. The `app/main/form.py` holds the form creation logic and the validation logic.

Finally our views are in `app/templates`. For this use case, I opted for backend rendering of our views. Both the `register.html` and `landing.html` contain Jinja template logic. This allows for dynamic rendering of views and forms. 

## Models

Our `MasterSchedule` model is designed to take in a school name and return a master schedule of classes and times. This is to support multiple school systems with multiple schedules. Each class is an hour long. A schedule is represented by a class and a time. The way we validate a correct schedule is to make sure that the student has 5 unique times, which means there are no overlapping hours.

Our `Student` model is very simple. It is an instance of a schedule. The student has 5 instances of classes represented by a single time.

## Stubbed Database
Since this is a "mini-application", the database is stubbed. All the database transactions are abstracted away, however. If I were to set up a database, all of the transaction logic would lie in the `models.py` file. Currently, the `models.py` file uses a dictionary as a pseudo-datastore. For this type of use case, I would use a noSQL database for quick iteration and quick set up. 
