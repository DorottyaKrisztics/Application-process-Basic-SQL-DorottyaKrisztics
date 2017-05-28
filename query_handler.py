import datamanager


def mentors_and_schools():
    query = """SELECT mentors.id, mentors.first_name, mentors.last_name, schools.name, schools.country
                FROM mentors
                INNER JOIN schools ON mentors.id=schools.contact_person
                ORDER BY mentors.id;"""
    mentors_query = datamanager.run_query(query)
    return mentors_query


def all_school():
    query = """SELECT mentors.id, mentors.first_name, mentors.last_name, schools.name, schools.country
                FROM mentors
                RIGHT JOIN schools ON mentors.id=schools.contact_person
                ORDER BY mentors.id;"""
    all_school_query = datamanager.run_query(query)
    return all_school_query

