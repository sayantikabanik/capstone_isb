"""
Method to extract locations: used is pre-processing
"""


def extract_location(job_function):
    try:
        loc = job_function.split(' for ')[1].split(' in ')[1]
        return loc
    except:
        return "Not Specified"
    finally:
        print("Unidentified error, check logs")
