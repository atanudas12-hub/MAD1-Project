

# ============================================
# FILE: app.py
# ============================================
from flask import Flask, render_template, request, redirect, url_for, session, flash
from models import db, Admin, Student, Company, PlacementDrive, Application
from config import Config
from datetime import datetime, date
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

with app.app_context():
    db.create_all()
    if not Admin.query.filter_by(username='admin').first():
        admin = Admin(username='admin', email='admin@iitm.ac.in')
        admin.set_password('admin123')
        db.session.add(admin)
        db.session.commit()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        role = request.form.get('role')
        
        if role == 'admin':
            user = Admin.query.filter_by(email=email).first()
            if user and user.check_password(password):
                session['user_id'] = user.id
                session['role'] = 'admin'
                flash('Login successful!', 'success')
                return redirect(url_for('admin_dashboard'))
        
        elif role == 'student':
            user = Student.query.filter_by(email=email).first()
            if user and user.check_password(password):
                if user.is_blacklisted:
                    flash('Your account has been blacklisted.', 'error')
                    return redirect(url_for('login'))
                session['user_id'] = user.id
                session['role'] = 'student'
                flash('Login successful!', 'success')
                return redirect(url_for('student_dashboard'))
        
        elif role == 'company':
            user = Company.query.filter_by(email=email).first()
            if user and user.check_password(password):
                if user.approval_status != 'Approved':
                    flash('Your account is pending approval.', 'warning')
                    return redirect(url_for('login'))
                if user.is_blacklisted:
                    flash('Your account has been blacklisted.', 'error')
                    return redirect(url_for('login'))
                session['user_id'] = user.id
                session['role'] = 'company'
                flash('Login successful!', 'success')
                return redirect(url_for('company_dashboard'))
        
        flash('Invalid credentials!', 'error')
    
    return render_template('auth/login.html')

@app.route('/register/student', methods=['GET', 'POST'])
def register_student():
    if request.method == 'POST':
        try:
            student = Student(
                roll_number=request.form.get('roll_number'),
                name=request.form.get('name'),
                email=request.form.get('email'),
                phone=request.form.get('phone'),
                department=request.form.get('department'),
                cgpa=float(request.form.get('cgpa', 0))
            )
            student.set_password(request.form.get('password'))
            db.session.add(student)
            db.session.commit()
            flash('Registration successful! Please login.', 'success')
            return redirect(url_for('login'))
        except Exception as e:
            db.session.rollback()
            flash('Registration failed. Email or roll number already exists.', 'error')
    
    return render_template('auth/register_student.html')

@app.route('/register/company', methods=['GET', 'POST'])
def register_company():
    if request.method == 'POST':
        try:
            company = Company(
                company_name=request.form.get('company_name'),
                email=request.form.get('email'),
                hr_name=request.form.get('hr_name'),
                hr_contact=request.form.get('hr_contact'),
                website=request.form.get('website'),
                description=request.form.get('description')
            )
            company.set_password(request.form.get('password'))
            db.session.add(company)
            db.session.commit()
            flash('Registration successful! Wait for admin approval.', 'success')
            return redirect(url_for('login'))
        except Exception as e:
            db.session.rollback()
            flash('Registration failed. Email already exists.', 'error')
    
    return render_template('auth/register_company.html')

@app.route('/logout')
def logout():
    session.clear()
    flash('Logged out successfully!', 'success')
    return redirect(url_for('index'))

@app.route('/admin/dashboard')
def admin_dashboard():
    if session.get('role') != 'admin':
        return redirect(url_for('login'))
    
    total_students = Student.query.count()
    total_companies = Company.query.count()
    total_drives = PlacementDrive.query.count()
    total_applications = Application.query.count()
    pending_companies = Company.query.filter_by(approval_status='Pending').count()
    pending_drives = PlacementDrive.query.filter_by(status='Pending').count()
    
    return render_template('admin/dashboard.html',
                         total_students=total_students,
                         total_companies=total_companies,
                         total_drives=total_drives,
                         total_applications=total_applications,
                         pending_companies=pending_companies,
                         pending_drives=pending_drives)

@app.route('/admin/companies')
def admin_manage_companies():
    if session.get('role') != 'admin':
        return redirect(url_for('login'))
    
    search = request.args.get('search', '')
    if search:
        companies = Company.query.filter(Company.company_name.contains(search)).all()
    else:
        companies = Company.query.all()
    
    return render_template('admin/manage_companies.html', companies=companies)

