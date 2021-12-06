@flight_search
Feature: Ryanair flight search
  As a Ryanair user,
  I want to find flight in specified dates.


  Background:
    Given I am on "main" page

  @one_way
  Scenario Outline: Verify user is finding flights in specified dates
    When I  input "<departure airport>" to "From Airport"
    And I input "<destination airport>" to "To Airport"
    And I choose "<depart date>" at "Depart Form"
    And I choose "<return date>" at "Return Form"


    Then I should see "flight contents" from "departure airport" to "destination airport" at "flight date"
    And I should see "flight contents" from "destination airport" to "departure airport" at "return date"
#    But I can should see "absence message"

    Examples: Flights
      | Departure Location      | Destination Location | depart date | return date |
      | Berlin Brandenburg      | Rome Fiumicino       | 04/14/2022  | 04/20/2022  |
      | Rome Fiumicino          | Brussels             | 03/09/2022  | 03/24/2022  |
      | Milan Bergamo           | Berlin Brandenburg   | 05/12/2022  | 05/18/2020  |