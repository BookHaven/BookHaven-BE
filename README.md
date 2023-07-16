[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

<div align="center">
    <img src="https://github.com/ResidentMario/missingno/assets/105441393/1b76aa4d-80a8-400b-97fc-792e83bcc2ce" alt="Logo" width="700" height="175">
  </a>
</div>
<br>
  <p align="center">
    BookHaven is a web application built for the Turing School of Software and Design's Mod 4 Capstone project. </br>
    Read more about project requirements <a href=project-requirements>here</a>.
    <br />
    <br />
    Check out our <a href=FE-deployment>deployed website</a>!
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
      <li><a href="#endpoints">Endpoints</a></li>
      <li><a href="#getting-started">Getting Started</a></li>
      <li><a href="#database-schema">Database Schema</a></li>
      <li><a href="#testing">Testing</a></li>
      <li><a href="#contributors">Contributors</a></li>
      <li><a href="#acknowledgments">Acknowledgments</a></li>
    </ol>
  </details>

<!-- ABOUT THE PROJECT -->
## About the Project

Welcome to Bookhaven! We have designed this software to streamline the inventory management of Little Free Libraries. We aim to connect books to readers in the most efficient way possible. Our application allows you to keep track of books in your library and explore the books in libaries near you, ensuring that each story finds a reader. For more information about Little Free Library, visit them at [LittleFreeLibrary.org](https://littlefreelibrary.org/).

Check out our front end repository: [![Github][Github]][project-fe-gh-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- BUILT WITH -->
### Built With

[![python][python]][python-url] [![Django][Django]][Django-url] [![Pytest][Pytest]][pytest-url] [![PostgreSQL][Postgres]][Postgres-url] [![Heroku][Heroku]][Heroku-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- ENDPOINTS -->
## Endpoints

### GET /api/v0/libraries

<details>
<summary>Response</summary>

Status: 200
```json
{
    "data": [
        {
            "id": 1,
            "type": "library",
            "attributes": {
                "name": "Jen & Eric's Library",
                "address": {
                    "street": "3410 W 98th Dr",
                    "city": "Westminster",
                    "state": "CO",
                    "zip": "80210"
                },
                "location": {
                    "latitude": 39.7392,
                    "longitude": -104.9903
                },
                "book_count": 12
            }
        },
        {
            "id": 2,
            "type": "library",
            "attributes": {
                "name": "Tom and Jerry's Library",
                "address": {
                    "street": "123 S Street",
                    "city": "Littleton",
                    "state": "CO",
                    "zip": "80209"
                },
                "location": {
                    "latitude": 39.7392,
                    "longitude": -104.9903
                },
                "book_count": 15
            }
        }
    ]
}
```

</details>

### GET /api/v0/libraries/:id

<details>
<summary>Response</summary>

Status: 200 OK
```json
{
    "data": {
         "id": 1, 
         "type": "library",
         "attributes": {
             "name": "Jen & Eric's Library",
             "address": {
                 "street": "3410 W 98th Dr",
                 "city": "Westminster",
                 "state": "CO",
                 "zip": "80123"
             },
             "location": {
                 "latitude": 39.7392,
                 "longitude": -104.9903
             }, 
             "book_count": 12
         }
    }
}
```

Status: 404 Not Found
```json
{
  "errors": [
    {
      "status": "404",
      "title":  "Library not found",
      "detail": "The library with id 1 does not exist."
    }
  ]
}
```
</details>

### GET /api/v0/libraries/:id/books

<details>
<summary>Response</summary>

Status: 200 OK
```json
{
	"data": [{
			"id": 1,
			"type": "book",
			"attributes": {
				"isbn": "9781101883082",
				"book_image": "http://books.google.com/books/content?id=wg0dDgAAQBAJ&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api",
				"description": "NEW YORK TIMES BESTSELLER - One million copies sold! Inspired by the life of a real World War II heroine, this remarkable debut novel reveals the power of unsung women to change history in their quest for love, freedom, and second chances. 'Extremely moving and memorable . . . This impressive debut should appeal strongly to historical fiction readers and to book clubs that adored Kristin Hannah's The Nightingale and Anthony Doerr's All the Light We Cannot See.'",
				"title": "Lilac Girls",
				"author": "Martha Hall Kelly",
				"genre": "Fiction",
				"library_id": 1
			}
		},
		{
			"id": 2,
			"type": "book",
			"attributes": {
				"isbn": "9781680680324",
				"book_image": "http://books.google.com/books/content?id=c28RMQAACAAJ&printsec=frontcover&img=1&zoom=1&source=gbs_api",
				"description": "Bob Johansson has just sold his software company and is looking forward to a life of leisure. There are places to go, books to read, and movies to watch. So it's a little unfair when he gets himself killed crossing the street.Bob wakes up a century later to find that corpsicles have been declared to be without rights, and he is now the property of the state. He has been uploaded into computer hardware and is slated to be the controlling AI in an interstellar probe looking for habitable planets. The stakes are high: no less than the first claim to entire worlds. If he declines the honor, he'll be switched off, and they'll try again with someone else. If he accepts, he becomes a prime target. There are at least three other countries trying to get their own probes launched first, and they play dirty.The safest place for Bob is in space, heading away from Earth at top speed. Or so he thinks. Because the universe is full of nasties, and trespassers make them mad - very mad.",
				"title": "We Are Legion (We Are Bob)",
				"author": "Dennis E. Taylor",
				"genre": "Fiction",
				"library_id": 1
			}
		},
		{
			"id": 3,
			"type": "book",
			"attributes": {
				"isbn": "9780451524935",
				"book_image": "http://books.google.com/books/content?id=ocNGwgEACAAJ&printsec=frontcover&img=1&zoom=1&source=gbs_api",
				"description": "Written more than 70 years ago, 1984 was George Orwell's chilling prophecy about the future. And while 1984 has come and gone, his dystopian vision of a government that will do anything to control the narrative is timelier than ever... - Nominated as one of America's best-loved novels by PBS's The Great American Read - 'The Party told you to reject the evidence of your eyes and ears. It was their final, most essential command.' Winston Smith toes the Party line, rewriting history to satisfy the demands of the Ministry of Truth. With each lie he writes, Winston grows to hate the Party that seeks power for its own sake and persecutes those who dare to commit thoughtcrimes. But as he starts to think for himself, Winston can't escape the fact that Big Brother is always watching... A startling and haunting novel, 1984 creates an imaginary world that is completely convincing from start to finish. No one can deny the novel's hold on the imaginations of whole generations, or the power of its admonitions-a power that seems to grow, not lessen, with the passage of time.",
				"title": "1984",
				"author": "George Orwell",
				"genre": "Fiction",
				"library_id": 1
			}
		}
	]
}
```

</details>

### POST /api/v0/libraries/:id/books

<details>
<summary>Request</summary>

```json
{
  "isbn": "12345"
}
```
</details>

<details>
<summary>Response</summary>

Status: 201 Created
```json
{
	"data": {
		"id": 1,
		"type": "books",
		"attributes": {
			"isbn": "12345",
			"book_image": "https://img.freepik.com/free-photo/book-composition-with-open-book_23-2147690555.jpg?w=1380&t=st=1688765682~exp=1688766282~hmac=6e996dd47de09ce70e8aa6e4cb31495d8773ce0bb860ce8869d09b8657fb3166",
			"description": "Books is good",
			"summary": "Books is good",
			"title": "Slacking 101",
			"author": "Jacob",
			"genre": "Educational",
			"library_id": 1
		}
	}
}

```

Status: 422 Unprocessable Entity
```json
{
  "errors": [
    {
      "status": "422",
      "title":  "Book not created",
      "detail": "Book could not be created because ISBN not found."
    }
  ]
}
```
</details>

### DESTROY /api/v0/libraries/:id/books/:id

<details>
<summary>Response</summary>

Status: 200 OK
```json
{
    "data": {
            "id": 1,
            "detail": "The book with id 1 was deleted."
    }
}
```

Status: 404 Not found
```json
{
    "errors": [
        {
            "status": "404",
            "title": "Book not found",
            "detail": "The book with id -1 does not exist."
        }
    ]
}
```
</details>

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- GETTING STARTED -->
## Getting Started

<!-- steps to run the application locally -->
### Setting up a local Postgresql database
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

### Install version 3.11.4 of python with HomeBrew
- Follow [these](https://www.pythoncentral.io/installing-python-on-mac-using-homebrew/) instructions. 

### Clone the repository
- Step 1: In a terminal window, navigate to a directory where you would like the project to live. 
- Step 2: Run `git clone git@github.com:BookHaven/BookHaven-BE.git`

### Setup virtual environment and install dependencies
- Step 1: In a terminal window, navigate just outside of the project directory. 
- Step 2: Create an environment.
  - run `python3 -m venv <name_of_environment>` 
- Step 3: Activate environment. 
  - run `source <name_of_environment>/bin/activate`
    - In your terminal you should now see something like 
      ```
      (<name_of_environment>) /Users/<username>
      ```
- Step 4: install dependencies
  - With the virtual environment still running navigate inside of the BookHaven directory
  - run `pip install -r requirements.txt`
    - all dependencies and versions will be loaded into your virtual environment. 

### Connect local database to application
> **_Note:_** If you followed 'Setting up a local Postgresql database' completely continue to step 2.  If you used the default user to create the local database continue to step 1. 
- Step 1: Update the settings file with your database credentials
  - Open the repository in your code editor of choice and navigate to 'book_haven/settings.py'
  - Scroll down to _'DATABASES'_ and change the following in the _'os.getenv('DJANGO_TEST')'_ section. 
  - Change _'NAME'_ to the database name you created. 
  - change _'USER'_ to your username and change _'PASSWORD'_ to be an empty string `''`
- Step 2: migrate the database schema to link and create the tables in your local database
  - In your terminal with the virtual environment running and inside of the BookHaven directory run:
    ```
    python manage.py migrate
    ```
    - A list of `OK`'s should display
    - Your local database is now connected and populated with the required tables.

### Obtain a Google API key
- Follow [these](https://developers.google.com/books/docs/v1/getting_started#getaccount) instructions to obtain a google API key
- In the root project directory create a file named `.env`
  - Within that file paste this `MY_API_KEY='<google_api_key>'` and replace google_api_key with your google api key
- Run test suite to verify everything was set up correctly
  - In your terminal with the virtual environment active and while inside the BookHaven directory run:
    ```
    export DATABASE_PASSWORD='1'
    export DJANGO_TEST=True
    pytest
    ```
      - You should have 8 passing tests


<!-- TESTING -->
### Testing

To run the test suite, run `pytest` in the terminal. You should have 8 passing tests.
*All tests are passing at time of writing.*

![Testing Coverage](https://github.com/BookHaven/BookHaven-BE/assets/119075417/6f8a250b-941e-4519-81aa-7d1c41c58ab3)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- DATABASE SCHEMA -->
## Database Schema

![Database Schema](https://github.com/RentInform/BE-Rent-Inform/assets/105441393/5def21c9-54ec-4167-b05c-8deb9f0ad164)

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- CONTRIBUTORS -->
## Contributors

| [<img alt="Alec Kapicak" width="100" src=".github/images/alec.jpeg"/>][alec-li-url] | [<img alt="Andrew Bingham" width="100" src=".github/images/andrew.jpeg"/>][andrew-li-url] | [<img alt="Grace Joh" width="100" src=".github/images/grace.jpeg"/>][grace-li-url] | [<img alt="Thomas Hawley" width="100" src=".github/images/thomas.jpeg"/>][thomas-li-url] | 
| ------------------ | ------------ | -------------- | ----------- | 
| Alec Kapicak | Andrew Bingham | Grace Joh | Thomas Hawley | 
| Developer | Developer | Developer | Developer |
| [![Github][Github]][alec-gh-url] | [![Github][Github]][andrew-gh-url] | [![Github][Github]][grace-gh-url] | [![Github][Github]][thomas-gh-url] | 
| [![Linkedin][linkedin]][alec-li-url] | [![Linkedin][linkedin]][andrew-li-url] | [![Linkedin][linkedin]][grace-li-url] | [![Linkedin][linkedin]][thomas-li-url] | 


<!-- ACKNOWLEDGEMENTS -->
## Acknowledgments

| Tiala Young | Sara Park | Judson Stevens | Jamison Ordway |
| ------------------ | ------------ | -------------- | ----------- | 
| Front End | Front End | Project Mentor | Project Manager |
| [![Github][Github]][tiala-gh-url] | [![Github][Github]][sara-gh-url] | [![Github][Github]][judson-gh-url] | [![Github][Github]][jamison-gh-url] | 
| [![Linkedin][linkedin]][tiala-li-url] | [![Linkedin][linkedin]][sara-li-url] | [![Linkedin][linkedin]][judson-li-url] | [![Linkedin][linkedin]][jamison-li-url] |

### Special Thanks to
* [Turing School of Software and Design](https://turing.io/)
* [Little Free Library](https://littlefreelibrary.org/)
</br>
</br>

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<div align="center">
  <h3 style='font-size: 36px;'>Thanks for Visiting!</h3>
  </br>
    <img src="https://github.com/ResidentMario/missingno/assets/105441393/31d504e0-593a-4317-9707-470c37be2851" alt="Logo" width="675" height="700">
  </a>
</div>

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[bookhaven-logo]: https://github.com/ResidentMario/missingno/assets/105441393/1b76aa4d-80a8-400b-97fc-792e83bcc2ce
[bookhaven-library]: https://github.com/ResidentMario/missingno/assets/105441393/31d504e0-593a-4317-9707-470c37be2851
[project-requirements]: https://mod4.turing.edu/projects/capstone/
[FE-deployment]: <!-- ADD DEPLOYED SITE HERE -->
[contributors-shield]: https://img.shields.io/github/contributors/BookHaven/BookHaven-BE.svg?style=for-the-badge
[contributors-url]: https://github.com/BookHaven/BookHaven-BE/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/BookHaven/BookHaven-BE.svg?style=for-the-badge
[forks-url]: https://github.com/BookHaven/BookHaven-BE/network/members
[stars-shield]: https://img.shields.io/github/stars/BookHaven/BookHaven-BE.svg?style=for-the-badge
[stars-url]: https://github.com/BookHaven/BookHaven-BE/stargazers
[issues-shield]: https://img.shields.io/github/issues/RentInform/BE-Rent-Inform.svg?style=for-the-badge
[issues-url]: https://github.com/BookHaven/BookHaven-BE/issues

<!-- tech stack -->
[python]: https://img.shields.io/badge/Python-3776AB.svg?style=for-the-badge&logo=python&logoColor=white
[python-url]: https://www.python.org/
[django]: https://img.shields.io/badge/Django-092E20.svg?style=for-the-badge&logo=django&logoColor=white
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
[tiala-li-url]: https://www.linkedin.com/in/tialayoung/
[sara-li-url]: https://www.linkedin.com/in/soyeon-sara-park/
[Jamison-li-url]: https://www.linkedin.com/in/jamisonordway/
[Judson-li-url]: https://www.linkedin.com/in/judsonstevens/


<!-- github -->
[Github]: https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white
[project-fe-gh-url]: https://github.com/BookHaven/BookHaven-FE
[project-be-gh-url]: https://github.com/BookHaven/BookHaven-BE
[alec-gh-url]: https://github.com/AlecKap
[andrew-gh-url]: https://github.com/andrew-bingham1
[thomas-gh-url]: https://github.com/thawley2
[grace-gh-url]: https://github.com/grace-joh
[tiala-gh-url]: https://github.com/tialaaa
[sara-gh-url]: https://github.com/soy-park
[Jamison-gh-url]: https://github.com/jamisonordway
[Judson-gh-url]: https://github.com/JudsonStevens