Feature: Ryanair cars search
  As a Ryanair user,
  I want to find cars in specified locations and dates.
Background:
  Given I am on main page

  @cars_search
  Scenario Outline: Verify user is finding car in specified dates
    When I choose cars tab
    And I input <location> to City Form
    And I choose <pick-up date> at Pick-Un Form
    And I choose <drop-off date> at Drop-Off Form
    And I choose <pick-up time> at Pick-Un Form
    And I choose <drop-off time> at Drop-Off Time
    Then I should see cards cards in <location> from <pick-up date> at <drop-off date> to <pick-up time> at <drop-off time>

    Examples: Hotels
      | location    | pick-up date    | drop-off date  | pick-up time | drop-off time |
      | Oslo       | 27 Apr 2022     | 5 May 2022     | 14:00        | 19:00         |
#      | Venezia     | 14 May 2022     | 25 May 2022    | 10:00        | 20:00         |
#      | Prague      | 13 Apr 2022     | 18 Apr 2022    | 11:00        | 21:00         |
#      | Oslo        | 13 Apr 2022     | 18 Apr 2022    | 12:00        | 16:00         |