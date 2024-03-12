class Vacancy:
    def __init__(self, name, salary, requirements, link):
        self.name = name
        if salary:
            self.salary = salary
        else:
            self.salary = 0
        self.requirements = requirements
        self.link = link
        
    def __eq__(self, other):
        return self.salary == other.salary

    def __lt__(self, other):
        return self.salary < other.salary

    def __gt__(self, other):
        return self.salary > other.salary
