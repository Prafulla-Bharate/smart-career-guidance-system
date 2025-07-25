from pydantic import BaseModel, Field
from typing import Optional, List

class StudentInput(BaseModel):
    Name: Optional[str] = "Not Available"
    Age: Optional[int] = None
    Gender: Optional[str] = "Not Available"
    Email: Optional[str] = "Not Available"
    Degree: Optional[str] = "Not Available"
    Branch: Optional[str] = "Not Available"
    CGPA: Optional[float] = None
    Personality_Type: Optional[str] = "Not Available"
    Preferred_Work_Style: Optional[str] = "Not Available"
    Skills: Optional[str] = "Not Available"
    Soft_Skills: Optional[str] = "Not Available"
    Interests: Optional[str] = "Not Available"
    Certifications: Optional[str] = "Not Available"
    Internship_Experience: Optional[str] = "Not Available"
    Career_Goal: Optional[str] = "Not Available"
    Favorite_Subjects: Optional[str] = "Not Available"
    Resume_Link: Optional[str] = "Not Available"
