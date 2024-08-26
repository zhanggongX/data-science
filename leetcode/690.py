# Definition for Employee.
from typing import List

class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates

class Solution:

    def getImportance(self, employees: List['Employee'], id: int) -> int:
        employee_dict = {employee.id: employee for employee in employees}
        return self.dfs(employee_dict[id], employee_dict)

    def dfs(self, employee, employee_dict) -> int:
        total = employee.importance
        if(employee.subordinates is None):
            return total

        for sub in employee.subordinates:
            total += self.dfs(employee_dict[sub], employee_dict)
        return total



if __name__ == '__main__':
    employees = [Employee(1, 5, [2, 3]), Employee(2, 3, None), Employee(3,3, None)]
    print(Solution().getImportance(employees, 1))
