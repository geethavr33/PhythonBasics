# Day 6 Tasks
## Django Project Setup and ORM Basics
Step 1: Install Django
Before starting a Django project, ensure you have Django installed. You can install it using pip:
* python -m venv venv
* pip freeze
* pip install django
* django-admin --version
  
Step 2: Start a New Django Project
Once Django is installed, you can create a new Django project using the following command:


* django-admin startproject project1

This will create a new directory called project1 with the following structure:


>project1/

    >>manage.py
    >>project1/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py
* manage.py: A command-line utility that helps interact with the Django project.
* settings.py: Contains the configurations for the project.
* urls.py: Defines the URL routes for the project.

## Step 3: Create a New Django App
In Django, you create applications within your project. To create an app, navigate to your project directory and run the following command:


* python manage.py startapp myapp

This creates a new directory called myapp with the following structure:


>myapp/

    >>migrations/
    __init__.py
    admin.py
    apps.py
    models.py
    tests.py
    views.py
* models.py: Contains the models (the database schema) for the app.
* admin.py: Registers models to be managed via the Django admin interface.
* views.py: Contains the logic to display data on your website.
## Step 4: Define a Model
A model in Django represents a table in the database. Let's create a Student model in myapp/models.py:
```python
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=50)  # A field for storing the student's name (up to 50 characters)
    age = models.IntegerField()  # A field for storing the student's age

    def __str__(self):
        return self.name  # Returns the student's name when queried
```
```python

name = models.CharField(max_length=50): Defines a character field with a maximum length of 50.
age = models.IntegerField(): Defines an integer field for storing the student's age.
```

### Step 4.1: Model Migration File
After defining the model, Django automatically generates migration files to apply changes to the database. The migration file looks something like this:

```python

# Inside migrations folder in a file like 0001_initial.py

from django.db import migrations, models

class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
            ],
        ),
    ]
```

## Step 5: Apply Migrations to the Database
After defining your model, you need to create and apply the migration to update your database.

#### 1.Create Migrations: Run the following command to create migration files based on the models you defined:

* python manage.py makemigrations
#### 2.Apply Migrations: This command applies the migrations to your database and creates the tables:

* python manage.py migrate
### Step 6: Register the Model in admin.py
To manage the Student model in the Django Admin interface, register it in myapp/admin.py:

```python

from django.contrib import admin
from .models import Student

admin.site.register(Student)
```
### Step 7: Run the Development Server
Start the Django development server to see your project in action:

* python manage.py runserver
* 
Visit http://127.0.0.1:8000/admin to access the Django admin panel. You should be able to see the Student model and add entries to the table.

## ORM Queries
Once the model is set up, you can interact with the database using Django ORM queries. Here are some examples:

### 1. Create a New Student Entry
python
Copy code
from myapp.models import Student

### Create a new student
```python 
student = Student(name='John Doe', age=21)
student.save()  # Save to the database
```
2. Query All Students
```python 
students = Student.objects.all()  # Returns a queryset of all student records
```
3. Query a Specific Student
```python

student = Student.objects.get(id=1)  # Fetch a student by their primary key (id)
```
4. Update a Student's Data
```python
student = Student.objects.get(id=1)
student.age = 22  # Modify the age
student.save()  # Save changes to the database
```
5. Delete a Student Record
```python
student = Student.objects.get(id=1)
student.delete()  # Remove the student from the database
```
## Important Points Covered in the Lesson
* Django Project Setup: Creating a Django project and an app.
* Defining Models: How to define database tables using models in Django.
* Migrations: Using Django's migration system to create and modify database tables.
* Django Admin: Managing models via the Django admin interface.
* Django ORM: Writing queries to interact with the database without writing raw SQL.
  
##  Python code for the Jump Game 
```python
def canJump(nums):
    # Variable to store the farthest index we can reach
    maxReach = 0
    
    # Iterate over each index in the array
    for i in range(len(nums)):
        # If the current index is beyond the farthest we can reach, return False
        if i > maxReach:
            return False
        # Update maxReach to the farthest index we can jump to from this position
        maxReach = max(maxReach, i + nums[i])
        # If maxReach reaches or exceeds the last index, return True
        if maxReach >= len(nums) - 1:
            return True
    
    # If we complete the loop and can't reach the end, return False
    return False

# Test cases
print(canJump([2, 3, 1, 1, 4]))  # Output: True
print(canJump([3, 2, 1, 0, 4]))  # Output: False
```
### Explanation:
1.	maxReach tracks the farthest index you can reach at any point.
2.	The loop goes through each index i. For each index:
o	It checks if the current index is reachable by comparing it with maxReach.
o	It then updates maxReach to the maximum value between the current maxReach and i + nums[i] (the farthest jump possible from the current index).
o	If maxReach exceeds or equals the last index, the function immediately returns true, indicating it's possible to reach the last index.
3.	If the loop completes and maxReach doesn't reach the last index, the function returns false.
Test Cases:
* 	For nums = [2, 3, 1, 1, 4], the function returns True because you can reach the last index.
*	For nums = [3, 2, 1, 0, 4], the function returns False because you get stuck at index 3 (since nums[3] = 0, you can't jump any further).

## III. Python code to solve the problem of finding the minimum number of jumps to reach the last index:
```python 
def jump(nums):
    # Initialize variables
    jumps = 0          # Number of jumps made
    farthest = 0       # Farthest we can reach at any point
    end = 0            # End of the current jump range
    
    # Iterate through the array except the last index
    for i in range(len(nums) - 1):
        # Update the farthest index we can reach
        farthest = max(farthest, i + nums[i])
        
        # If we've reached the end of the current jump range
        if i == end:
            jumps += 1      # Make a jump
            end = farthest  # Update the end to the farthest point we can reach

    return jumps

# Test cases
print(jump([2, 3, 1, 1, 4]))  # Output: 2
print(jump([2, 3, 0, 1, 4]))  # Output: 2
```
### Explanation:
* jumps keeps track of the number of jumps made.
* farthest records the farthest point you can reach during the current range.
* end marks the boundary of the current jump, and once you reach it, you increase the jump count.
* The loop iterates from the first index to the second-to-last index, and whenever you reach the end of the current jump, you make a new jump and update the boundary (end) to the farthest point you can reach.
### Test Cases:
* For the input [2, 3, 1, 1, 4], the output is 2 (jump from index 0 to 1, then from 1 to the last index).
* For the input [2, 3, 0, 1, 4], the output is also 2 (same jumps).