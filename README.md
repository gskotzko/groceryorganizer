# groceryorganizer
## A simple python script to re-organize a grocery list by section within a particular store.

#### Grocery Organizer is a script that will allow you do parse a csv based, unorganized grocery list and then re-organize the list based on preferred store and how you like to flow through the store.

### Why?
##### Because it's one of my weird ticks that I hate going into the grocery stores around here and dealing with the unwashed hordes while trying to group and organize my trip based off of an unorganized list (that someone else gave me). Or if I'm there with my kids and suddenly we're across the store and there was one last item back on the other side and I have now shlep them back over. 

How it's supposed to work (initial idea):
1. Place list in unsortlist folder
2. Run lister.py
3. Select your preferred grocery store from Menu
  + Right now this contains just my usuals, want to expand past this to include others.
  + Selecting your store, selects a preferred flow through the store (Produce -> Dairy -> Meat -> Dry goods - > etc). Dependent on store.
4. The script then parses your list, checks the item against the grocery sections and creates a new list that is organized by section of store.

### Thing's I would like to improve:
1. It's clunky - I don't like how the different grocery sections are defined. I'm thinking a keyed dictionary may be a better approach.
2. It currently doesn't handle "new" items - need to build in a function that will say "if i not in list: (Prompt user to select section to append it to)
3. Date coding of lists (should be a simple fix)
4. Expand the list of stores
5. Eventually see if there are any APIs from stores like Wegmans, etc that access their in-store products
6. Change to a GUI setup, eventually make it an app.
