## Author: Francisco Bumanglag
## Project: INGREDIENT ADJUSTER
## Assignment: Module 1 Project 4
## Course: Python Santa Ana College
## Class: CMPR114 Jason Sim
## Date: June 18, 2023

#CONSTANTS
cookieRecipe = 48
sugarRecipe = 1.5
butterRecipe = 1
flourRecipe = 2.75

#INPUT THE INFORMATION
cookiesNeeded = int(input('Enter the number of cookies you need for the current recipe: '))

#CALCULATIONS
sugarNeeded = (cookiesNeeded / cookieRecipe) * sugarRecipe
butterNeeded = (cookiesNeeded / cookieRecipe) * butterRecipe
flourNeeded = (cookiesNeeded / cookieRecipe) * flourRecipe

#OUTPUT 
print('\n To make' , str(cookiesNeeded) + ' cookies you will needed the following ingredients: \n ')
print('\t\t Sugar:', str(round(sugarNeeded, 2)) + ' cups of sugar')
print('\t\t Butter:', str(round(butterNeeded, 2)) + ' cups of butter')
print('\t\t Flour:' , str(round(flourNeeded, 2)) + ' cups of flour \n')




