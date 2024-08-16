## Setup
Before installing, create your .env file and copy everything from the .env.sample. You should have docker running, in console type docker compose build, after successful docker compose up. And done!


## Usage
To run the tests use the command - ./bin/manage test apps.books.tests.test_book_api.BookAPITestCase.
There is a Swagger installed here, so you can go to http://0.0.0.0:8002/swagger/ for a convenient test. There you will see all available APIs.
