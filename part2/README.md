Document project configuration


Fichier :
•	Run.py : It serves as an entry point for application execution.

•	Config.py : Set environment-specific parameters.

•	Requirements.txt : List of Python packages needed for the project.

Répertoire :

App : This directory contains the basic application codes

 Fichier :

•	__init__.py : This file is used to create the Flask application instance.

Répertoire :
Api : 
o	__init__.py : 

Repertoire : 
V1 :
•	__inti__.py :
•	Users.py : 
•	Places.py : 
•	Reviews.py :
•	Aminities.py : 


Models :
•	__init__.py : 
•	user.py : 
•	Place.py : 
•	Review.py :
•	Amenity.py :


Services : This class manages communication between the Presentation, Business Logic and Persistence layers.

•	__init__.py :  This is for creating a class instance that will be used to ensure that only one class instance is created and used in the application.

•	Façade.py :  It defines the class that will generate communication between the Presentation, Business Logic and Persistence layers.

Persistence : Manages object storage and validation, which will then be replaced by a database-based repository.

•	__init__.py : 

•	Repository.py : In-memory repository and interface fully implemented.

•	Incluez des instructions sur l’installation des dépendances et l’exécution de l’application.

