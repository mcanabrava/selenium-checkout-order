# selenium-scripts
This repository was initially focused on experimenting with Selenium basic functionalities to log in to a [demo website](https://www.saucedemo.com/), add an item to the cart, and check out while using Google Chrome.

It was a super easy task. The most challenging part was dealing with the dependencies between Selenium and Chrome versions and related issues, so I created a few more Selenium scripts.

I have also added time.sleep between actions so it's possible to visualize Selenium doing its work on the recordings.

## saucedemo.py
This is the original script for the test selenium marketplace website.

https://github.com/mcanabrava/selenium-scripts/assets/54443088/6b985a04-78c3-45f8-9a13-28070ba90e0e

## amazon.py
After the first challenge, I decided to test my new skills on an actual website like Amazon.com. The script basically:

1. searches for a product
2. reads all the prices for that product on the first page
3. clicks on the cheapest product that fills the name criteria and has a price above a configurable threshold (to avoid scams or related accessories)
4. adds the product to the cart and exit before the log-in, as we don't really want to purchase anything
  
The script tries to dodge modals, but it's not always successful as they might appear in different ways.

https://github.com/mcanabrava/selenium-scripts/assets/54443088/6ecc2937-c359-4932-aafd-cb31c4d3b0cc
