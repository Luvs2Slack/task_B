import random

def daily_sales(available_items, inventory_records, current_day):
    '''
***********COMPLETE THIS FUNCTION***********
This function is responsible for updating the sales for a given day.
---------------
Function Input:
---------------
available_items: (integer) Available Tshirts from the previous day.
inventory_records: (List) A list of inventory records until the previous day. Each row contains (day, sales, restocked items, available items)
current_day: (integer) Day number which you want to add as the current day. 

----------------
Function Output:
----------------
available_items:(integer) This function returns this integer which updates the available items at the current day.

The function will also update the inventory_records (For restocking) for a  given current day. 

    '''
    
    # Sales should only happen on non-restocking days
    if current_day % 7 >= 0:
        # Generate a random sales number between 0 and 200
        daily_sales = random.randint(0, 200)
        
        # Ensure sales do not exceed available items
        daily_sales = min(daily_sales, available_items)
        
        # Update available items after sales
        available_items -= daily_sales
        
        # Append the day's sales data to inventory records with 0 restocked items
        inventory_records.append((current_day, daily_sales, 0, available_items))
    
    return available_items
