<!--
[contributors-shield][contributors-url]
[forks-shield][forks-url]
[stars-shield][stars-url]
[issues-url]
-->
<div align="center">
    <img src="https://github.com/BookHaven/BookHaven-BE/assets/120225785/10a11ac0-fbc8-4dd4-9688-9d5e090a3912" alt="Logo" width="700" height="175">
  </a>
</div>
<br>
  <p align="center">
    BookHaven is a web application built for the Turing School of Software and Design's Mod 4 Capstone project. Read more about project requirements: https://mod4.turing.edu/projects/capstone/
    <br />
  </p>

  <details>
    <summary>Table of Contents</summary>
    <ol>
      <li>
        <a href="#about">About The Project</a>
        <ul>
          <li><a href="#built-with">Built With</a></li>
        </ul>
      </li>
      <li>
        <a href="#getting-started">Getting Started</a>
      </li>
      <li><a href="#database-schema">Database Schema</a></li>
      <li><a href="#testing">Testing</a></li>
      <li><a href="#endpoints">Endpoints</a></li>
      <li><a href="#contributors">Contributors</a></li>
      <li><a href="#acknowledgments">Acknowledgments</a></li>
    </ol>
  </details>

<!-- ABOUT THE PROJECT -->
## About the Project

Welcome to Bookhaven! We have designed this software to streamline the inventory management of Little Free Libraries. We aim to connect books to readers in the most efficient way possible. Our application allows you to keep track of books in your library and explore the books in libaries near you, ensuring that each story finds a reader. For more information, visit Little Free Libraries at [Little Free Library](https://littlefreelibrary.org/).

Check out our front end repository: [![Github][Github]][project-fe-gh-url]


<!-- BUILT WITH -->
### Built With

* [![python][python]][python-url]
* [![Django][Django]][Django-url]
* [![Pytest][Pytest]][pytest-url]
* [![PostgreSQL][Postgres]][Postgres-url]
* [![Heroku][Heroku]][Heroku-url]


<!-- GETTING STARTED -->
## Getting Started
### Setting up a local Postgresql database (rough draft)
- Step 1: Install PostgreSQL with HomeBrew
  - Follow [these](https://www.moncefbelyamani.com/how-to-install-postgresql-on-a-mac-with-homebrew-and-lunchy/) instructions.
- Step 2: Create a new user in the PostgreSQL interactive terminal
  > **_Note:_** If you would like to immediately utilize this repository without altering database code follow the instructions below.  If you would like to use your own username/password skip to step 3.

  - Open the PostgreSQL interactive terminal.
    - In a terminal window type `psql` .
    - You should see:
    ```
    psql (14.8 (Homebrew))
    username=#
  - Next create a new username and password and give this new user access to create a database.
    ```
    username=# CREATE USER bookhaven WITH PASSWORD 'password';
    username=# ALTER USER bookhaven CREATEDB;
    ```
- Step 3: Create the database
  - Exit out of the interactive terminal by entering `\q` .
  - If you followed the steps above enter:
    ```
    createdb -U bookhaven -W book_haven
    ```
      - It should ask you for your password which will be `password` .
  - If you want to use your own username and custom database name enter:
    ```
    createdb <name_of_database>
    ```
  - Check to make sure the database was created. 
    - Open the PostgreSQL interactive terminal with `psql` .
    - Enter `\l` to show the list of all databases where you should see `book_haven` or the name you chose listed.

<!-- steps to run the application locally -->


<!-- DATABASE SCHEMA -->
### Database Schema

![Screenshot 2023-07-13 at 3 39 32 PM](https://github.com/RentInform/BE-Rent-Inform/assets/105441393/5def21c9-54ec-4167-b05c-8deb9f0ad164)


<!-- TESTING -->
### Testing

<!-- to run tests... -->


<!-- CONTRIBUTORS -->
### Contributors

* Alec Kapicak: [![Linkedin][linkedin]][alec-li-url] [![Github][Github]][alec-gh-url]
* Andrew Bingham: [![Linkedin][linkedin]][andrew-li-url] [![Github][Github]][andrew-gh-url]
* Thomas Hawley: [![Linkedin][linkedin]][thomas-li-url] [![Github][Github]][thomas-gh-url]
* Grace Joh: [![Linkedin][linkedin]][grace-li-url] [![Github][Github]][grace-gh-url]

* Front End: [![Github][Github]][project-fe-gh-url]
* Back End: [![Github][Github]][project-be-gh-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- ACKNOWLEDGEMENTS -->
### Acknowledgments

* Sara Park - Front End Developer
* Tiala Young - Front End Developer
* Jamison Ordway - Project Manager
* Judson Stevens - Project Mentor
* [Turing School of Software and Design](https://turing.io/)
* [Little Free Libraries](https://littlefreelibrary.org/)

<div align="center">
    <img src="https://github.com/BookHaven/BookHaven-BE/assets/120225785/6081c2b9-8ba5-48c9-be0f-a9618104d0d6" alt="Logo" width="675" height="700">
  </a>
</div>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[bookhaven-logo]: https://github.com/BookHaven/BookHaven-BE/assets/120225785/4b2c5f42-5820-4171-a0b9-aa48bd5f42e4
[bookhaven-library]: https://github.com/BookHaven/BookHaven-BE/assets/120225785/ee11b767-2ee8-430d-bcf4-f72d1ceae806
[contributors-shield]: https://img.shields.io/github/contributors/BookHaven/BookHaven-BE.svg?style=for-the-badge
[contributors-url]: https://github.com/BookHaven/BookHaven-BE/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/BookHaven/BookHaven-BE.svg?style=for-the-badge
[forks-url]: https://github.com//ithill22/draft_madness_be/network/members
[stars-shield]: https://img.shields.io/github/stars/BookHaven/BookHaven-BE.svg?style=for-the-badge
[stars-url]: https://github.com/BookHaven/BookHaven-BE/stargazers
[issues-url]: https://github.com/BookHaven/BookHaven-BE/issues

<!-- tech stack -->
[python]: https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white
[python-url]: https://www.python.org/
[django]: https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white
[django-url]: https://www.djangoproject.com/
[pytest]: https://img.shields.io/badge/PyTest-3776AB?style=for-the-badge&logo=pytest&logoColor=white
[pytest-url]: https://docs.pytest.org/en/7.4.x/
[slack-shield]:	https://img.shields.io/badge/Slack-4A154B?style=for-the-badge&logo=slack&logoColor=white
[Postgres]: https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white
[Postgres-url]: https://www.postgresql.org/
[Heroku]: https://img.shields.io/badge/Heroku-430098?style=for-the-badge&logo=heroku&logoColor=white
[Heroku-url]: https://www.heroku.com

<!-- linkedin -->
[linkedin]: https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white
[alec-li-url]: https://www.linkedin.com/in/alec-kapicak-b703bab8/
[andrew-li-url]: https://www.linkedin.com/in/andrew-bingham1/
[thomas-li-url]: https://www.linkedin.com/in/thomas-hawley-901612123/
[grace-li-url]: https://www.linkedin.com/in/graceehjoh/

<!-- github -->
[Github]: https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white
[project-fe-gh-url]: https://github.com/BookHaven/BookHaven-FE
[project-be-gh-url]: https://github.com/BookHaven/BookHaven-BE
[alec-gh-url]: https://github.com/AlecKap
[andrew-gh-url]: https://github.com/andrew-bingham1
[thomas-gh-url]: https://github.com/thawley2
[grace-gh-url]: https://github.com/grace-joh
