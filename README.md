# QA Fundamental Project- Library App (CRUD Functionality)


This Project looks to create a web application that demonstrates CRUD functionality i.e. Creating database entries, reading them, updating them and deleting them.
The information used to demonstrate this CRUD functionality is stored in an SQL database (specifically using MySQL), which comprised of 3 tables that shared a relationship (one-to-many relationships between each table, but using a connector table to demonstrate a many-to-many relationship between book and customer). The app was then built up using the Flask micro-framework. This was all specifically done to meet the brief for this project.




**App Design:**

For this project I decided to design a library app which allows users to upload new books to the library (Create), users to view the library of books available (Read), update books available to borrow (Update) and remove any books from the library that are no longer part of the library (Delete). The MVP of this database is a books table and a customers table with each customer associated to either no books or many. From future sprints, future iterations of the app would look to include an authors table, that would share a many to many relationship with the books table as currently a book can only have one author, and a genres table in order to view books by category.

**CI Pipeline:**

In addition to the minimum app design the project also requested implementation of some of the stages of a typical CI pipeline: Project Tracking, Version Control, Development Environment and using a build server. 
For Project Tracking a Trello board was used. Items in the product backlog were assigned story points, acceptance criteria and MoSCoW priority and then moved to the sprint backlog where work could then begin on them and they could then move to review when completed as the project progressed. At the beginning of the Sprint the Trello board looked something like this:
![initialSprint](https://user-images.githubusercontent.com/88770784/132550264-eb7c34f5-4ddc-42e4-8f53-65da5f871981.PNG)


[**insert trello board picture here**]

For version control git was used, allowing for changes in the project to be made and committed and a history of these commits allows for restoration to earlier versions of the project should any changes end up breaking the project. In particular GitHub was used to host the repository allowing for the repository to be stored away from the development environment to ensure development on the project didn’t cause any unintended alterations to the project.

The development environment for the project was a python3 virtual environment (venv) set up on a virtual machine (EC2 Instance) running Ubuntu 18.04. Using a venv allows for pip installs and the application to be run without any conflicts between other pip install versions installed on the same machine.

[**insert terminal/instance screenshots here?**]







**Issues during the project:**

Whilst the end product from this project is a functioning webb app that exhibits CRUD functionality, this was of course not achieved without a few issues along the way. Firstly, when attempting to connect the app to the MySQL database made for this project, the connection to the database would time out before the two could properly connect. This was not an immediate issue, as the app could be developed on the databse built into SQLAlchemy in Flask, and only really had to be dealt with when it came to finalising the project.

When it came to using Jenkins, intitially GitHub could not create a webhook with Jenkins to allow for immediate pulls by Jenkins whenever a push was made to the remote repo. Again this wasn't a huge issue as anything that Jenkins can automate can of course be done manually if needed. 

In the creating of unit tests and integration testing for the application some of the tests devised would return errors such as "object does not have attribute post" etc. This was because we were initially trying to write tests that interacted with the database in with the integration tests which looked at a live server case. To resolve this issue a second tests file was created which imported TestCase from Flask-Testing as opposed to the LiveServerTestCasing for the selenium driven integration tests.

Also throughout the development of the programs written in this application, there were times where running the code would return an error, which was then (usually) quickly resolved. 
