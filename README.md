# Mineral Catalog

### A Treehouse Tech Degree Project in Python with Django

Note on loading minerals.json into the database:

1. minerals/views.py contains two functions responsible for loading the minerals
into the database.

2. Ensure that minerals.json is located in minerals/

3. Run the Django shell and import views from minerals.models

4. Call views.add_minerals_to_database() to load minerals into the database.