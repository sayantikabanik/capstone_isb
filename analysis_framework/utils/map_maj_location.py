def map_maj_location(major_locations,location_name):
    
    for loc in major_locations:
        ind=-1
        if location_name.find(loc)!=-1:
            ind=location_name.find(loc)
            return loc
    if ind==-1:
        return location_name