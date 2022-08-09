def extract_location(jobFunction):
    try:
        loc=jobFunction.split(' for ')[1].split(' in ')[1]
        return loc
    except:
        return 'Not Specified'