@app.route('/admin/company/approve/<int:id>')
def approve_company(id):
    if session.get('role') != 'admin':
        return redirect(url_for('login'))
    
    company = Company.query.get_or_404(id)
    company.approval_status = 'Approved'
    db.session.commit()
    flash(f'{company.company_name} approved!', 'success')
    return redirect(url_for('admin_manage_companies'))

@app.route('/admin/company/reject/<int:id>')
def reject_company(id):
    if session.get('role') != 'admin':
        return redirect(url_for('login'))
    
    company = Company.query.get_or_404(id)
    company.approval_status = 'Rejected'
    db.session.commit()
    flash(f'{company.company_name} rejected!', 'success')
    return redirect(url_for('admin_manage_companies'))

@app.route('/admin/company/blacklist/<int:id>')
def blacklist_company(id):
    if session.get('role') != 'admin':
        return redirect(url_for('login'))
    
    company = Company.query.get_or_404(id)
    company.is_blacklisted = not company.is_blacklisted
    db.session.commit()
    status = 'blacklisted' if company.is_blacklisted else 'unblacklisted'
    flash(f'{company.company_name} {status}!', 'success')
    return redirect(url_for('admin_manage_companies'))

@app.route('/admin/company/delete/<int:id>')
def delete_company(id):
    if session.get('role') != 'admin':
        return redirect(url_for('login'))
    
    company = Company.query.get_or_404(id)
    db.session.delete(company)
    db.session.commit()
    flash('Company deleted!', 'success')
    return redirect(url_for('admin_manage_companies'))

@app.route('/admin/students')
def admin_manage_students():
    if session.get('role') != 'admin':
        return redirect(url_for('login'))
    
    search = request.args.get('search', '')
    if search:
        students = Student.query.filter(
            (Student.name.contains(search)) | 
            (Student.roll_number.contains(search)) |
            (Student.email.contains(search))
        ).all()
    else:
        students = Student.query.all()
    
    return render_template('admin/manage_students.html', students=students)

@app.route('/admin/student/blacklist/<int:id>')
def blacklist_student(id):
    if session.get('role') != 'admin':
        return redirect(url_for('login'))
    
    student = Student.query.get_or_404(id)
    student.is_blacklisted = not student.is_blacklisted
    db.session.commit()
    status = 'blacklisted' if student.is_blacklisted else 'unblacklisted'
    flash(f'{student.name} {status}!', 'success')
    return redirect(url_for('admin_manage_students'))

@app.route('/admin/student/delete/<int:id>')
def delete_student(id):
    if session.get('role') != 'admin':
        return redirect(url_for('login'))
    
    student = Student.query.get_or_404(id)
    db.session.delete(student)
    db.session.commit()
    flash('Student deleted!', 'success')
    return redirect(url_for('admin_manage_students'))

@app.route('/admin/drives')
def admin_manage_drives():
    if session.get('role') != 'admin':
        return redirect(url_for('login'))
    
    drives = PlacementDrive.query.all()
    return render_template('admin/manage_drives.html', drives=drives)

@app.route('/admin/drive/approve/<int:id>')
def approve_drive(id):
    if session.get('role') != 'admin':
        return redirect(url_for('login'))
    
    drive = PlacementDrive.query.get_or_404(id)
    drive.status = 'Approved'
    db.session.commit()
    flash('Drive approved!', 'success')
    return redirect(url_for('admin_manage_drives'))

@app.route('/admin/drive/reject/<int:id>')
def reject_drive(id):
    if session.get('role') != 'admin':
        return redirect(url_for('login'))
    
    drive = PlacementDrive.query.get_or_404(id)
    drive.status = 'Rejected'
    db.session.commit()
    flash('Drive rejected!', 'success')
    return redirect(url_for('admin_manage_drives'))

@app.route('/admin/applications')
def admin_view_applications():
    if session.get('role') != 'admin':
        return redirect(url_for('login'))
    
    applications = Application.query.all()
    return render_template('admin/view_applications.html', applications=applications)

@app.route('/company/dashboard')
def company_dashboard():
    if session.get('role') != 'company':
        return redirect(url_for('login'))
    
    company = Company.query.get(session['user_id'])
    drives = PlacementDrive.query.filter_by(company_id=company.id).all()
    
    drive_stats = []
    for drive in drives:
        applicant_count = Application.query.filter_by(drive_id=drive.id).count()
        drive_stats.append({'drive': drive, 'applicants': applicant_count})
    
    return render_template('company/dashboard.html', company=company, drive_stats=drive_stats)

