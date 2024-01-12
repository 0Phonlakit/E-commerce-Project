*** Settings ***
Library             SeleniumLibrary

*** Variables ***
${browser}          chrome
${shop_url}         http://127.0.0.1:8000/
${username}         tester
${password}         1234
${contact_num}      0123456789
${address}          House No.- Apt- Bldg- Village- Alley- Road- District- Province- Postal Code-

*** Test Cases ***
Open Browser with GUI and Logging
    Open Browser  ${shop_url}  ${browser}  options=add_argument("--disable-gpu --enable-logging --v=1")
    Execute JavaScript  document.querySelector("a.btn-2").click();
    Wait Until Element Is Visible  //*[@id="content2-2"]/div/div[1]/h4

    Execute JavaScript  document.querySelector("#navbarSupportedContent ul li:nth-child(4) a").click();
    Execute JavaScript  document.querySelector("#navbarSupportedContent ul li:nth-child(4) div a:nth-child(2)").click();

    Execute JavaScript  document.querySelector("#form7-q div div:nth-child(2) form div div:nth-child(1) input").value = "${username}"
    Execute JavaScript  document.querySelector("#form7-q div div:nth-child(2) form div div:nth-child(2) input").value = "${password}"

    Execute JavaScript  document.querySelector("#form7-q div div:nth-child(2) form div div:nth-child(3) button").click()
    Execute JavaScript  document.querySelector("#navbarSupportedContent ul li:nth-child(2) a").click();

    Execute JavaScript  document.evaluate('//*[@id="content2-2"]/div/div[2]/div[3]/div/div[1]/a', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue.click()
    Capture Page Screenshot  
    
    Execute JavaScript  document.evaluate('/html/body/div/div/div/div[2]/div/div[2]/a', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue.click()
    Capture Page Screenshot
    
    Execute JavaScript  document.evaluate('/html/body/section[3]/div/div/div/div/div/div/div[2]/div/a/button', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue.click()
    Execute JavaScript  document.querySelector("#content2-2 > div > div > div.row > form > div:nth-child(2) > div > input").value = "${contact_num}"
    Execute JavaScript  document.querySelector("#content2-2 > div > div > div.row > form > div:nth-child(3) > div > input").value = "${address}"
    Capture Page Screenshot
    Execute JavaScript  document.querySelector("#content2-2 > div > div > div.col-auto.mbr-section-btn.align-center > button").click()
    Capture Page Screenshot

    Close Browser
