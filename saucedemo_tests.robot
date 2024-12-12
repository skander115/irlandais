*** Settings ***
Library           SeleniumLibrary

*** Variables ***
${URL}            https://www.saucedemo.com/
${VALID_USER}     standard_user
${VALID_PASS}     secret_sauce
${LOCKED_USER}    locked_out_user

*** Test Cases ***
Login Validation
    [Documentation]    Verify valid and invalid login scenarios
    Open Browser    ${URL}    Chrome
    Input Text    id:user-name    ${VALID_USER}
    Input Text    id:password    ${VALID_PASS}
    Click Button    id:login-button
    Location Should Contain    inventory.html
    [Teardown]    Close Browser

    Open Browser    ${URL}    Chrome
    Input Text    id:user-name    ${LOCKED_USER}
    Input Text    id:password    ${VALID_PASS}
    Click Button    id:login-button
    Element Text Should Be    css:h3[data-test='error']    Epic sadface: Sorry, this user has been locked out.
    [Teardown]    Close Browser

Remove From Cart
    [Documentation]    Ensure items cannot be removed from the cart due to a potential bug
    Open Browser    ${URL}    Chrome
    Input Text    id:user-name    ${VALID_USER}
    Input Text    id:password    ${VALID_PASS}
    Click Button    id:login-button
    Click Button    css:button[name*='add-to-cart']
    Click Link    class:shopping_cart_link
    ${REMOVE_BUTTON}=    Get WebElement    css:button[name*='remove']
    Click Element    ${REMOVE_BUTTON}
    ${IS_REMOVED}=    Run Keyword And Return Status    Element Should Not Exist    css:button[name*='remove']
    Should Be True    ${IS_REMOVED}
    [Teardown]    Close Browser

Checkout Form Validation
    [Documentation]    Verify checkout form behavior
    Open Browser    ${URL}    Chrome
    Input Text    id:user-name    ${VALID_USER}
    Input Text    id:password    ${VALID_PASS}
    Click Button    id:login-button
    Click Button    css:button[name*='add-to-cart']
    Click Link    class:shopping_cart_link
    Click Button    id:checkout
    Input Text    id:first-name    John
    Input Text    id:postal-code    12345
    Click Button    id:continue
    Location Should Not Contain    checkout-step-two.html
    [Teardown]    Close Browser

Image Loading Validation
    [Documentation]    Verify product images load correctly
    Open Browser    ${URL}    Chrome
    Input Text    id:user-name    ${VALID_USER}
    Input Text    id:password    ${VALID_PASS}
    Click Button    id:login-button
    ${IMAGES}=    Get WebElements    tag:img
    ${ALL_LOADED}=    Evaluate    all(img.get_attribute('src') for img in ${IMAGES})
    Should Be True    ${ALL_LOADED}
    [Teardown]    Close Browser

Checkout Button with Empty Cart
    [Documentation]    Verify the checkout button is disabled with an empty cart
    Open Browser    ${URL}    Chrome
    Input Text    id:user-name    ${VALID_USER}
    Input Text    id:password    ${VALID_PASS}
    Click Button    id:login-button
    Click Link    class:shopping_cart_link
    ${IS_ENABLED}=    Run Keyword And Return Status    Element Should Be Enabled    id:checkout
    Should Be False    ${IS_ENABLED}
    [Teardown]    Close Browser

Sorting Functionality
    [Documentation]    Verify sorting by price (low to high)
    Open Browser    ${URL}    Chrome
    Input Text    id:user-name    ${VALID_USER}
    Input Text    id:password    ${VALID_PASS}
    Click Button    id:login-button
    Select From List By Value    class:product_sort_container    lohi
    ${PRICES}=    Get WebElements    class:inventory_item_price
    ${PRICE_VALUES}=    Create List
    :FOR    ${PRICE}    IN    @{PRICES}
    \    ${VALUE}=    Replace String    ${PRICE.text}    $    
    \    Append To List    ${PRICE_VALUES}    ${VALUE}
    ${SORTED}=    Evaluate    sorted(${PRICE_VALUES}) == ${PRICE_VALUES}
    Should Be True    ${SORTED}
    [Teardown]    Close Browser
