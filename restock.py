def restock_inventory(available_items, inventory_records, current_day):
    '''
    Updates inventory by adding restocked items and updates inventory records.
    
    Args:
        available_items (int): Available T-shirts after daily sales.
        inventory_records (List): A list of inventory records until the previous day.
        current_day (int): Day number to update as the current day.
    
    Returns:
        int: Updated available items after restocking.
    '''
    
    # Check if today is a restocking day (Day 0 or every 7 days)
    if current_day == 0:
        available_items = 1000
        restocked_items = 1000
        inventory_records.append((current_day, 0, restocked_items, available_items))
    elif current_day % 7 == 0:
        # Calculate the number of items to restock to reach 2000 units
        restocked_items = 2000 - available_items
        
        # Ensure restocked items don’t exceed the stock limit of 2000 units
        restocked_items = max(0, min(restocked_items, 2000))
        
        # Update available items after restocking
        available_items += restocked_items
        
        # Append today’s record to inventory_records
        inventory_records.append((current_day, 0, restocked_items, available_items))
    
    return available_items

