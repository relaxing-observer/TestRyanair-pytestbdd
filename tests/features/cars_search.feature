Feature: Ryanair cars search
  As a Ryanair user,
  I want to find cars in specified locations and dates.
Background:
  Given I am on "main" page
  @cars_search
  Scenario Outline: Verify user is finding car in specified dates
    When I choose "cars" tab on "main" page
    And I input "<location>" on "cars" tab
    And I select "<pick-up-date>" on "cars" tab to pick
    And I select "<drop-off-date>" on "cars" tab to drop
    And I choose "<pick-up-time>" on "cars" tab to pick
    And I choose "<drop-off-time>" on "cars" tab to drop
    Then I should see car cards in "<location>" on "search cars" page
    And I should see "<pick-up-date>" to "<drop-off-date>" and "<pick-up-time>" to "<drop-off-time>" on "search cars" page

    Examples: Hotels
    | location    | pick-up-date    | drop-off-date  | pick-up-time | drop-off-time |
    | Oslo        | 27 Apr 2022     | 5 May 2022     | 14:00        | 19:00         |
     cars | Prague      | 13 Apr 2022     | 18 Apr 2022    | 11:00        | 21:00         |
     cars | Vienna        | 13 Apr 2022     | 18 Apr 2022    | 12:00        | 16:00         |