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

# put unorganized grocery list in order:
# put item into category bucket
# return buckets in preferred order want to navigate the store

#python 3


import os,csv,glob
###HELPER DICT AND LISTS###
INPUT_DIRECTORY = '.\grocerylists\*'
OUTPUT_DIRECTORY = '.\sortedGroceryList'

GROCERY_SECTIONS = {1:"Dairy", 2:"Meat",3:"Produce",4:"Dry Goods",5:"Drinks",6:"Baked Goods",7:"Frozen Foods",8:"Household",9:"Misc"}
DAIRY=['milk', 'butter','eggs','sour cream', 'sliced cheese','shredded cheese']
MEAT=['ribeye','chicken thighs','chicken breasts','ground turkey','ground beef','porkchops']
DRINKS=['beer','seltzer','red wine','white wine','soda','champagne']
DRY_GOODS=['cereal','dog food','ziploc bags','canned soup','canned beans','beans']
BAKED_GOODS=['bread','bagels','muffins','cinnamon rolls']
FROZEN_FOODS=['fish sticks','ice cream','pizza','lean cuisine']
HOUSEHOLD=['detergent','dryer sheets','bleach']


def main():
	print("Welcome to the Grocery List organizer. Because you too can be this anal. \nSelect the store you plan to shop:")
	store = selectStore()
	print("Select Grocery List:")
	groceryList = getList(INPUT_DIRECTORY)
	sorted_list = organizeList(groceryList)
	Store_Order = Get_Store_Order(store)
	Organized_List = order_sections(sorted_list,Store_Order)
	WriteCSV(Organized_List,store)
	print("Thank you for playing. Your organized list in saved in ./sortedGroceryList")


def getList(directory):
	csv_input = glob.glob(directory)
	file_names =[]

	for i in (csv_input):
		splitlist = i.split("\\")
		file_names.append(splitlist[-1])

	for i in range(len(file_names)):
		print (i, ":", file_names[i])
	while True:
		try:
			csv_input_sel = int(input('Select Grocery List: '))
		except ValueError:
			continue
		if (int(csv_input_sel) >= 0) and (int(csv_input_sel) < len(csv_input)):
			break

	return csv_input[csv_input_sel]

def selectStore():
	#Ask user for raw input on which store they want; eg: Wegmans, Food Lion, LIDL
	storeMenu = """
	0. Exit
	1. LIDL
	2. Wegmans
	3. Food Lion\n\nSelection:"""

	store_num = getNonNegInt(storeMenu,3)
	if store_num == 0:
		exit()
	return store_num


def Get_Store_Order(store_number):
	LIDL = [6,3,2,1,7,4,5,8]
	Wegmans = [3,6,2,1,7,4,5,8]
	FoodLion = [3,7,4,2,5,8,1,6]

	if store_number == 1:
		return LIDL
	elif store_number == 2:
		return Wegmans
	else:
		return FoodLion


def organizeList(GroceryCSV):
	unsorted_list=[]
	All_Sections = {"Dairy":[],"Meat":[],"Produce":[],"Dry Goods":[],"Drinks":[],"Baked Goods":[],"Frozen Foods":[],"Household":[],"Misc":[]}
	with open(GroceryCSV,"r") as f:
		for row in f.readlines():
			row = row.strip("\n")
			unsorted_list.append(row)
	f.close()

	for i in range(len(unsorted_list)):
		if unsorted_list[i] in DAIRY:
			All_Sections["Dairy"].append(unsorted_list[i])
		elif unsorted_list[i] in MEAT:
			All_Sections["Meat"].append(unsorted_list[i])
		elif unsorted_list[i] in DRINKS:
			All_Sections["Drinks"].append(unsorted_list[i])
		elif unsorted_list[i] in DRY_GOODS:
			All_Sections["Dry Goods"].append(unsorted_list[i])
		elif unsorted_list[i] in BAKED_GOODS:
			All_Sections["Baked Goods"].append(unsorted_list[i])
		elif unsorted_list[i] in FROZEN_FOODS:
			All_Sections["Frozen Foods"].append(unsorted_list[i])
		elif unsorted_list[i] in HOUSEHOLD:
			All_Sections["Household"].append(unsorted_list[i])
		else:
			All_Sections["Misc"].append(unsorted_list[i])

	return All_Sections


def order_sections(All_Sections,store_order):
	sorted_list=[]
	for i in range(len(store_order)):
		current_bucket = All_Sections[GROCERY_SECTIONS[store_order[i]]]
		sorted_list.append(GROCERY_SECTIONS[store_order[i]])
		for j in current_bucket:
			sorted_list.append(j)
		sorted_list.append("")

	return sorted_list


def WriteCSV(sorted_list,store_number):
	store_name=""
	if store_number == 1:
		store_name = 'LIDL'
	elif store_number == 2:
		store_name = 'Wegmans'
	else:
		store_name = 'FoodLion'

	with open(OUTPUT_DIRECTORY+"/"+store_name+"_List.csv","a") as fl:
		wr=csv.writer(fl)
		for i in sorted_list:
			fl.write(i+"\n")
	fl.close()


def getNonNegInt(prompt,max):
	value = 0
	while True:
		try:
			value = int(input(prompt))
		except ValueError:
			continue
		if value >= 0 and value <= max:
			break
	return value

main()
