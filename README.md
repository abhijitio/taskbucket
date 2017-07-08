# taskindee

Indee Todo Task Management is a simple Todo List Program. It helps you to keep track of work. 

<p> UI Components :- </p>
<p><li>Skeleton JS</li>
<li>jQuery</li>
<li>CSS</li></p>

<p>Backend :- </p>
<p><li>Backend is based on Django and Djangorestframework</li></p>


<p>Test System :-</p>
<p><li> Ubuntu 14.04 LTS </li></p>


<p> Installation :- </p>
Open terminal and type the below commands (If you don't have django installed):- 

<code>
<p> sudo pip install django </p>
<p> sudo pip install djangorestframework </p>
</code>

<p> Next go to the project directory where you want keep the project and type below commands :- </P>

<code>
<p>cd indieetask</p>
<p>git clone https://github.com/abhijitio/taskindee.git </p>
<p>python manage.py migrate</p>
<p>python manage.py runserver</p>
</code>

Make sure to do migrations. Migrations are Django’s way of propagating changes you make to your models (adding a field, deleting a model, etc.) into your database schema. Now, you can browse the landing page by visiting http://localhost:8000/

<p>References :- </p>
<p>http://flask.pocoo.org/snippets/33/</p>
<p>https://docs.djangoproject.com/en/1.7/intro/tutorial01/</p>
<p>https://stackoverflow.com/questions/31762878/sqlite-3-database-with-django</p>
<p>http://www.tangowithdjango.com/book/chapters/models.html</p>
<p>http://www.django-rest-framework.org/api-guide/serializers/</p>
<p>http://www.django-rest-framework.org/tutorial/1-serialization/</p>
<p>https://micropyramid.com/blog/custom-validations-for-serializer-fields-django-rest-framework/</p>
<p>https://stackoverflow.com/questions/757022/how-do-you-serialize-a-model-instance-in-django</p>
<p>https://medium.com/django-rest-framework/dealing-with-unique-constraints-in-nested-serializers-dade33b831d9</p>
<p>https://medium.com/@djstein/modern-django-part-2-rest-apis-apps-and-django-rest-framework-ea0cac5ab104</p>
<p>https://www.reddit.com/r/django/comments/4cbn3e/django_rest_framework_serializers_with_threedeep/</p>