@app.route('/company/create_drive', methods=['GET', 'POST'])
def create_drive():
    if session.get('role') != 'company':
        return redirect(url_for('login'))
    
    company = Company.query.get(session['user_id'])
    if company.approval_status != 'Approved':
        flash('Your company must be approved first!', 'error')
        return redirect(url_for('company_dashboard'))
    
    if request.method == 'POST':
        try:
            drive = PlacementDrive(
                company_id=company.id,
                job_title=request.form.get('job_title'),
                job_description=request.form.get('job_description'),
                eligibility_criteria=request.form.get('eligibility_criteria'),
                required_cgpa=float(request.form.get('required_cgpa', 0)),
                salary_package=request.form.get('salary_package'),
                application_deadline=datetime.strptime(request.form.get('application_deadline'), '%Y-%m-%d').date()
            )
            db.session.add(drive)
            db.session.commit()
            flash('Drive created! Waiting for admin approval.', 'success')
            return redirect(url_for('company_dashboard'))
        except Exception as e:
            db.session.rollback()
            flash('Failed to create drive.', 'error')
    
    return render_template('company/create_drive.html')

@app.route('/company/drives')
def company_view_drives():
    if session.get('role') != 'company':
        return redirect(url_for('login'))
    
    company = Company.query.get(session['user_id'])
    drives = PlacementDrive.query.filter_by(company_id=company.id).all()
    
    return render_template('company/view_drives.html', drives=drives)

@app.route('/company/drive/edit/<int:id>', methods=['GET', 'POST'])
def edit_drive(id):
    if session.get('role') != 'company':
        return redirect(url_for('login'))
    
    drive = PlacementDrive.query.get_or_404(id)
    if drive.company_id != session['user_id']:
        flash('Unauthorized!', 'error')
        return redirect(url_for('company_dashboard'))
    
    if request.method == 'POST':
        drive.job_title = request.form.get('job_title')
        drive.job_description = request.form.get('job_description')
        drive.eligibility_criteria = request.form.get('eligibility_criteria')
        drive.required_cgpa = float(request.form.get('required_cgpa', 0))
        drive.salary_package = request.form.get('salary_package')
        drive.application_deadline = datetime.strptime(request.form.get('application_deadline'), '%Y-%m-%d').date()
        drive.status = 'Pending'
        db.session.commit()
        flash('Drive updated! Waiting for admin re-approval.', 'success')
        return redirect(url_for('company_view_drives'))
    
    return render_template('company/edit_drive.html', drive=drive)

@app.route('/company/drive/close/<int:id>')
def close_drive(id):
    if session.get('role') != 'company':
        return redirect(url_for('login'))
    
    drive = PlacementDrive.query.get_or_404(id)
    if drive.company_id != session['user_id']:
        flash('Unauthorized!', 'error')
        return redirect(url_for('company_dashboard'))
    
    drive.status = 'Closed'
    db.session.commit()
    flash('Drive closed!', 'success')
    return redirect(url_for('company_view_drives'))

@app.route('/company/drive/delete/<int:id>')
def delete_drive(id):
    if session.get('role') != 'company':
        return redirect(url_for('login'))
    
    drive = PlacementDrive.query.get_or_404(id)
    if drive.company_id != session['user_id']:
        flash('Unauthorized!', 'error')
        return redirect(url_for('company_dashboard'))
    
    db.session.delete(drive)
    db.session.commit()
    flash('Drive deleted!', 'success')
    return redirect(url_for('company_view_drives'))

@app.route('/company/drive/<int:id>/applications')
def company_view_applications(id):
    if session.get('role') != 'company':
        return redirect(url_for('login'))
    
    drive = PlacementDrive.query.get_or_404(id)
    if drive.company_id != session['user_id']:
        flash('Unauthorized!', 'error')
        return redirect(url_for('company_dashboard'))
    
    applications = Application.query.filter_by(drive_id=id).all()
    return render_template('company/view_applications.html', drive=drive, applications=applications)

