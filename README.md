# HBNB

This is the console /command interpreter for the Holberton Airbnb clone project. The console can be used to store objects in and retrieve objects from a JSON.

### Supported classes:
* BaseModel
* User
* State
* City
* Amenity
* Place
* Review

### Commands:
* create - create an object
* show - show an object (based on id)
* destroy - destroy an object
* all - show all objects, of one type or all types
* quit/EOF - quit the console
* help - see descriptions of commands

To start, navigate to the project folder and enter `./console.py` in the shell.

#### Create
`create <class name>`
Ex:
`create BaseModel`

#### Show
`show <class name> <object id>`
Ex:
`show User my_id`

#### Destroy
`destroy <class name> <object id>`
Ex:
`destroy Place my_place_id`

#### All
`all` or `all <class name>`
Ex:
`all` or `all State`

#### Quit
`quit` or `EOF`

#### Help
`help` or `help <command>`
Ex:
`help` or `help quit`

Additionally, the console supports `<class name>.<command>(<parameters>)` syntax.
Ex:
`City.show(my_city_id)`

## Original Author
* Kevin Yook
-----------------

# Airbnb Clone v2
An update of the orignal, forked clone above, implenting new features:

## Using a MySQL database for object creation/storage
- **DBStorage**: (models/engine/db_storage.py)
	- **all(self, cls=None)**: query all in current database
	- **new(self, obj)**: add the object to the current database session
	- **save(self)**: commit all changes of the current database session 
	- **delete(self, obj=None)**: delete from the current database session obj if not None
	- **reload(self)**: create all tables in database 

## Classes that establish, update, and delete relationships among different MySQL tables
- User
- Place
- Review
- Amenity
- City
- State
- BaseModel

## Updates to console commands to validate and create these new databse objects
- **do_create(self, arg)**:
	- **Command syntax**: ```create <Class name> <param 1> <param 2> <param 3>...```
	- **Param syntax**: ```<key name>=<value>```

## Authors
* Heindrick Cheung
* Brent Janski
