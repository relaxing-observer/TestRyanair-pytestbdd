Feature: Ryanair flight search
  As a Ryanair user,
  I want to find flight in specified dates.
Background:
  Given I am on "main" page

  @flights_search
  Scenario Outline: Verify user is finding flights in specified dates

    When I input "<departure airport>" to From Airport Form on "flights" tab
    And I input "<destination airport>" to To Airport Form on "flights" tab
    And I choose "<depart date>" at Depart Form on "flights" tab
    And I choose "<return date>" at Return Form on "flights" tab
    Then I should see flight cards from "<departure airport>" to "<destination airport>" at "<depart date>" and "<return date>" at "search flights" page

    Examples: Flights
      | departure airport       | destination airport  | depart date | return date |
      | Berlin Brandenburg      | Rome Fiumicino       | 27 Apr 2022 | 5 May 2022  |
      | Rome Fiumicino          | Brussels Charleroi   | 14 May 2022 | 25 May 2022 |
      | Milan Bergamo           | Berlin Brandenburg   | 13 Apr 2022 | 18 Apr 2022 |