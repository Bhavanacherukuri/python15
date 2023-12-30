class Employee:
    compeny='TCS'
    ceo='steve'
    def insert_member(obj,name,age,salary,eid):
       obj.name=name
       obj.age=age
       obj.salary=salary
       obj.eid=eid
    
bhanu=Employee()
hari=Employee()

Employee.insert_member(bhanu,'bhanu',21,50000,'21345')
Employee.insert_member(hari,'hari',22,40000,'21346')   
print(bhanu.name)
print(bhanu.age)
print(bhanu.salary)
print(bhanu.eid)
print(hari.name)
print(hari.age)
print(hari.salary)
print(hari.eid)

