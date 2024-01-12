*** Settings ***
Library             SeleniumLibrary

*** Variables ***
${browser}          chrome
${shop_url}         http://127.0.0.1:8000/
${username}         tester
${password}         1234

*** Test Cases ***
Open Browser with GUI and Logging
    Open Browser  ${shop_url}  ${browser}  options=add_argument("--disable-gpu --enable-logging --v=1")
    Execute JavaScript  document.querySelector("a.btn-2").click();
    Wait Until Element Is Visible  //*[@id="content2-2"]/div/div[1]/h4

    Execute JavaScript  document.querySelector("#navbarSupportedContent ul li:nth-child(4) a").click();
    Capture Page Screenshot
    Execute JavaScript  document.querySelector("#navbarSupportedContent ul li:nth-child(4) div a:nth-child(2)").click();

    Execute JavaScript  document.querySelector("#form7-q div div:nth-child(2) form div div:nth-child(1) input").value = "${username}"
    Execute JavaScript  document.querySelector("#form7-q div div:nth-child(2) form div div:nth-child(2) input").value = "${password}"
    Capture Page Screenshot
    Execute JavaScript  document.querySelector("#form7-q div div:nth-child(2) form div div:nth-child(3) button").click()
    Execute JavaScript  document.querySelector("#navbarSupportedContent ul li:nth-child(2) a").click();
    Execute JavaScript  document.querySelector("#navbarSupportedContent ul li:nth-child(4) a").click();
    Wait Until Element Is Visible  //*[@id="navbarSupportedContent"]/ul/li[4]/a
    Capture Page Screenshot
    Close Browser
