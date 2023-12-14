# MongoDB Exercises

## Prerequisites:
- Create a database named `LibraryDB`.
- Within `LibraryDB`, create two collections: `Books` and `Members`.
- In the `Books` collection, insert the following documents:

  | Title                   | Author           | Year Published | Genre     |
  |-------------------------|------------------|----------------|-----------|
  | The Hobbit              | J.R.R. Tolkien   | 1937           | Fantasy   |
  | 1984                    | George Orwell    | 1949           | Dystopian |
  | To Kill a Mockingbird   | Harper Lee       | 1960           | Fiction   |

- In the `Members` collection, insert the following documents:

  | Name          | Membership Start Date | Borrowed Books                |
  |---------------|-----------------------|-------------------------------|
  | Alice Johnson | 2021-06-15            | ["The Hobbit", "1984"]        |
  | Bob Smith     | 2020-01-20            | ["To Kill a Mockingbird"]     |
  | Carol White   | 2022-03-11            | []                            |

## Basic Find Queries

**Task**:
- Write a query to find all books published on 1949.

**Expected Output**:
- Documents containing:
  - "1984" by George Orwell

## Find with Projection: Specific Fields

**Task**:
- Retrieve only the titles and authors of all books in the `Books` collection.

**Expected Output**:
- Documents with fields:
  - Title: "The Hobbit", Author: "J.R.R. Tolkien"
  - Title: "1984", Author: "George Orwell"
  - Title: "To Kill a Mockingbird", Author: "Harper Lee"

**Task**:
- Write a query in the `Members` collection to retrieve only the names of members and their borrowed books.

**Expected Output**:
- Documents with fields:
  - Name: "Alice Johnson", Borrowed Books: ["The Hobbit", "1984"]
  - Name: "Bob Smith", Borrowed Books: ["To Kill a Mockingbird"]
  - Name: "Carol White", Borrowed Books: []

## Exclude Specific Fields

**Task**:
- Perform a query on the `Books` collection to retrieve all documents but exclude the `year_published` field.

**Expected Output**:
- Documents with fields:
  - Title: "The Hobbit", Author: "J.R.R. Tolkien", Genre: "Fantasy"
  - Title: "1984", Author: "George Orwell", Genre: "Dystopian"
  - Title: "To Kill a Mockingbird", Author: "Harper Lee", Genre: "Fiction"

## Combining Filters and Projection

**Task**:
- Query the `Books` collection to find books in the "Fantasy" genre, but return only the title and year published.

**Expected Output**:
- Document with fields:
  - Title: "The Hobbit", Year Published: 1937

## Projection with Limited Fields in Members

**Task**:
- Retrieve the membership start dates and borrowed books of all members in the `Members` collection, excluding their names.

**Expected Output**:
- Documents with fields:
  - Membership Start Date: "2021-06-15", Borrowed Books: ["The Hobbit", "1984"]
  - Membership Start Date: "2020-01-20", Borrowed Books: ["To Kill a Mockingbird"]
  - Membership Start Date: "2022-03-11", Borrowed Books: []


## Using `$and` Operator

**Task**:
- Query the `Books` collection to find books that were published after 1930 and are of the genre "Fiction".

**Expected Output**:
- Document with fields:
  - Title: "To Kill a Mockingbird", Author: "Harper Lee", Year Published: 1960, Genre: "Fiction"

## Using `$lt` (Less Than) Operator

**Task**:
- Write a query in the `Books` collection to find books published before 1950.

**Expected Output**:
- Documents with fields:
  - Title: "The Hobbit", Author: "J.R.R. Tolkien", Year Published: 1937, Genre: "Fantasy"
  - Title: "1984", Author: "George Orwell", Year Published: 1949, Genre: "Dystopian"

## Using `$gt` (Greater Than) Operator

**Task**:
- Find members in the `Members` collection who joined after January 1, 2021.

**Expected Output**:
- Documents with fields:
  - Name: "Alice Johnson", Membership Start Date: "2021-06-15", Borrowed Books: ["The Hobbit", "1984"]
  - Name: "Carol White", Membership Start Date: "2022-03-11", Borrowed Books: []

## Combining `$gt` and `$lt`

**Task**:
- Query the `Books` collection to find books whose year of publication is between 1940 and 1960, inclusive.

**Expected Output**:
- Document with fields:
  - Title: "1984", Author: "George Orwell", Year Published: 1949, Genre: "Dystopian"
  - Title: "To Kill a Mockingbird", Author: "Harper Lee", Year Published: 1960, Genre: "Fiction"

## Using `$in` Operator

**Task**:
- Find books in the `Books` collection where the genre is either "Fantasy" or "Dystopian".

**Expected Output**:
- Documents with fields:
  - Title: "The Hobbit", Author: "J.R.R. Tolkien", Year Published: 1937, Genre: "Fantasy"
  - Title: "1984", Author: "George Orwell", Year Published: 1949, Genre: "Dystopian"

## Using `$or` Operator

**Task**:
- Query the `Members` collection to find members who either joined before 2021 or have borrowed more than 1 book.

**Expected Output**:
- Documents with fields:
  - Name: "Alice Johnson", Membership Start Date: "2021-06-15", Borrowed Books: ["The Hobbit", "1984"]
  - Name: "Bob Smith", Membership Start Date: "2020-01-20", Borrowed Books: ["To Kill a Mockingbird"]
