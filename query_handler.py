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


def mentors_by_country():
    query = """SELECT schools.country, COUNT(schools.country)
                FROM schools
                INNER JOIN mentors ON mentors.city=schools.city
                GROUP BY schools.country
                ORDER BY schools.country;"""
    mentors_by_country_query = datamanager.run_query(query)
    return mentors_by_country_query


def contacts():
    query = """SELECT schools.name, mentors.first_name || ' ' || mentors.last_name AS mentors_full_name
                FROM mentors
                INNER JOIN schools ON mentors.id=schools.contact_person
                ORDER BY schools.name;"""
    contacts_query = datamanager.run_query(query)
    return contacts_query


def applicants():
    query = """SELECT applicants.first_name, applicants.application_code, applicants_mentors.creation_date
                FROM applicants
                INNER JOIN applicants_mentors ON applicants.id=applicants_mentors.applicant_id
                WHERE applicants_mentors.creation_date > '2016-01-01'
                ORDER BY applicants_mentors.creation_date DESC;"""
    applicants_query = datamanager.run_query(query)
    return applicants_query

