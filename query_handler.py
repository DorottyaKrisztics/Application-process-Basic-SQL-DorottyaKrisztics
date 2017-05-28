import datamanager

#  the name of the mentors plus the name and country of the school (joining with the schools table) 
#  ordered by the mentors id column (columns: mentors.first_name, mentors.last_name, schools.name, schools.country).


def mentors_and_schools():

    query = """SELECT mentors.first_name, mentors.last_name, schools.name, schools.country
                FROM mentors 
                INNER JOIN schools ON mentors.id=schools.contact_person;"""
    # INNER JOIN schools ON mentors.id=schools.contact_person
    mentors_query = datamanager.run_query(query)
    return mentors_query

