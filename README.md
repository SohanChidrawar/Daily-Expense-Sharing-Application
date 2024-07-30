SetUp and Installation: 
1.	Clone the Repository:
   
      	         git clone <repository-url>

      	         cd <repository-directory>

3.	Create a Virtual Environment:
   
	         python -m venv env

5.	Activate Virtual Environment:
   
	         env\Scripts\activate

7.	Install Dependencies:
   
	         pip install -r requirements.txt

Ensure that “ requirements.txt  “ inclue:

           Django>=4.0, <5.0
           
           djangorestframework>=3.14,<4.0

9.	Apply Migration:
    
	          python manage.py migrate

11.	Create a superuser (Admin User):
    
	          python manage.py createsuperuser

13.	Run Development Server:
    
	          python manage.py runserver

Testing:

To run test cases:

	          python manage.py test
