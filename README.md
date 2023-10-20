# jitto-fullstack-challenge

Note: when I initially read the challenge description, I thought it was for dealing with user data specifically. 
Throughout the implementation of my API, I reffered to the data as 'users' instead of 'items' but the underlying functionality is the same.

## Accessing the API
- API Key: The API is secured with an API key, which is included in my email submission
- Base URL: The base url is also included in my email submission

## API endpoints

/get-user (GET):
- Returns the name and description associated with a specific user
- Query string params: id

/get-all-users (GET):
- Returns all contents of the table
- Query string params: none

/new-user (POST):
- Creates a new user and returns the user's auto-generated UUID
- Query string params: name, description

## DynamoDB
- Each entry consists of: id, name, description
- Primary partition key: id
- The GitHub has a CSV of test data created using the API's POST method

## CloudWatch
- The API logs events to a CloudWatch log group
- The GitHub has a JSON file with log data from testing the API

## Rate limiting
- I created a useage plan to implement rate limiting for the API
- Throttling: 10 requests/sec
- Quota: 100 requests/day
