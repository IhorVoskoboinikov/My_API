# **My api**
___
## My api - this is an application that allows the user to interact with the site (in our case, play). Our project has the following features:

+  Player registration
+ Getting a list of players (everyone who registered, who plays, who does not play)
+ Changing the player's status (login or logout)
+ Getting information about a user by id
+ Deleting a user
___

## Setup:

+ ```git clone https://github.com/IhorVoskoboinikov/My_API```
+ ```pip install -r requirements.txt```
+ ```uvicorn test_project.app:app```
___

## Usage:

> 1. go to the url where our website was launched
> 2. go to the site documentation by adding http://127.0.0.1:8000/docs in the address bar
___

## The REST API to the example app is described below:
### _Get All Users:_
> + GET/operation/Get All Users
>   + Status == '--'  list all users who have registered from database
>   + Status == 'in game'  list all users who in game now from database
>   + Status == 'out game'  list all users who out game now from database

### _Created User:_
> + POST/operation/Created User
>   + Add user with {user_id} to database

### _Get User:_
> + GET/operation/{user_id} Get User
>   + Get user by {user_id} from database

### _Get User:_
> +  PUT/operation/{user_id} Enter And Out Game
>   + Change the status of the user by {user_id} "in the game" or "out of the game" and write to the database

### _Delete User:_
> + DELETE/operation/Delete User
>   + Remove user with {user_id} from database