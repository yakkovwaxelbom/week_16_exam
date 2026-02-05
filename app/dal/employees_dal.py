from core.config import settings

class EmployeesDal:

    def __init__(self, db):

        self.db = db
        self.coll = settings.EMPLOYEES_COOL  

    def get_engineering_high_salary_employees(self, min_salary):
    
        project = {"_id": 0, "name": 1, "employee_id": 1, "salary": 1}
        match = {"job_role.department": "Engineering", "salary": {"$gt": min_salary}}

        return list(self.db[self.coll].find(match, project)) 
    

    def get_employees_by_age_and_role(self, min_age, max_age, roles):

        match = {"age": {"$gte": min_age, "$lte": max_age}, "$or": [{"job_role.title": r} for r in roles]}

        results = []

        for doc in self.db[self.coll].find(match):
            doc["_id"] = str(doc["_id"])
            results.append(doc)

        return results

    
    def get_top_seniority_employees_excluding_department(self, top_n, excluded_department):

        match = {"job_role.department": {"$ne": excluded_department}}
        sort = [("years_at_company", -1)]

        results = []

        for doc in self.db[self.coll].find(match).sort(sort).limit(top_n):
            doc["_id"] = str(doc["_id"])
            results.append(doc)

        return results
    

    def get_employees_by_age_or_seniority(self, min_age, max_years_at_company):

        project = {"_id": 0, "name": 1, "years_at_company": 1, "age": 1}
        match = {"$or": [{"age": {"$gt": min_age}}, {"years_at_company": {"$lt": max_years_at_company}}]}

        return list(self.db[self.coll].find(match, project))
    
    def get_managers_excluding_departments(self, *excluded_departments):

        match = {"job_role.title": "Manager", "job_role.department": {"$nin": excluded_departments}}

        results = []

        for doc in self.db[self.coll].find(match):
            doc["_id"] = str(doc["_id"])
            results.append(doc)

        return results    

    def get_employees_by_lastname_and_age(self, max_age, last_name):

        project = {"_id": 0, "name": 1, "age": 1, "job_role.department": 1}
        match = {"name": {"$regex": f'({"|".join(last_name)})$', "$options": "i"}, "age": {"$lt": max_age}}

        return list(self.db[self.coll].find(match, project))
    