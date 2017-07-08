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


