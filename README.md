# QA Fundamental Project- Library App (CRUD Functionality)


This Project looks to create a web application that demonstrates CRUD functionality i.e. Creating database entries, reading them, updating them and deleting them.
The information used to demonstrate this CRUD functionality is stored in an SQL database (specifically using MySQL), which comprised of 3 tables that shared a relationship (one-to-many relationships between each table, but using a connector table to demonstrate a many-to-many relationship between book and customer). 




**App Design:**

For this project I decided to design a library app which allows users to upload new books to the library (Create), users to view the library of books available (Read), update books available to borrow (Update) and remove any books from the library that are no longer part of the library (Delete). The MVP of this database is a books table and a customers table with each customer associated to either no books or many. From future sprints, future iterations of the app would look to include an authors table, that would share a many to many relationship with the books table as currently a book can only have one author, and a genres table in order to view books by category.

At the beginning of the sprint the ERD looked like this:
![basicERD](https://user-images.githubusercontent.com/88770784/132720287-c340c3e0-11ee-4d1c-9542-726a3d650fbc.PNG)


The app was built up using the Flask micro-framework. This provided a basic structure for the web app, meaning that I was able to focus on developing the different objects and their interactions within the app and the layout of the web app. Since this app would rely on storing information in a database, the SQLAlchemy extension could be used with Flask to facilitate this. Additionally, sensitive pieces of information, such as the Database URI could be stored in an environment variable so that they aren't visible in any of the code saved in this repo, and Secret Keys were used to provide an extra layer of security.


**CI Pipeline:**

In addition to the minimum app design the project also requested use of some of the stages of a typical CI pipeline: Project Tracking and Management, Version Control, Development Environment and using a build server. 
For Project Tracking a Trello board was used. Items in the product backlog were assigned story points, acceptance criteria and MoSCoW priority and then moved to the sprint backlog where work could then begin on them and they could then move to review when completed as the project progressed. At the beginning of the Sprint the Trello board looked something like this:
![initialSprint](https://user-images.githubusercontent.com/88770784/132550264-eb7c34f5-4ddc-42e4-8f53-65da5f871981.PNG)


[**insert trello board picture here**]

For version control git was used, allowing for changes in the project to be made and committed and a history of these commits allows for restoration to earlier versions of the project should any changes end up breaking the project. In particular GitHub was used to host the repository allowing for the repository to be stored away from the development environment to ensure development on the project didn’t cause any unintended alterations to the project.

The development environment for the project was a python3 virtual environment (venv) set up on a virtual machine (EC2 Instance) running Ubuntu 18.04. Using a venv allows for pip installs and the application to be run without any conflicts between other pip install versions that may be installed on the same virtual machine.

[**insert terminal/instance screenshots here?**]

Jenkins is an open-source automation server which can be used to automate some of the processes involved in the development of an application such as this. To begin with Jenkins was used to automate the unit/integrations tests of the app, ideally testing new versions of the app as soon as they had been pushed to this repository, through the use of a webhook, though with the way this app was developed, Jenkins was only implemented fairly late on in the process, and whilst it can still automate testing of the app, this is a little redundant if the testing had already been done manually before the code was ever pushed up to the repository. Additionally, Jenkins **(was)** used to automate deployment of the app once a successful test build had been completed. Jenkins is an incredibly useful tool for the production of an app when used correctly, though it certainly came with a few issues that needed resolving before it could be used properly, as will be discussed in the next section.



**Issues during the project:**

Whilst the end product from this project is a functioning webb app that exhibits CRUD functionality, this was of course not achieved without a few issues along the way. Firstly, when attempting to connect the app to the MySQL database made for this project, the connection to the database would time out before the two could properly connect. This was not an immediate issue, as the app could be developed on the databse built into SQLAlchemy in Flask, and only really had to be dealt with when it came to finalising the project.

When it came to using Jenkins, intitially GitHub could not create a webhook with Jenkins to allow for immediate pulls by Jenkins whenever a push was made to the remote repo. Again this wasn't a huge issue as anything that Jenkins can automate can of course be done manually if needed. In attempts to resolve this issue, a new VM was created, however, when then trying to install Jenkins onto that VM, not all of the plugins would install, including ones allowing Jenkins to interact with GitHub, which is a vital part of being able to automate builds using webhooks. 

In the creating of unit tests and integration testing for the application some of the tests devised would return errors such as "object does not have attribute post" etc. This was because we were initially trying to write tests that interacted with the database in with the integration tests which looked at a live server case. To resolve this issue a second tests file was created which imported TestCase from Flask-Testing as opposed to the LiveServerTestCasing for the selenium driven integration tests.

Also throughout the development of the programs written in this application, there were times where running the code would return an error, which was then (usually) quickly resolved. 
