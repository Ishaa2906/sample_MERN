from fastapi import FastAPI
from pydantic import BaseModel
class Student(BaseModel):
    stuname: str
    studept: str
    stuusername:str
    stupassword:str
    stuage:int
    stumark:float
app=FastAPI()
#localhost:8000/getStudents
@app.get("/getStudents")
def getStudents():
    return "Get students method called"
#localhost:8000/addStudent
@app.post("/addStudent")
def addStudent(stu:Student):
    return {"student_details":stu}
#try two more routes
#updateStudent => put & /deletestudent => delete
@app.put("/putStudent")
def putStudent():
    return "Put student method called"
@app.delete("/deleteStudent")
def deleteStudent():
    return "Delete student method called"

@app.get("/getParticularStudent/{id}")
def getParticularStudent(id:int):
    return{"userid":id}
@app.get("/filterdept")
def filterdept(dept:str, mark:int):
    return{"dept":dept, "mark":mark}