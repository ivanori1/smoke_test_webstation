Feature: Login Failed

  Scenario Outline: EULA not accepted
    Given Open WebStation login page
    When Select language "<languages>"
    When Click on Login button
    Then Error appears: "<messages>"

    Examples:
      | languages |  | messages                                                              |
      | English   |  | You have to accept the End User License Agreement in order to log in. |
      | Deutch    |  | Sie müssen die Nutzungsbestimmungen akzeptieren, um sich einzuloggen. |

  Scenario Outline: EULA is accepted
    Given Select language "<languages>"
    """
    the text of scenario is Username and password fields are empty
    """
    When Username " " and password " "
    And Stay logged in option is "unchecked"
    And Accept EULA is "checked"
    And Click on Login button
    Then Error appears: "<messages>"
    Examples:
      | languages |  | messages                                                               |
      | English   |  | The username or password is incorrect Please try again.                |
      | Deutch    |  | Benutzername oder Passwort ist falsch Bitte versuchen Sie es nochmals. |

  Scenario Outline: Invalid user:
    Given  Select language "<languages>"
    When Username "test.test18" and password "test12"
    And Accept EULA is "checked"
    And Click on Login button
    Then Error appears: "<messages>"
    Examples:
      | languages |  | messages                                                                                             |
      | English   |  | This user account is disabled. Please contact the support team for further actions.                  |
      | Deutch    |  | Dieser Benutzerzugang ist deaktiviert. Bitte kontaktieren Sie das Support Team für weitere Aktionen. |

  Scenario: Success login
    Given Select language "English"
    When Username "ivan.coric91" and password "ictrader123"
    And Accept EULA is "checked"
    And Click on Login button
    Then Home page will appear