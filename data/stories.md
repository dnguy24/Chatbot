## ask_direction
* greet
    - utter_greet
* ask_directions{"directions":"hoyt", "directions":"douglass"}
    - return_direction
## ask_direction2
* greet
    - utter_greet
* ask_directions_start_missing{"directions":"hoyt"}
    - return_direction
* inform_starting_location{"directions":"dfo"}
    - return_direction
## ask_opening_hour
* greet
    - utter_greet
* hungry
    - request_open_dininghalls
* goodbye
    - utter_goodbye
    
## ask_opening_hour 2
* greet
    - utter_greet
* hungry{"dininghall":"hillside"}
    - request_open_dininghalls
## ask_direction2
* greet
    - utter_greet
* ask_directions_start_missing{"directions":"douglass"}
    - return_direction
* inform_starting_location{"directions":"morey"}
    - return_direction
 
## ask_coffee
* greet
    - utter_greet
* ask_coffee
    - request_coffee
* thankyou
    - utter_welcome


## ask_weather
* greet
    - utter_greet
* ask_weather
    - request_weather
* goodbye
    - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## fallback
- utter_unclear