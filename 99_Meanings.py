# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 17:22:01 2022

@author: Ronaldo
"""

# 99 MEANINGS

import os
from random import choice
from PIL import Image, ImageDraw, ImageFont
from datetime import date
import struct
import ctypes

source_dir = r'C:\Users\Ronaldo\OneDrive\Python\Projects\99 Meanings'

Dict_Allah = {1: {"Name": "AR-RAHMAAN", "Meaning": "The Beneficent"},
              2: {"Name": "AR-RAHEEM", "Meaning": "The Merciful"},
              3: {"Name": "AL-MALIK", "Meaning": "The King"},
              4: {"Name": "AL-QUDDUS", "Meaning": "The Most Sacred"},
              5: {"Name": "AS-SALAM", "Meaning": "The Source of Peace, The Flawless"},
              6: {"Name": "AL-MU’MIN", "Meaning": "The Infuser of Faith"},
              7: {"Name": "AL-MUHAYMIN", "Meaning": "The Preserver of Safety"},
              8: {"Name": "AL-AZIZ", "Meaning": "All Mighty"},
              9: {"Name": "AL-JABBAR", "Meaning": "The Compeller, The Restorer"},
              10: {"Name": "AL-MUTAKABBIR", "Meaning": "The Supreme, The Majestic"},
              11: {"Name": "AL-KHAALIQ", "Meaning": "The Creator, The Maker"},
              12: {"Name": "AL-BAARI", "Meaning": "The Evolver"},
              13: {"Name": "AL-MUSAWWIR", "Meaning": "The Fashioner"},
              14: {"Name": "AL-GHAFFAR", "Meaning": "The Great Forgiver"},
              15: {"Name": "AL-QAHHAR", "Meaning": "The All-Prevailing One"},
              16: {"Name": "AL-WAHHAAB", "Meaning": "The Supreme Bestower"},
              17: {"Name": "AR-RAZZAAQ", "Meaning": "The Provider"},
              18: {"Name": "AL-FATTAAH", "Meaning": "The Supreme Solver"},
              19: {"Name": "AL-‘ALEEM", "Meaning": "The All-Knowing"},
              20: {"Name": "AL-QAABID", "Meaning": "The Withholder"},
              21: {"Name": "AL-BAASIT", "Meaning": "The Extender"},
              22: {"Name": "AL-KHAAFIDH", "Meaning": "The Reducer"},
              23: {"Name": "AR-RAAFI’", "Meaning": "The Exalter, The Elevator"},
              24: {"Name": "AL-MU’IZZ", "Meaning": "The Honourer, The Bestower"},
              25: {"Name": "AL-MUZIL", "Meaning": "The Dishonourer, The Humiliator"},
              26: {"Name": "AS-SAMEE’", "Meaning": "The All-Hearing"},
              27: {"Name": "AL-BASEER", "Meaning": "The All-Seeing"},
              28: {"Name": "AL-HAKAM", "Meaning": "The Impartial Judge"},
              29: {"Name": "AL-‘ADL", "Meaning": "The Utterly Just"},
              30: {"Name": "AL-LATEEF", "Meaning": "The Subtle One, The Most Gentle"},
              31: {"Name": "AL-KHABEER", "Meaning": "The All-Aware"},
              32: {"Name": "AL-HALEEM", "Meaning": "The Most Forbearing"},
              33: {"Name": "AL-‘AZEEM", "Meaning": "The Magnificent, The Supreme"},
              34: {"Name": "AL-GHAFOOR", "Meaning": "The Great Forgiver"},
              35: {"Name": "ASH-SHAKOOR", "Meaning": "The Most Appreciative"},
              36: {"Name": "AL-‘ALEE", "Meaning": "The Most High, The Exalted"},
              37: {"Name": "AL-KABEER", "Meaning": "The Most Great"},
              38: {"Name": "AL-HAFEEDH", "Meaning": "The Preserver"},
              39: {"Name": "AL-MUQEET", "Meaning": "The Sustainer"},
              40: {"Name": "AL-HASEEB", "Meaning": "The Reckoner"},
              41: {"Name": "AL-JALEEL", "Meaning": "The Majestic"},
              42: {"Name": "AL-KAREEM", "Meaning": "The Most Generous, The Most Esteemed"},
              43: {"Name": "AR-RAQEEB", "Meaning": "The Watchful"},
              44: {"Name": "AL-MUJEEB", "Meaning": "The Responsive One"},
              45: {"Name": "AL-WAASI’", "Meaning": "The All-Encompassing, the Boundless"},
              46: {"Name": "AL-HAKEEM", "Meaning": "The All-Wise"},
              47: {"Name": "AL-WADUD", "Meaning": "The Most Loving"},
              48: {"Name": "AL-MAJEED", "Meaning": "The Glorious, The Most Honorable"},
              49: {"Name": " AL-BA’ITH", "Meaning": "The Infuser of New Life"},
              50: {"Name": "ASH-SHAHEED", "Meaning": "The All Observing Witnessing"},
              51: {"Name": "AL-HAQQ", "Meaning": "The Absolute Truth"},
              52: {"Name": "AL-WAKEEL", "Meaning": "The Trustee, The Disposer of Affairs"},
              53: {"Name": "AL-QAWIYY", "Meaning": "The All-Strong"},
              54: {"Name": "AL-MATEEN", "Meaning": "The Firm, The Steadfast"},
              55: {"Name": "AL-WALIYY", "Meaning": "The Protecting Associate"},
              56: {"Name": "AL-HAMEED", "Meaning": "The Praiseworthy"},
              57: {"Name": "AL-MUHSEE", "Meaning": "The All-Enumerating, The Counter"},
              58: {"Name": "AL-MUBDI", "Meaning": "The Originator, The Initiator"},
              59: {"Name": "AL-MUEED", "Meaning": "The Restorer, The Reinstater"},
              60: {"Name": "AL-MUHYI", "Meaning": "The Giver of Life"},
              61: {"Name": "AL-MUMEET", "Meaning": "The Creator of Death"},
              62: {"Name": "AL-HAYY", "Meaning": "The Ever-Living"},
              63: {"Name": " AL-QAYYOOM", "Meaning": "The Sustainer, The Self-Subsisting"},
              64: {"Name": "AL-WAAJID", "Meaning": "The Perceiver"},
              65: {"Name": "AL-MAAJID", "Meaning": "The Illustrious, the Magnificent"},
              66: {"Name": "AL-WAAHID", "Meaning": "The One"},
              67: {"Name": "AL-AHAD", "Meaning": "The Unique, The Only One"},
              68: {"Name": "AS-SAMAD", "Meaning": "The Eternal, Satisfier of Needs"},
              69: {"Name": "AL-QADEER", "Meaning": "The Omnipotent One"},
              70: {"Name": "AL-MUQTADIR", "Meaning": "The Powerful"},
              71: {"Name": "AL-MUQADDIM", "Meaning": "The Expediter, The Promoter"},
              72: {"Name": "AL-MU’AKHKHIR", "Meaning": "The Delayer"},
              73: {"Name": "AL-AWWAL", "Meaning": "The First"},
              74: {"Name": "AL-AAKHIR", "Meaning": "The Last"},
              75: {"Name": "AZ-ZAAHIR", "Meaning": "The Manifest"},
              76: {"Name": "AL-BAATIN", "Meaning": "The Hidden One, Knower of the Hidden"},
              77: {"Name": "AL-WAALI", "Meaning": "The Sole Governor"},
              78: {"Name": "AL-MUTA’ALI", "Meaning": "The Self Exalted"},
              79: {"Name": "AL-BARR", "Meaning": "The Source of All Goodness"},
              80: {"Name": "AT-TAWWAB", "Meaning": "The Ever-Pardoning, The Relenting"},
              81: {"Name": "AL-MUNTAQIM", "Meaning": "The Avenger"},
              82: {"Name": "AL-‘AFUWW", "Meaning": "The Pardoner"},
              83: {"Name": "AR-RA’OOF", "Meaning": "The Most Kind"},
              84: {"Name": "MAALIK-UL-MULK", "Meaning": "Master of the Kingdom, Owner of the Dominion"},
              85: {"Name": "DHUL-JALAALI WAL-IKRAAM", "Meaning": "Lord of Glory and Honour, Lord of Majesty and Generosity"},
              86: {"Name": "AL-MUQSIT", "Meaning": "The Just One"},
              87: {"Name": "AL-JAAMI’", "Meaning": "The Gatherer, the Uniter"},
              88: {"Name": "AL-GHANIYY", "Meaning": "The Self-Sufficient, The Wealthy"},
              89: {"Name": "AL-MUGHNI", "Meaning": "The Enricher"},
              90: {"Name": "AL-MANI’", "Meaning": "The Withholder"},
              91: {"Name": "AD-DHARR", "Meaning": "The Distresser"},
              92: {"Name": "AN-NAFI’", "Meaning": "The Propitious, the Benefactor"},
              93: {"Name": "AN-NUR", "Meaning": "The Light, The Illuminator"},
              94: {"Name": "AL-HAADI", "Meaning": "The Guide"},
              95: {"Name": "AL-BADEE'", "Meaning": "The Incomparable Originator"},
              96: {"Name": "AL-BAAQI", "Meaning": "The Everlasting"},
              97: {"Name": "AL-WAARITH", "Meaning": "The Inheritor, The Heir"},
              98: {"Name": "AR-RASHEED", "Meaning": "The Guide, Infallible Teacher"},
              99: {"Name": "AS-SABOOR", "Meaning": "The Forbearing, The Patient"},
              }
Dict_Affirm = {1: "I grow stronger with every mindful breath", 2: "Thank you for all the love in my life",
               3: "Thank you for giving me such a beautiful family", 4: "Thank you for the kindness of strangers",
               5: "I choose to be happy and love myself", 6: "My possibilities are endless", 7: "My thoughts become my reality",
               8: "I am grateful for all that I have", 9: "I will not worry about things I cannot control",
               10: "I know my worth and remind others of theirs", 11: "I am worthy of what I desire",
               12: "A beautiful day begins with a beautiful mindset", 13: "Great things never came from comfort zones",
               14: "I trust I am on the right path", 15: "My mind is full of brilliant ideas", 16: "I can overcome any challenge I face",
               17: "I will focus on what I can control", 18: "I'm well-rested and full of energy", 19: "My energy comes from within",
               20: "I radiate joy and cheerfulness", 21: "I bring happiness to people's lives", 22: "I can be anything I want to be",
               23: "Today I will learn and grow", 24: "I will be fearless today", 25: "Unlimited energy will fill me today",
               26: "I have an abundance of energy", 27: "Today I will change my life", 28: "I will be a better person today",
               29: "I will help someone today", 30: "I'm a magnet for good ideas", 31: "Success will find me today", 32: "Today is full of possibilities",
               33: "The sunrise fills me with confidence", 34: "I choose to be positive", 35: "My intentions and thoughts are powerful",
               36: "I always can find the silver lining", 37: "I am deserving because I am grateful", 38: "I am worthy because I'm a good person",
               39: "The opinion of others doesn't define me", 40: "I am confident in who I am", 41: "I am optimistic for the future",
               42: "Having pure intentions is what counts", 43: "Pain is inevitable but suffering is optional", 44: "My thoughts become things",
               45: "I think therefore I am", 46: "Positive thoughts become positive things", 47: "I have fantastic logic & write brilliant code",
               48: "All I need is within me right now", 49: "I wake up motivated", 50: "I am filled with focus", 51: "Today will be a productive day",
               52: "I feel more grateful every day", 53: "I am getting healthier every day", 54: "I am inspiring people through my work",
               55: "Today is a phenomenal day", 56: "I am powerful", 57:"I am strong", 58: "I am confident", 59: "I am independent and self-sufficient",
               60: "I am healing & strengthening every day", 61: "I finish what matters & let go of what's not", 62: "I have creative energy within",
               63: "I am positive", 64: "I am calm, patient & at peace", 65: "I feed my spirit", 66: "I am adventurous", 67: "I have fun every day",
               68: "I can manage whatever comes up", 69: "I make dreams come true", 70: "I have confidence in myself", 71: "I make every day count",
               72: "I trust myself", 73: "I make every day count", 74: "I make the world a better place", 75: "I like to learn new things",
               76: "I believe in myself", 77: "Today is the best day", 78: "I choose to be in a good mood", 79: "I choose to have a good attitude",
               80: "Gratitude is the best attitude", 81: "I love my life", 82: "I love my work", 83: "I am open to possibilities",
               84: "I believe in my goals", 85: "I keep growing and keep going", 86: "I welcome the unexpected", 87: "My possibilities are endless",
               88: "I have what it takes", 89: "I make my life happy", 90: "I will make my life happen", 91: "I put my heart into everything I do",
               92: "I learn and change every day", 93: "I'm bubbling with energy", 94: "My attitude makes me thrive", 95: "I see a bright future for myself",
               96: "I make a difference", 97: "I am ready for whatever comes", 98: "I can always figure out a solution", 99: "I am thankful for my life"
               }
Dict_Grat = {1: "Life", 2: "Family", 3: "Water", 4: "Kindness", 5: "Nature", 6: "Health", 7: "The Moon",
             8: "The Sun", 9: "Love", 10: "Forgiveness", 11: "The Quran", 12: "Generosity", 13: "Happiness",
             14: "Knowledge", 15: "Wisdom", 16: "Patience", 17: "Altruism", 18: "Food", 19: "Water", 20: "Animals",
             21: "Plants", 22: "Shelter", 23: "Adventure", 24: "Possessions", 25: "Earth", 26: "Technology",
             27: "Ambition", 28: "Laughter", 29: "Vision", 30: "Sound", 31: "Taste", 32: "Goo", 33: "Friendship",
             34: "Hardships", 35: "Smell", 36: "Daytime", 37: "Nighttime", 38: "Sports", 39: "Competition", 40: "Ramadan",
             41: "Warmth", 42: "Cats", 43: "Rain", 44: "Music", 45: "Dance", 46: "Zakat", 47: "Salah", 48: "Coding",
             49: "Unity", 50: "Bees", 51: "Light", 52: "Roads", 53: "Pollen", 54: "Insects", 55: "Feeling", 56: "Sympathy", 57: "Empathy",
             58: "Flowers", 59: "Wealth", 60: "Money", 61: "Trade", 62: "Electricity", 63: "Maths", 64: "Metal", 65: "Chemicals", 
             66: "Chemistry", 67: "Positivity", 68: "Clouds", 69: "Air", 70: "Dates", 71: "Sweetness", 72: "Salt", 73: "Language",
             74: "Coffee", 75: "Spices", 76: "Biology", 77: "Physics", 78: "Herbs", 79: "Time", 80: "Birds", 81: "Flight", 82: "Compassion",
             83: "Education", 84: "Creation", 85: "Sunrise", 86: "Sunset", 87: "Fish", 88: "Entertainment", 89:"Games",
             90: "Faith", 91:"Islam", 92: "Religion", 93: "The Blades", 94: "Support", 95: "Home", 96: "Communication",
             97: "Passion", 98: "Hope", 99: "Justice"
             }

# Lists for the choice functions
names_options = []
affirm_options = []
grat_options = []
image_options = []

for key, value in Dict_Allah.items():  # Collecting Name Keys
    names_options.append(key)
for keys in Dict_Affirm:  # Collecting Affirmation Keys
    affirm_options.append(keys)
for keys in Dict_Grat:  # Collecting Gratitude Keys
    grat_options.append(keys)
for filename in os.listdir(source_dir+"\Images"):  # Collect Image Keys
    if filename.endswith(".png"):
        image_options.append(filename)
    else:
        continue

# Randomly choose key values
name_choice = choice(names_options)
affirm_choice = choice(affirm_options)
image_choice = choice(image_options)
grat_choice = choice(grat_options)
# Create title without file extension
image_title = image_choice.replace('.png', '')

# Print all choices to Console
print(Dict_Allah[name_choice]["Name"])
print(Dict_Affirm[affirm_choice])
print(Dict_Grat[grat_choice])
print(image_choice)

# Function for determining text sizes


def get_text_dimensions(text_string, font):

    ascent, descent = font.getmetrics()

    text_width = font.getmask(text_string).getbbox()[2]
    text_height = font.getmask(text_string).getbbox()[3] + descent

    return (text_width, text_height)


today = date.today()
dateformat = today.strftime("%d/%m/%Y")
datesave = today.strftime("%d-%m")

# Open random image
RandomImage = Image.open(source_dir+'\Images\\'+str(image_choice))
# Write key value onto image
draw = ImageDraw.Draw(RandomImage)
# Locate & choose font format for Header
fontsFolder = 'C:\Windows\Fonts'
# Find centre for using Header on image

image_width, image_height = RandomImage.size
# Create x coordinate adjusted for top left of text box
# Create a header with a fitted background

# Get dimensions for the text to be written in blurb
FontGrat = ImageFont.truetype(os.path.join(fontsFolder, 'arial.ttf'), 23)
grat_width, grat_height = get_text_dimensions(
    "Something to be grateful for: "+Dict_Grat[grat_choice], FontGrat)
FontTrans = ImageFont.truetype(os.path.join(fontsFolder, 'arial.ttf'), 20)
tran_width, tran_height = get_text_dimensions(
    "Translation: "+Dict_Allah[name_choice]["Meaning"], FontTrans)
FontAllah = ImageFont.truetype(os.path.join(fontsFolder, 'arial.ttf'), 23)
name_width, name_height = get_text_dimensions(
    "Names of Allah: "+Dict_Allah[name_choice]["Name"], FontAllah)
FontTitle = ImageFont.truetype(os.path.join(fontsFolder, 'arial.ttf'), 20)
title_width, title_height = get_text_dimensions(
    "Photo: "+image_title, FontTitle)
FontAffirm = ImageFont.truetype(os.path.join(fontsFolder, 'arial.ttf'), 23)
affirm_width, affirm_height = get_text_dimensions(
    Dict_Affirm[affirm_choice], FontAffirm)

# Dimensions for date and info box
FontProj = ImageFont.truetype(os.path.join(fontsFolder, 'arial.ttf'), 22)
proj_width, proj_height = get_text_dimensions(
    "Daily Positivity Generator", FontProj)
FontDate = ImageFont.truetype(os.path.join(fontsFolder, 'arial.ttf'), 19)
date_width, date_height = get_text_dimensions("Todays Date: "+dateformat, FontDate)
FontDisc = ImageFont.truetype(os.path.join(fontsFolder, 'arial.ttf'), 14)
disc_width, disc_height = get_text_dimensions(
    "*This is a randomly generated image", FontDisc)

# Make background for the blurb the total height of all text
blurb_height = grat_height + tran_height + name_height + title_height
# Make widest text the width for the blurbs background
blurb_width = grat_width
if tran_width > blurb_width:
    blurb_width = tran_width
if name_width > blurb_width:
    blurb_width = name_width
if title_width > blurb_width:
    blurb_width = title_width
if affirm_width > blurb_width:
    blurb_width = affirm_width

# Draw backgrounds for the blurb
draw.rectangle((image_width-blurb_width-10, image_height-blurb_height-6,
               image_width+blurb_width, image_height+blurb_height), (105, 209, 197))
draw.rectangle((image_width-blurb_width-10, image_height-blurb_height-affirm_height -
               6, image_width+blurb_width, image_height-blurb_height-5), (23, 42, 58))

# Drawing Text for the blurb
draw.text((image_width-blurb_width-5, image_height-grat_height),
          "Something to be grateful for: "+Dict_Grat[grat_choice], (23, 42, 58), font=FontGrat)
draw.text((image_width-blurb_width-5, image_height-grat_height-tran_height),
          "Translation: "+(Dict_Allah[name_choice]["Meaning"]), (23, 42, 58), font=FontTrans)
draw.text((image_width-blurb_width-5, image_height-grat_height-tran_height-name_height-3),
          "Names of Allah: "+(Dict_Allah[name_choice]["Name"]), (23, 42, 58), font=FontAllah)
draw.text((image_width-blurb_width-5, image_height-blurb_height-4),
          "Photo: "+image_title, (23, 42, 58), font=FontTitle)

# Drawing Text for the header of the blurb
affirm_xcoord = image_width-(((blurb_width+10)/2)+(affirm_width/2))
draw.text((affirm_xcoord, image_height-blurb_height-affirm_height-6),
          Dict_Affirm[affirm_choice], (105, 209, 197), font=FontAffirm)

# Draw background for date and info box
draw.rectangle((0, 0, proj_width+10, proj_height+date_height+5), (23, 42, 58))
draw.rectangle((0, proj_height+date_height+5, proj_width+10,
               proj_height+date_height+disc_height+5), (105, 209, 197))

# Draw text for date and info box
draw.text((5, 5), "Daily Positivity Generator", (105, 209, 197), font=FontProj)
draw.text((5, 5+proj_height), "Todays Date: " +
          dateformat, (105, 209, 197), font=FontDate)
draw.text((5, 5+proj_height+date_height),
          "*This is a randomly generated image", (23, 42, 58), font=FontDisc)

# Load Logo infront of a rectangle background
LogoIm = Image.open(source_dir+'\ResizedLogo.png')
Logo_Width, Logo_Height = LogoIm.size
draw.ellipse((15, 935, 145, 1065), ("black"))
# draw.rectangle((0, image_height-Logo_Height-10, Logo_Width+10, image_height), ("black"))
RandomImage.paste(LogoIm, (9, image_height-124), LogoIm)
# Save changes.
RandomImage.save(source_dir+'\Images\Output\\'+datesave+'.png')

# Get Quotes for Desktop Image
Dict_Quote = {}
quote_lists = []
quote_options = []

# This creates a list of quotes and authors
a_file = open(source_dir+"\Quotes.txt", "r")
for line in a_file:
    stripped_line = line.strip("\n- ")
    quote_lists.append(stripped_line)
a_file.close()

# Puts quotes and author from list into a dictionary
n = len(quote_lists)
for i in range(0, n, 2):
    Dict_Quote[quote_lists[i]] = quote_lists[i+1]

# Create options for the quote
for key, value in Dict_Quote.items():
    quote_options.append(key)

# Randomly choose a quote
quote_choice = choice(quote_options)
print(quote_choice)


OriginalIm = Image.open(source_dir+'\Images\Output\\'+datesave+'.png')
original_width, original_height = OriginalIm.size
FittedIm = OriginalIm.resize(
    (int(original_width - 60), int(original_height - 60)))
FittedIm.save(source_dir+'\Background\Fitted.png')

BackgroundImage = Image.open(
    source_dir+'\Background\Desktop Background.png')
draw = ImageDraw.Draw(BackgroundImage)
if len(quote_choice) < 40:
    FontQuote = ImageFont.truetype(
        os.path.join(fontsFolder, 'arial.ttf'), 22)
elif 50 > len(quote_choice) < 40:
    FontQuote = ImageFont.truetype(
        os.path.join(fontsFolder, 'arial.ttf'), 17)
else:
    FontQuote = ImageFont.truetype(
        os.path.join(fontsFolder, 'arial.ttf'), 15)

quote_width, quote_height = get_text_dimensions(
    quote_choice, FontQuote)
draw.text((1700-(quote_width/2), 915),
          quote_choice, (105, 209, 197), font=FontQuote)
author_width, author_height = get_text_dimensions(Dict_Quote[quote_choice], FontQuote)
draw.text((1700-(author_width/2), 950), Dict_Quote[quote_choice],
          (105, 209, 197), font=FontQuote)

# Function to countdown days for deadline
def numOfDays(date1, date2):
    return (date2-date1).days

# Determine the objectives deadlines
present = date.today()
deadline1 = date(2022, 10, 25)
deadline2 = date(2022, 10, 16)
deadline3 = date(2022, 10, 11)
deadline4 = date(2022, 10, 14)

# Concantenate the number of days left
Obj1_Deadline = (str(numOfDays(present, deadline1))+" days")
Obj2_Deadline = (str(numOfDays(present, deadline2))+" days")
Obj3_Deadline = (str(numOfDays(present, deadline3))+" days")
Obj4_Deadline = (str(numOfDays(present, deadline3))+" days")

# Font size for the Objectives
FontObj = ImageFont.truetype(
os.path.join(fontsFolder, 'arial.ttf'), 25)
spacing = 55

# Draw the objectives on the background
obj_width, obj_height = get_text_dimensions(
        "Python Course: "+Obj1_Deadline, FontObj)
draw.text((1700-(obj_width/2), 555), "Python Course: "+Obj1_Deadline,
              (105, 209, 197), font=FontObj)

obj_width, obj_height = get_text_dimensions(
        "Complete CV: "+Obj2_Deadline, FontObj)
draw.text((1700-(obj_width/2), 555+spacing), "Complete CV: "+Obj2_Deadline,
              (105, 209, 197), font=FontObj)

obj_width, obj_height = get_text_dimensions(
        "Milestone Cap Proj: "+Obj3_Deadline, FontObj)
draw.text((1700-(obj_width/2), 555+(2*spacing)), "Milestone Cap Proj: "+Obj3_Deadline,
              (105, 209, 197), font=FontObj)

obj_width, obj_height = get_text_dimensions(
        "Plan Nov Trip: "+Obj4_Deadline, FontObj)
draw.text((1700-(obj_width/2), 555+(3*spacing)), "Plan Nov Trip: "+Obj4_Deadline,
              (105, 209, 197), font=FontObj)

Background_Width, Background_Height = BackgroundImage.size
ChosenIm = Image.open(source_dir+'\Background\Fitted.png')
Chosen_Width, Chosen_Height = ChosenIm.size
BackgroundImage.paste(
        ChosenIm, ((Background_Width//2)-(Chosen_Width//2), (0)))
BackgroundImage.save(source_dir+'\Background\Output\Background.png')


SPI_SETDESKWALLPAPER = 20
WALLPAPER_PATH = r'C:\Users\Ronaldo\OneDrive\Python\Projects\99 Meanings\Background\Output\Background.png'


def is_64_windows():
    """Find out how many bits is OS. """
    return struct.calcsize('P') * 8 == 64


def get_sys_parameters_info():
    """Based on if this is 32bit or 64bit returns correct version of SystemParametersInfo function. """
    return ctypes.windll.user32.SystemParametersInfoW if is_64_windows() \
        else ctypes.windll.user32.SystemParametersInfoA


def change_wallpaper():
    sys_parameters_info = get_sys_parameters_info()
    r = sys_parameters_info(SPI_SETDESKWALLPAPER, 0, WALLPAPER_PATH, 3)

    # When the SPI_SETDESKWALLPAPER flag is used,
    # SystemParametersInfo returns TRUE
    # unless there is an error (like when the specified file doesn't exist).
    if not r:
        print(ctypes.WinError())


change_wallpaper()

# TO DO: Email the Output
# TO DO:
