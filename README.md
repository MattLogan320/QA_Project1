# QA Fundamental Project- Library App (CRUD Functionality)


This Project looks to create a web application that demonstrates CRUD functionality i.e. Creating database entries, reading them, updating them and deleting them.
The information used to demonstrate this CRUD functionality is stored in an SQL database (specifically using MySQL), which comprised of (X number tables) that shared a relationship (one-to-many relationships, but using connector tables to demonstarte a many-to-many relationship). The app was then built up using the Flask micro-framework. This was all specifically done to meet the brief for this project.


**App Design:**

For this project I decided to design a library app which allows users (staff) to upload new books to the library (Create), users to view the library of books available (staff and customers) (Read), update books available to borrow (Update) and remove any books from the library that are no longer part of the library (Delete)(staff). The MVP of this database is a books table and a customers table with each customer associated to either no books or many. To extend on this the authors of books was added, with the authors table being created with a relationship to the books table, where every book had at least one author associated with it.

**CI Pipeline:**

In addition to the minimum app design the project also requested implementation of many of the stages of a typical CI pipeline: Project Tracking, Version Control, Development Environment and build server. 
For Project Tracking a Trello board was used. Items in the product backlog were assigned story points, acceptance criteria and MoSCoW priority and then moved to the sprint backlog where work could then begin on them and they could then move to review when completed as the project progressed.

[**insert trello board picture here**]

For version control git was used, allowing for changes in the project to be made and committed and a history of these commits allows for restoration to earlier versions of the project should any changes end up breaking the project. In particular GitHub was used to host the repository allowing for the repository to be stored away from the development environment to ensure development on the project didn’t cause any unintended alterations to the project.

The development environment for the project was a python3 virtual environment (venv) set up on a virtual machine (EC2 Instance) running Ubuntu 20.something. Using a venv allows for pip installs and the application to be run without any conflicts between other pip install versions installed on the same machine.

[**insert terminal/instance screenshots here?**]
