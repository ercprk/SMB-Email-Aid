#!/usr/bin/python3

import os
import nltk
import re
import html

def sanitize(text):

    nltk.download('punkt')
    split_data = nltk.tokenize.sent_tokenize(text)

    text = ""

    for i in range(len(split_data)):
        phrase = split_data[i].strip()
        phrase = re.sub(r'[^\x00-\x7F]+',' ', phrase)
        phrase = ' '.join(phrase.split())

        if contain_junk(phrase):
            pass
        else:
            phrase = html.unescape(phrase)
            print(f"{phrase}\n")
            text = text + phrase + " "

    return text

def contain_junk(text):
    words = ["COVID", "Jazzberry", "yazzberryyam@gmail.com", "click", "Click",
             "All Rights", "Ruby", "Text", "April", "@", "Update", "link",
             "yazzberryyam", "CONFIRM", "Rewards", "rewards", "point", "www.",
             "$", "ONLINE", "email", "Email", ".com", "promo", "member",
             "February", "January", "March", "ORDER", "order", "Offer",
             "Facebook", "Twitter", "Pinterest", "Instagram", "logo", "offer",
             "reward", "FREE", "Free", "Delivery", "%", "safety", "corona",
             "Image", "delivery", "LOCATION", "Location", "location", "Problem",
             "Buca", "Contact", "online", "Circus", "circus", "Spotify", "IHOP",
             "Copyright", "virtual", "Moe", "FACEBOOK", "TWITTER",
             "INSTAGRAM", "difficult", "no-contact", "browser", "Carl", "OREO",
             "Promo", "Olive Garden", "Kentucky", "Tuesday", "KFC", "DoorDash",
             "HOOTERS", "Hooters", "Steakhouse", "BOGO", "Bahama", "Birthday",
             "WEDNESDAY", "Sbarro", "FEBRUARY", "Grubhub", "7-Eleven",
             "Bertucci", "Cheesecake", "SALE", "Auntie", "Taco Bell",
             "Firehouse", "Fuddruckers", "Wingstop", "charged", "transaction",
             "Scan", "Popeyes", "Privacy", "newsletter", "Dave Jensen",
             "Seasons", "Everett", "Roadhouse", "VERIFY", "MERCH", "eClub",
             "Sonic", "Carvel", "Below", "Eddie", "Valentine", "Reserve",
             "Molasses", "LongHorn", "Little Caesars", "test", "e-Club",
             "expire", "MONDAY", "monday", "3/8", "Tomorrow", "Wednesday",
             "PM", "LLC", "Pi", "Order", "RESERVATION", "UNO", "Online",
             "Cater", "crisis", "DELIVERY", "reserved", "3/6", "subscription",
             "join", "Shake", "coupon", "BLIZZARD", "1/3", "SEASONS",
             "Boneless", "Dickason", "Caffeinated", "Prosecutor", "POINTS",
             "Arby", "Mardi Gras", "Patrick", "Monday", "BurgerFi",
             "RedCoffee", "Sweetgreen", "*", "Download", "BOU", "linguini",
             "shrimp", "Redeem", "discount", "swag", "HOMEWRECKER", "Today",
             "Sunday", "11pm", "3 Cheeses", "Slice", "TUESDAY", "Capital",
             "1 priority", "Baja", "Coronavirus", "National", "Impossible",
             "sub", "steaks", "Creations", "plant-based", "Pretzel", "jazz",
             "Bou-rritos", "message", "Chicken", "Ethiopian", "Smoothies",
             "NATIONAL", "Rita", "Manage", "Wormtown", "Discount", "Salmon",
             "activity", "beef", "Cookie", "pancakes", "meats", "steakhouse",
             "Deep Dish", "unused", "Awkward", "Curbside", "curbside",
             "drive-thru", "Patty", "burger", "salsa", "salmon", "soup",
             "Cake", "vegan", "dairy", "queso", "Reuben", "Cone", "Dine-in",
             "MIDWEEK", "slices", "nuts", "churros", "lobster", "Burger",
             "coffee", "smoothie", "garlic", "beer", "cats", "cream",
             "Sandwiches", "uncertain", "crazy", "deliver", "Scoop", "Grill",
             "Buy a drink", "1950", "photo of your ex", "Leap Year", "code",
             "Available All Day!", "XL", "Dine-In only", "Open now to see",
             "grill", "Saturday", "temporarily", "time at home", "ToGo",
             "No contact", "No wait", "No lines", "Teaching", "Parenting",
             "andWhat", "andOr", "awkward", "challenges", "responders", 
             "carryout", "birthday", "Great American", "1.", "Chirp",
             "STAY-AT-HOME", "BURGERS", "Takeout", "Beer", "GreatSweet",
             "springtime", "7-oz", "To-Go", "Postmates", "Easter", "Lobster",
             "Learning at home", "Buy 8", "Buy 16", "Bacon", "Sleep",
             "leaving", "weekdays", "CATER", "Signature", "PRIZE", "Convenient",
             "contactless", "safely", "Expiration", "BONUS", "New users",
             "appetizer", "Congratulations", "signed in", "lSee", "heaters",
             "let the NEW", "prizes", "HiAnd", "See ya soon", "See you there!",
             "CHECKING IN", "Deliciouso", "You betcha", "Done.", 
             "in this together", "Stay home", "CallLet", "Smokey Bones",
             "We are Open", "hoppy", "literally", "at home", "egg hunt",
             "New.", "To Go.", "again soon", "next event", "Hop Out", "handle",
             "HANDLE", "CHEF", "rapidly", "limited", "girls", "tLike", "newAnd",
             "cluttered", "tWelcome", "Enter now", "tap", "toCheck", "emoji"]

    for word in words:
        if word in text:
            return True

def main():

    # Filepaths
    original_filename = "unsanitized_data.txt"
    sanitized_filename = "sanitized_data.txt"

    # Read unsanitized, original data
    original_file = open(original_filename)
    try:
        text = original_file.read()
    finally:
        original_file.close()

    # Sanitize
    text = sanitize(text)

    # Write the result
    try:
        sanitized_file = open(sanitized_filename, "w")
        sanitized_file.write(text)
    finally:
        sanitized_file.close()

if __name__ == '__main__':
    main()
