=====
Exileui
=====

Exileui is a simple Django app to conduct Web-based exileui. For each
question, visitors can choose between a fixed number of answers.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "exileui" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        'exileui',
        ...
    ]

2. Include the exileui URLconf in your project urls.py like this::

    url(r'^exileui/', include('exileui.urls')),

3. Run `python manage.py migrate` to create the exileui models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a poll (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/exileui/ to participate in the poll.
