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
    Given Username " " and password " "
    """
    the text of scenario is Username and password fields are empty
    """
    When Select language "<languages>"
    And Stay logged in option is "unchecked"
    And Accept EULA is "checked"
    And Click on Login button
    Then Error appears: "<messages>"
    Examples:
      | languages |  | messages                                                               |
      | English   |  | You have to accept the End User License Agreement in order to log in.  |
      | Deutch    |  | Benutzername oder Passwort ist falsch Bitte versuchen Sie es nochmals. |

