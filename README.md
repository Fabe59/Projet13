# Projet 13 : OpenRider  
  
## Description:  
OpenRider is a web application allowing motorcyclists to find suitable accommodation for themselves and their motorcycles.  
OpenRider is available at : https://www.openrider.fr
  
  
### Create the virtual environment and install the devDependencies 
```sh
$ pip intall pipenv  
$ pipenv shell  
$ pipenv install
```
  
### Initialize project  
Position yourself in the openrider folder  
Then initialize db:  

```sh
$ ./manage.py makemigrations  
$ ./manage.py migrate
$ ./manage.py initdb
```  
  
Your can now create a superuser by typing:  

```sh
$ ./manage.py createsuperuser
``` 

Finally, launch with : 
  
```sh
$ ./manage.py runserver
``` 
  
### Tests  
  
In the **openrider folder**, you can launch test typing:  
```sh
$ coverage run --source='.' manage.py test
``` 
  
To view the test report :
```sh
$ coverage report
``` 