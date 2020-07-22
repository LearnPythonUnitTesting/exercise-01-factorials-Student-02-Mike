Feature: factorials

  Scenario Outline: factorials
    Given I have a positive integer <i>
    When calculate factorial
    Then I get a factorial of the integer <f>

    Examples: factorials
      | i | f  |
      | 2 | 2  |
      | 3 | 6  |
      | 4 | 24 |