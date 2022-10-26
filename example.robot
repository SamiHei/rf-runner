*** Settings ***
Library      Collections


*** Variables ***
${EXAMPLE}=   "Just an example"


*** Keywords ***
Example Keyword
    [Arguments]  ${text}
    Log To Console  ${text}


*** Test Cases ***
Test case 1
    Example Keyword  "Case number 1."

Test case 2
    Example Keyword  "Case number 2."

Test case 3
    Example Keyword  "Case number 3."

Test case 4
    Example Keyword  "Case number 4."

Test case 5
    Example Keyword  "Case number 5."

Test case 6
    Example Keyword  "Case number 6."

Test case 7
    Example Keyword  "Case number 7."

Test case 8
    Example Keyword  "Case number 8."

Test case 9
    Example Keyword  "Case number 9."
