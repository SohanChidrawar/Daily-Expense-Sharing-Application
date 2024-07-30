SetUp and Installation: 
1.	Clone the Repository:
   
      	         git clone repository-url

      	         cd repository-directory

2.	Create a Virtual Environment:
   
      	         python -m venv env

3.	Activate Virtual Environment:
   
      	         env\Scripts\activate

4.	Install Dependencies:
   
      	         pip install -r requirements.txt

      Ensure that “ requirements.txt  “ inclue:

           Django>=4.0, <5.0
           
           djangorestframework>=3.14,<4.0

----> Go to expense folder and then run below command 

5.	Apply Migration:
    
      	          python manage.py migrate
  	   	          python manage.py migrate

6.	Create a superuser (Admin User):
    
      	          python manage.py createsuperuser

7.	Run Development Server:
    
      	          python manage.py runserver

Testing:

To run test cases:

   	             python manage.py test
