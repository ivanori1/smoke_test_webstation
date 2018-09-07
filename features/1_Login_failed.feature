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

  Scenario Outline: Success login with account <username>
    Given Select language "English"
    When Username "<username>" and password "<password>"
    And Accept EULA is "checked"
    And Click on Login button
    And "Home" button will appear
    Then Logout

    Examples:
      | username     | password    |
      | dpaafx.web92 | TTtest123   |
      | teletrad.95  | 7zvTFDRY    |
      | ivan.coric91 | ICtrader123 |

  Scenario Outline: Expired session with autologin <status>
    Given Open WebStation login page with timeout
    When Username "ican.coric91" and password "ICtrader123"
    And  Stay logged in option is "<status>".
    And Click on Login button
    And "<buttons> button will appear

    Examples:
      | status    | buttons |
      | checked   | Home    |
      | unchecked | Login   |