Feature: Ryanair hotels search
  As a Ryanair user,
  I want to find hotel in specified dates.
Background:
  Given I am on main page

  @hotels_search
  Scenario Outline: Verify user is finding hotels in specified dates
    When I choose hotels tab
    And I input <location> to Destination Form
    And I choose <check-in date> at Check-In Form
    And I choose <check-out date> at Check-out Form
    Then I should see accommodation cards in <location> from <check-in date> to <check-out date>

    Examples: Hotels
      | location    | check-in date   | check-out date  |
      | Kotor       | 27 Apr 2022     | 5 May 2022      |
      | Venezia     | 14 May 2022     | 25 May 2022     |
      | Prague      | 13 Apr 2022     | 18 Apr 2022     |
      | Oslo        | 13 Apr 2022     | 18 Apr 2022     |