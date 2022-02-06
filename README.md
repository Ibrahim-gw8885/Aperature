# Aperature
### Our hack makes sure that yummy and rich food you have around the house will never spoil. Our hack allows you to keep track of your food in your fridge or your pantry, warning you if some food is close to expiring,when some food has expired already, and what food is a long ways from expiring.
## Made by 
#### - Ibrahim Hussaini(person5)
#### - Theshazaminator
#### - dnote

# Overview
## Approach
### We started by brainstorming the components of our hack, and what we would need to do to learn to complete the project. 
### Language
#### We started with what language we were going to use, that being python since all of our members knew a little bit of python and one member was new to coding, so we decided python would be best since its simple to code in. 
### Problems and solutions
#### Next we had to plan how we would store the data of the expiration date and what food everyone had, for that we employed pandas and the csv modules that python provides to write and read from csv files where we would store our data. The data we used is test data we made ourselves, it works with the formal of [name,month,day,year]
#### Then we had to decide how we would display this data, using a shell wouldnt be optimal since listing all the data can be complex and convoluted, and just using a shell wouldnt let people know important info without it having to be in the format of a csv or excel format. We decided to use tkinter to make our gui to let the user interact easily and see thier foods eand results easily as well.
## Outcomes
#### We were able to let the use be able to add food into the program, let them see all of the food they have, and let them delete stuff all within the program, creating a easy to use ui for our hack

# Navigation
## core files
#### - main.py
#### - fridge.csv
## other files for reference
#### - modules, used for testing functions outside of the gui
#### - fridge2.0.csv - more examples
#### - fridgePic.png - unused "reference" pic
