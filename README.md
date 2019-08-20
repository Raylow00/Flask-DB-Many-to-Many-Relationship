# Flask-DB-Many-to-Many-Relationship
A Youtube system clone to showcase many-to-many relationship using Flask SQLAlchemy
![Screenshot of app]

In any web applications that we see nowadays, the database established on the back-end side has to deal with a lot of relationships with multiple tables.
Using Flask SQLAlchemy, this kind of relationship can be established fairly easily.

This Youtube system clone web app enables you to create a user and a channel.
Because of the back-end relationship model, different users can subscribe to different channels, and different channels can have multiple subscribers.

What I Learnt:
- how to establish a many-to-many relationship database model using Flask SQLAlchemy
- how to create an association table that relates two or more tables together
- how to assign foreign keys to the association table to establish connection between two or more tables
- how to establish the relationship by using db.relationship() and db.backref
