<img width="1080" height="1080" alt="image" src="https://github.com/user-attachments/assets/8fdc8604-53f4-4263-ae76-c31016590c91" />

# AD University Placement Portal 🎓
## By: Atanu Das
## 24f2007175 | Modern Application Development - I | IIT Madras
--------

## Project Overview

A comprehensive web-based platfrom degined to streaming the campus recruitment process. This portal serves as a bridge between students, recruiting companies and the university's placement administration ensuring a smooth and organized workflow for job posting,student applications and interview drives.

### Screenshots 

| | | |
|:---------------------------:|:----------------------------:|:---------------------------:|
|<img width="2879" height="1456" alt="home page" src="https://github.com/user-attachments/assets/2b1f05c8-8805-4683-bdca-46af3f5e6771" />Home Page | <img width="2879" height="1453" alt="login page" src="https://github.com/user-attachments/assets/78dd9b37-9388-48ba-90fc-28d4ace7243a" /> Login Page | <img width="2879" height="1445" alt="contact" src="https://github.com/user-attachments/assets/3ffce217-499a-4b2f-a825-8e2a356fc83e" />Contact Page |
|<img width="2879" height="1456" alt="Screenshot 2026-03-25 185455" src="https://github.com/user-attachments/assets/40af5d1d-861b-4cfa-805a-e746027dbb23" />About Us Section | <img width="2879" height="1450" alt="admin dash" src="https://github.com/user-attachments/assets/db350be4-d419-47f8-9f8e-1c07c0413945" /> Admin Dashboard | <img width="2879" height="1451" alt="admin companies" src="https://github.com/user-attachments/assets/ef205ae3-5f66-43ce-bf6d-d43e716b5e54" /> Admins's Company Section |
|<img width="2879" height="1450" alt="admin student" src="https://github.com/user-attachments/assets/ade2190d-5562-44b1-bcc2-48bd5bdbf61e" />Admin's Students Section |<img width="2879" height="1458" alt="admin drive" src="https://github.com/user-attachments/assets/67164074-cb59-4821-bec4-0bd841c53c58" />Admin's Jobs or Drives Section |<img width="2879" height="1449" alt="admin manage" src="https://github.com/user-attachments/assets/908577b4-2f39-4040-a090-dd173224fa87" />Admin's Applications Section |
|<img width="1062" height="463" alt="register option" src="https://github.com/user-attachments/assets/363ec450-3b3e-48b8-af4b-9ca5f224b641" />Register Option | <img width="2879" height="1449" alt="student dash" src="https://github.com/user-attachments/assets/9392e5da-c8c9-4610-a00f-06229ffc06a3" />Student Dashboard |<img width="2879" height="1447" alt="company dash" src="https://github.com/user-attachments/assets/e866372d-3192-400d-a3c8-851b0358c1ce" />Company Dashboard |







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

# 📁Project Structure

<img width="288" height="1337" alt="project structure" src="https://github.com/user-attachments/assets/aaaeac02-22a7-46ad-9652-1c17d18f6dd5" />


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


