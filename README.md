# selenium-scripts
This repository was initially focused on experimenting with Selenium basic functionalities to log-in into a [demo website](https://www.saucedemo.com/), add an item to the cart and check out while using Google Chrome.

It was a super easy task and the most challenging part was to deal with the dependencies between selenium and chrome versions and related issues, so I decided to create a few more selenium scripts.

## saucedemo.py
This is the original script for the test selenium marketplace website.

## amazon.py
I decided to test my new skills in a real website, such as Amazon.com. The script basically searches for a product the owner of the script can configure, and then reads all the product prices for that product on the search. It will then click on the most cheap product that fills the name criteria and has a price above a configurable threshold (to avoid scam or related accessories). It will then add the product to cart and exit before the log-in, as we don't really want to purchase anything. The script tries to dodge from modals, but it's not always successful as they might appear in different places and timings.

