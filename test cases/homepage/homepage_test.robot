*** Settings ***
Library             SeleniumLibrary

*** Variables ***
${browser}          chrome
${shop_url}         http://127.0.0.1:8000/

*** Test Cases ***
Open Browser with GUI and Logging
    Open Browser  ${shop_url}  ${browser}  options=add_argument("--disable-gpu --enable-logging --v=1")
    Execute JavaScript  document.querySelector("a.btn-2").click();
    Wait Until Element Is Visible  //*[@id="content2-2"]/div/div[1]/h4
    Capture Page Screenshot
    Close Browser
