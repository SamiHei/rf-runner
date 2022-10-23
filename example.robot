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
    Example Keyword  "First case"

Test case 2
    Example Keyword  "Second case"

Test case 3
    Example Keyword  "Third case"

Test case 4
    Example Keyword  "Fourth case"