@app.route('/company/application/update/<int:id>/<status>')
def update_application_status(id, status):
    if session.get('role') != 'company':
        return redirect(url_for('login'))
    
    application = Application.query.get_or_404(id)
    drive = PlacementDrive.query.get(application.drive_id)
    
    if drive.company_id != session['user_id']:
        flash('Unauthorized!', 'error')
        return redirect(url_for('company_dashboard'))
    
    if status in ['Shortlisted', 'Selected', 'Rejected']:
        application.status = status
        db.session.commit()
        flash(f'Application {status.lower()}!', 'success')
    
    return redirect(url_for('company_view_applications', id=drive.id))

@app.route('/student/dashboard')
def student_dashboard():
    if session.get('role') != 'student':
        return redirect(url_for('login'))
    
    student = Student.query.get(session['user_id'])
    approved_drives = PlacementDrive.query.filter_by(status='Approved').filter(PlacementDrive.application_deadline >= date.today()).all()
    my_applications = Application.query.filter_by(student_id=student.id).all()
    
    return render_template('student/dashboard.html', 
                         student=student,
                         approved_drives=approved_drives,
                         my_applications=my_applications)

@app.route('/student/drives')
def student_view_drives():
    if session.get('role') != 'student':
        return redirect(url_for('login'))
    
    student = Student.query.get(session['user_id'])
    approved_drives = PlacementDrive.query.filter_by(status='Approved').filter(PlacementDrive.application_deadline >= date.today()).all()
    
    applied_drive_ids = [app.drive_id for app in Application.query.filter_by(student_id=student.id).all()]
    
    return render_template('student/view_drives.html', 
                         drives=approved_drives,
                         applied_drive_ids=applied_drive_ids)

@app.route('/student/apply/<int:id>')
def apply_drive(id):
    if session.get('role') != 'student':
        return redirect(url_for('login'))
    
    student = Student.query.get(session['user_id'])
    drive = PlacementDrive.query.get_or_404(id)
    
    if drive.status != 'Approved':
        flash('This drive is not available!', 'error')
        return redirect(url_for('student_view_drives'))
    
    if drive.application_deadline < date.today():
        flash('Application deadline has passed!', 'error')
        return redirect(url_for('student_view_drives'))
    
    if student.cgpa < drive.required_cgpa:
        flash(f'You do not meet the CGPA requirement ({drive.required_cgpa})!', 'error')
        return redirect(url_for('student_view_drives'))
    
    existing = Application.query.filter_by(student_id=student.id, drive_id=id).first()
    if existing:
        flash('You have already applied for this drive!', 'warning')
        return redirect(url_for('student_view_drives'))
    
    application = Application(student_id=student.id, drive_id=id)
    db.session.add(application)
    db.session.commit()
    flash('Application submitted successfully!', 'success')
    return redirect(url_for('student_dashboard'))

@app.route('/student/applications')
def student_applications():
    if session.get('role') != 'student':
        return redirect(url_for('login'))
    
    student = Student.query.get(session['user_id'])
    applications = Application.query.filter_by(student_id=student.id).all()
    
    return render_template('student/application_history.html', applications=applications)

@app.route('/student/profile', methods=['GET', 'POST'])
def student_profile():
    if session.get('role') != 'student':
        return redirect(url_for('login'))
    
    student = Student.query.get(session['user_id'])
    
    if request.method == 'POST':
        student.name = request.form.get('name')
        student.phone = request.form.get('phone')
        student.department = request.form.get('department')
        student.cgpa = float(request.form.get('cgpa', 0))
        
        if 'resume' in request.files:
            file = request.files['resume']
            if file and file.filename and allowed_file(file.filename):
                filename = secure_filename(f"{student.roll_number}_{file.filename}")
                os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
                filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(filepath)
                student.resume_path = filepath
        
        db.session.commit()
        flash('Profile updated successfully!', 'success')
        return redirect(url_for('student_profile'))
    
    return render_template('student/profile.html', student=student)

@app.route('/download/resume/<int:student_id>')
def download_resume(student_id):
    if not session.get('role'):
        return redirect(url_for('login'))
    
    student = Student.query.get_or_404(student_id)
    
    if session.get('role') == 'student' and session.get('user_id') != student_id:
        flash('Unauthorized access!', 'error')
        return redirect(url_for('student_dashboard'))
    
    if not student.resume_path or not os.path.exists(student.resume_path):
        flash('Resume not found!', 'error')
        return redirect(request.referrer or url_for('index'))
    
    from flask import send_file
    return send_file(student.resume_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)