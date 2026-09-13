master_string_list = ['0,hi,hello,3,1.5','1,hola,saludos,4,6.9','2,nihao,ninhao,8,8.8']

def parse_row(row: str) -> list:
    """
    Accepts a single row (string) read from the data file.
    Splits it into a list of individual values, cast to numeric datatypes where appropriate.
    :param row: the string row read from the file
    :return: the parsed row, as a list
    """
    # use .split() and ID numbers/replace in list later
    r_items = row.split(',') # list of strings for now

    # hard code indexes to convert to number types
    eID = r_items[0] # exam ID string
    weight_kg = r_items[3] # weight in kg, string
    height_m = r_items[4] # height in m, string
    r_items[0] = int(eID) # exam ID, int
    r_items[3] = int(weight_kg) # weight in kg, int
    r_items[4] = float(height_m) # height in m, float
    
    #print(r_items)
    return r_items

for r in master_string_list: # iterate through rows
        r_list = parse_row(r) # list of items in current row. Can i have temporary lists in for loops?
        #wt = r_list[3] # get weight and height
        #ht = r_list[4]
        #calculate, write bmi into new csv
        print(r_list)