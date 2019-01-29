#Create tool to ingest a shopping list, and produce an organized/optimized shopping list based on layout of store
##STEPS##
#1)Create dictionaries for items (produce, meat, etc)
#	eg - groceries = {
#			"dairy": ('milk','butter','eggs','sour cream','sliced cheese'),
#			"meat": ('ribeye','chicken thigh', 'chicken breast')
#			"water": ('seltzer','')
#}
#2)Set of Dictionaries (?) to store preferred path in a grocery store (Fresh Veg/Fruit -> Baked Goods -> Meat -> Dairy -> dry goods, etc)
#3)Read in CSV of grocery list
#4)Compare list to stored dictionaries, if product is new to "Dairy" then add it.
#4)Have user select store
#5)Create ordered list of grocery section layout depending on preferred store - Wegmans v. Food Lion v. LIDL v. Giant
#6)Export out as CSV or create a 'task list' that user can tick off items from (if digital preferred)

#python 3

import os,csv,glob
import pandas as pd

def main():
	print("Welcome to the Grocery List organizer. Because you too can be this anal. \nSelect the store you plan to shop:")
	store = selectStore()
	print("Select Grocery List:")
	groceryList = getList(inputDirectory)
	organizeList(store)
	print("Thank you for playing. Your organized list in saved in ./sortedGroceryList")

#Helper Functions -- Need to revisit.
# def foodLists():
# 	groceries = {
# 		"dairy": ('milk', 'butter','eggs','sour cream', 'sliced cheese'),
# 		"meat": ('ribeye','chicken thighs','chicken breasts','ground turkey','ground beef','porkchops'),
# 		"drinks": ('beer','seltzer','red wine','white wine','soda','champagne'),
# 		"dry goods": ('cereal','dog food','ziploc bags','canned soup','canned beans','beans')
# 		"baked goods": ('bread','bagels','muffins')
# 		"frozen foods": ('fish sticks','ice cream','pizza','lean cuisine')
# 		"household": ('detergent','dryer sheets','bleach','')}

	return groceries

def selectStore():
	#Ask user for raw input on which store they want; eg: Wegmans, Food Lion, LIDL
	storeMenu = """
	0. Exit
	1. LIDL
	2. Wegmans
	3. Food Lion"""

	print(storeMenu)
#	getNonNegInt("Store Selection:")

def storeOrder(store):
	grocerySections = {1:"Dairy", 2:"Meat",3:"Produce",4:"Dry Goods",5:"Drinks",6:"Baked Goods",7:"Frozen Foods",8:"Household"}
	#GroceryStore Orders....
	groceries = {
		"dairy": ('milk', 'butter','eggs','sour cream', 'sliced cheese','shredded cheese'),
		"meat": ('ribeye','chicken thighs','chicken breasts','ground turkey','ground beef','porkchops'),
		"drinks": ('beer','seltzer','red wine','white wine','soda','champagne'),
		"dry goods": ('cereal','dog food','ziploc bags','canned soup','canned beans','beans'),
		"baked goods": ('bread','bagels','muffins','cinnamon rolls'),
		"frozen foods": ('fish sticks','ice cream','pizza','lean cuisine'),
		"household": ('detergent','dryer sheets','bleach')}

	LIDL = [6,3,2,1,7,4,5,8]
	Wegmans = [3,6,2,1,7,4,5,8]
	FoodLion = [3,7,4,2,5,8,1,6]

	return groceries,storeOrder

def getList(directory):
	grocery_list = glob.glob(directory)
	for i in range(len(grocery_list)):
		print i, ":", grocery_list[i]
	while True:
		try:
			grocery_list_sel = int(raw_input('Select your grocery list: '))
		except ValueError:
			continue
		if (int(grocery_list_sel) >= 0) and (int(grocery_list_sel) < len(grocery_list)):
			break
	return grocery_list[grocery_list_sel]

def organizeList(groceries,groceryStore,storeOrder,groceryList):
	#Open
	for i in range(len(storeOrder)):
		#sortedGroceryList.append(storeOrder[i])
		for j in groceryList:
			if dict[j] == storeOrder[i]:
				sortedGroceryList.append(groceryList[i])
	#loop to get stuff that doesn't fall in the grocery sections
	for i in range(len(groceryList)):
		if groceryList[i] not in sortedGroceryList:
			sortedGroceryList.append(groceryList[i])


def getNonNegInt(prompt):
    value = 0
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            continue
        if value >= 0:
            break
    return value

inputDirectory = './grocerylists/*'
outputDirectory = './sortedGroceryList'
