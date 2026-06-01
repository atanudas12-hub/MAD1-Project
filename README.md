<img width="1080" height="1080" alt="569286425-8fdc8604-53f4-4263-ae76-c31016590c91" src="https://github.com/user-attachments/assets/d0540001-4772-4d83-a94c-de94471e92be" />

# AD University Placement Portal 🎓
## By: Atanu Das
## 24f2007175 | Modern Application Development - I | IIT Madras
--------

## Project Overview

A comprehensive web-based platfrom degined to streaming the campus recruitment process. This portal serves as a bridge between students, recruiting companies and the university's placement administration ensuring a smooth and organized workflow for job posting,student applications and interview drives.

### Screenshots 

| | | |
|:---------------------------:|:----------------------------:|:---------------------------:|
|<img width="2879" height="1456" alt="569260304-2b1f05c8-8805-4683-bdca-46af3f5e6771" src="https://github.com/user-attachments/assets/2ded5009-9274-492e-bdba-e6ccad09d1ec" />Home Page | <img width="2879" height="1453" alt="569241238-78dd9b37-9388-48ba-90fc-28d4ace7243a" src="https://github.com/user-attachments/assets/1761cf7b-abca-458f-b7df-624fa90b67af" />Login Page | <img width="2879" height="1445" alt="569241694-3ffce217-499a-4b2f-a825-8e2a356fc83e" src="https://github.com/user-attachments/assets/b0caa300-17a0-4541-8534-ec1f12050566" />Contact Page |
|<img width="2879" height="1456" alt="569245317-40af5d1d-861b-4cfa-805a-e746027dbb23" src="https://github.com/user-attachments/assets/773a5b01-5e35-4a26-9e8f-7aef8ecfbff8" />About Us Section | <img width="2879" height="1450" alt="569242632-db350be4-d419-47f8-9f8e-1c07c0413945" src="https://github.com/user-attachments/assets/c7f0000e-d94d-4b3a-a3eb-4071085404a1" />Admin Dashboard | <img width="2879" height="1451" alt="569242936-ef205ae3-5f66-43ce-bf6d-d43e716b5e54" src="https://github.com/user-attachments/assets/84bb425b-b794-4bbe-800b-90c919763a21" />Admins's Company Section |
|<img width="2879" height="1450" alt="569243409-ade2190d-5562-44b1-bcc2-48bd5bdbf61e" src="https://github.com/user-attachments/assets/988078cb-d382-4d75-95a9-ce2b1e7ed9c7" />Admin's Students Section |<img width="2879" height="1454" alt="575728024-5a9fb419-3642-454b-8003-03f809f5b76d" src="https://github.com/user-attachments/assets/d6d95794-1515-4b94-987d-4534a4ad42b2" />Admin's Jobs or Drives Section |<img width="2879" height="1449" alt="569244397-908577b4-2f39-4040-a090-dd173224fa87" src="https://github.com/user-attachments/assets/d5c4af61-a273-4717-b600-02189b8591bc" />Admin's Applications Section |
|<img width="1062" height="463" alt="569262687-363ec450-3b3e-48b8-af4b-9ca5f224b641" src="https://github.com/user-attachments/assets/71086aff-d2d0-4c67-b3e4-b2ea0a8c983b" />Register Option | <img width="2879" height="1449" alt="569262918-9392e5da-c8c9-4610-a00f-06229ffc06a3" src="https://github.com/user-attachments/assets/4f70f1a3-63a4-424f-894f-0d915b80c473" />Student Dashboard |<img width="2879" height="1447" alt="569263139-e866372d-3192-400d-a3c8-851b0358c1ce" src="https://github.com/user-attachments/assets/ec0efda9-3ac2-4455-9452-4131c951ab6a" />Company Dashboard |







# Key Features:

## 👨‍💼 For Administrators (/admin)
 - Centralized Dashboard
 - Students Management
 - Company Management
 - Drive & Application Tracking
### email_id= admin@iitm.ac.in
### password= admin123

## 🏢 For Companies (/company)
  - Company Dashboard
  - Drive Management
  - Applicant Tracking

## 👨‍🎓 For Students (/student)
  - Student Dashboard
  - Browse Drives
  - Application History

## 🔐 Authentication(/auth)
  - Seccure, role-based login system.
  - Dedicated registration flows for both students and companies(requiring admin approval).
-----

# 🌐API Resource and End Points


| | | |
|:---------------------------:|:----------------------------:|:---------------------------:|
|End Point	|Method |Description |
/	| GET |	Home page |
/login	| GET, POST	| User login |
/logout	| GET	| Logout User |
/register/student	| GET, POST	| Register Student |
/student/dashboard | GET	| View Student Dashboard |
/student/drives	| GET	| View Available Drives
/student/apply/`<id>`	| GET	| Apply for Placement Drives
/student/applications| GET	| View application History
/student/profile| GET, POST	| Update student Profile
/view/resume/`<student_id>`	| GET	| View Uploaded Resume
/register/company	| GET, POST	| Register Company
/company/dashboard|	GET	| Company Dashboard
/company/create_drives	| GET, POST |	Create placement drive
/company/drives	| GET	| View Company Drives
/company/drive/edit/`<id>` | GET, POST | 	Edit Drive
/company/drive/delete/`<id>`	| GET	| Close Drive
/company/drive/`<id>`/applications	| GET	 | View Applications
/company/application/update/`<id>/<status>`	| GET	| Update Application Status
/admin/dashboard	| GET	| Admin dashboard Overview
/admin/companies	| GET	| Manage Companies
/admin/company/approve/`<id>`|	GET	| Approve Company
/admin/company/reject/`<id>`	| GET	| Reject company
/admin/company/blacklist/`<id>`	| GET	| Company Blacklist
/admin/company/delete/`<id>`|	GET	| Delete Company
/admin/students	| GET	| Manage Students
/admin/students/blacklist/`<id>`|	GET	| Student Blacklist
/admin/students/delete/`<id>`	| GET	| Delete Students
/admin/drives	| GET	| Manage Placement Drives
/admin/drives/approve/`<id>`| 	GET	| Approve Drive
/admin/drives/reject/`<id>`	| GET | Reject Drive
/admin/applications	| GET	| View All Applications
/about |	GET	| About Page
/contact	| GET	| Contact page


# 🎥Video link
https://drive.google.com/file/d/1c83GURp2JfdUcPN2uJUMF-N6EU4NQ8sC/view?usp=sharing

# github link
https://github.com/atanudas1206/Placement-Portal-Application


