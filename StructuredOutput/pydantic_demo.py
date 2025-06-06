from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):
    name:str = "Dipit"
    age: Optional[int] = None
    email: EmailStr
    cgpa: float = Field(gt = 0, lt = 10)


new_student = {
    "age":19,
    "name":"Dipit",
    "email":"dipitmadan@gmail.com",
    "cgpa": 9
}

student = Student(**new_student)
print(dict(student)["name"])
