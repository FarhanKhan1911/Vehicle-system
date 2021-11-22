# Vehicle System

## Intoduction 

Vehicle system is the web based app that allow users to get information about cars and also can contribute there information.
<br> This app uses HTML&CSS for its frontend and Django for backend purposes. We have choosen PostgresSQL for database. Other framework used to enchance UI UX includes Bootstrap5 and Font Awesome.

## Feature Available 

<ul>
    <li> Cars List view
    <li>Cars Detail view
    <li>Cars create,update and delete view
   
</ul>

## Pictures

<p align="center" width="100%">
    <h2> Main Page </h2>
    <img src="https://github.com/FarhanKhan1911/Vehicle-system/blob/main/assests/mainpage.jpg"> 
    <h2> Login Page </h2>
    <img src="https://github.com/FarhanKhan1911/Vehicle-system/blob/main/assests/login.jpg"> 
    <h2> Register Page </h2>
    <img src="https://github.com/FarhanKhan1911/Vehicle-system/blob/main/assests/register.jpg"> 
    <h2> Listview Page </h2>
    <img src="https://github.com/FarhanKhan1911/Vehicle-system/blob/main/assests/listview.jpg"> 
    <h2> Detailview Page </h2>
    <img src="https://github.com/FarhanKhan1911/Vehicle-system/blob/main/assests/detailview.jpg"> 
    <h2> Updateview Page </h2>
    <img src="https://github.com/FarhanKhan1911/Vehicle-system/blob/main/assests/updateview.jpg"> 
    <h2> Deleteview Page </h2>
    <img src="https://github.com/FarhanKhan1911/Vehicle-system/blob/main/assests/deleteview.jpg"> 
    <h2> Createview Page </h2>
    <img src="https://github.com/FarhanKhan1911/Vehicle-system/blob/main/assests/createview.jpg"> 
    <h2> Navbar Hovered </h2>
    <img src="https://github.com/FarhanKhan1911/Vehicle-system/blob/main/assests/navbarhovered.jpg"> 
    <h2> Logout Page </h2>
    <img src="https://github.com/FarhanKhan1911/Vehicle-system/blob/main/assests/logout.jpg"> 
    <h2> Mobile Responsive View </h2>
    <img width="20%" src="https://github.com/FarhanKhan1911/Vehicle-system/blob/main/assests/mobileresponsive1.png">
    <img width="20%" src="https://github.com/FarhanKhan1911/Vehicle-system/blob/main/assests/mobileresponsive2.png"> 
</p>


## Requirement 

Python v.3.8+

## Usuage

### Clone Repository

Copy Paste the following commands to clone the repo

```bash
    git clone https://github.com/FarhanKhan1911/Vehicle-system
```
Go inside the directory and install the module from requirements.txt

```bash
  pip install -r requirements.txt
 ```
 
 Then make the migrations and then migrate the database
 
 ```bash
    python manage.py makemigrations
    python manage.py migrate
  ```
  
  Create the superuser 
  
  ```bash
    python manage.py createsuperuser
  ```
  
  Now run the django server
  
  ```bash
    python manage.py runserver
  ````
  
  <h2>Now you goto localhost:8000 to see the website</h2>
  
  ```bash
      http://127.0.0.1:8000/
  ```
  
