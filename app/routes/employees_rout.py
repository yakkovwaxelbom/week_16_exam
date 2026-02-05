from fastapi import routing, Depends, Query
from typing import Optional
from typing import List

from core.db import get_db
from dal.employees_dal import EmployeesDal


router = routing.APIRouter(prefix="/employees", tags=["Employees"])


@router.get('/engineering/high-salary')
def get_high_salary_employees(min_salary: int = 65_000, db = Depends(get_db)):
    
    return EmployeesDal(db).get_engineering_high_salary_employees(min_salary)

@router.get('/by-age-and-role')
def get_employees_by_age_and_role(min_age: int = 30, max_age: int = 45,
    roles: List[str] = Query(["Specialist", "Engineer"]),
    db = Depends(get_db)):

    return EmployeesDal(db).get_employees_by_age_and_role(min_age, max_age, roles)
@router.get('/top-seniority')
def get_top_seniority_employees(top_n: int = 7,
                                 excluded_department: str = "HR",
                                   db = Depends(get_db)):
    
    return EmployeesDal(db).get_top_seniority_employees_excluding_department(
        top_n, excluded_department)   

@router.get('/age-or-seniority')
def get_employees_by_age_or_seniority(min_age: int = 50, 
                                      max_years_at_company: int = 3, 
                                      db = Depends(get_db)):
    
    return EmployeesDal(db).get_employees_by_age_or_seniority(
        min_age, max_years_at_company)

@router.get('/managers/excluding-departments')
def get_managers_excluding_departments(excluded_departments: List[str] = 
                                       Query(["Sales", "Marketing"]),
                                        db = Depends(get_db)):
    
    return EmployeesDal(db).get_managers_excluding_departments(excluded_departments)    

@router.get('/by-lastname-and-age')
def get_employees_by_lastname_and_age(last_name: List[str] = Query(["Nelson", "Wright"]), 
                                      max_age: int = 35, 
                                      db = Depends(get_db)):
    
    return EmployeesDal(db).get_employees_by_lastname_and_age(
        max_age, last_name) 
