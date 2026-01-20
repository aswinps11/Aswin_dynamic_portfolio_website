from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import HomeContent, Skill, Education, Experience, Project, ContactMessage, User

# Create your views here.
def dashboard(request):
    return render(request,'backend/dashboard.html')

def homecontent(request):
    # Get or create the home content instance
    content, created = HomeContent.objects.get_or_create(id=1, defaults={
        'name': 'Your Name', 
        'role': 'Your Role',
        'about_title': 'About Me',
        'about_paragraph1': 'Short paragraph describing who you are, your degree, and what you are looking for.',
        'about_paragraph2': 'Another short paragraph about your interests, learning mindset, and goals.',
        'experience': 'Fresher / Internship Experience',
        'degree': 'B.Tech in Information Technology',
        'location': 'Kozhikode, Kerala, India',
        'email': 'yourmail@example.com',
        'phone': '+91 XXXXXXXXXX',
        'availability': 'Open to Work'
    })

    if request.method == 'POST':
        # Get form data for hero section only
        name = request.POST.get('name', '').strip()
        role = request.POST.get('role', '').strip()
        
        # Validate that required fields are not empty
        if name and role:
            # Update only the hero content
            content.name = name
            content.role = role
            content.save()
            messages.success(request, 'Hero content updated successfully!')
            return redirect('homecontent')
        else:
            messages.error(request, 'Please fill in all required fields.')

    return render(request, 'backend/homecontent.html', {'content': content})

def resume(request):
    # Get or create the home content instance
    content, created = HomeContent.objects.get_or_create(id=1, defaults={
        'name': 'Your Name', 
        'role': 'Your Role'
    })

    if request.method == 'POST':
        # Handle resume upload
        if 'resume' in request.FILES:
            content.resume = request.FILES['resume']
            content.save()
            messages.success(request, 'Resume uploaded successfully!')
            return redirect('resume')
        
        # Handle resume deletion
        elif 'delete_resume' in request.POST:
            if content.resume:
                content.resume.delete()
                content.resume = None
                content.save()
                messages.success(request, 'Resume deleted successfully!')
            else:
                messages.info(request, 'No resume to delete.')
            return redirect('resume')
        
        # Handle education addition
        elif 'add_education' in request.POST:
            degree = request.POST.get('degree', '').strip()
            institution = request.POST.get('institution', '').strip()
            year_range = request.POST.get('year_range', '').strip()
            degree_level = request.POST.get('degree_level', '').strip()
            if degree and institution and year_range and degree_level:
                Education.objects.create(
                    degree=degree,
                    institution=institution,
                    year_range=year_range,
                    degree_level=degree_level,
                    home_content=content
                )
                messages.success(request, 'Education added successfully!')
            else:
                messages.error(request, 'Please fill in all education fields.')
            return redirect('resume')
        
        # Handle experience addition
        elif 'add_experience' in request.POST:
            position = request.POST.get('position', '').strip()
            company = request.POST.get('company', '').strip()
            duration = request.POST.get('duration', '').strip()
            description = request.POST.get('description', '').strip()
            if position and company and duration and description:
                Experience.objects.create(
                    position=position,
                    company=company,
                    duration=duration,
                    description=description,
                    home_content=content
                )
                messages.success(request, 'Experience added successfully!')
            else:
                messages.error(request, 'Please fill in all experience fields.')
            return redirect('resume')
        
        # Handle education deletion
        elif 'delete_education' in request.POST:
            education_id = request.POST.get('education_id')
            try:
                education = Education.objects.get(id=education_id, home_content=content)
                education.delete()
                messages.success(request, 'Education deleted successfully!')
            except Education.DoesNotExist:
                messages.error(request, 'Education not found.')
            return redirect('resume')
        
        # Handle experience deletion
        elif 'delete_experience' in request.POST:
            experience_id = request.POST.get('experience_id')
            try:
                experience = Experience.objects.get(id=experience_id, home_content=content)
                experience.delete()
                messages.success(request, 'Experience deleted successfully!')
            except Experience.DoesNotExist:
                messages.error(request, 'Experience not found.')
            return redirect('resume')
        
        # Handle education editing
        elif 'edit_education' in request.POST:
            education_id = request.POST.get('education_id')
            try:
                education = Education.objects.get(id=education_id, home_content=content)
                education.degree = request.POST.get('degree', '').strip()
                education.institution = request.POST.get('institution', '').strip()
                education.year_range = request.POST.get('year_range', '').strip()
                education.degree_level = request.POST.get('degree_level', '').strip()
                if education.degree and education.institution and education.year_range and education.degree_level:
                    education.save()
                    messages.success(request, 'Education updated successfully!')
                else:
                    messages.error(request, 'Please fill in all education fields.')
            except Education.DoesNotExist:
                messages.error(request, 'Education not found.')
            return redirect('resume')
        
        # Handle experience editing
        elif 'edit_experience' in request.POST:
            experience_id = request.POST.get('experience_id')
            try:
                experience = Experience.objects.get(id=experience_id, home_content=content)
                experience.position = request.POST.get('position', '').strip()
                experience.company = request.POST.get('company', '').strip()
                experience.duration = request.POST.get('duration', '').strip()
                experience.description = request.POST.get('description', '').strip()
                if experience.position and experience.company and experience.duration and experience.description:
                    experience.save()
                    messages.success(request, 'Experience updated successfully!')
                else:
                    messages.error(request, 'Please fill in all experience fields.')
            except Experience.DoesNotExist:
                messages.error(request, 'Experience not found.')
            return redirect('resume')

    educations = content.educations.all()
    experiences = content.experiences.all()
    return render(request, 'backend/resume.html', {
        'content': content,
        'educations': educations,
        'experiences': experiences
    })

def aboutme(request):
    # Get or create the home content instance
    content, created = HomeContent.objects.get_or_create(id=1, defaults={
        'name': 'Your Name', 
        'role': 'Your Role',
        'about_title': 'About Me',
        'about_paragraph1': 'Short paragraph describing who you are, your degree, and what you are looking for.',
        'about_paragraph2': 'Another short paragraph about your interests, learning mindset, and goals.',
        'experience': 'Fresher / Internship Experience',
        'degree': 'B.Tech in Information Technology',
        'location': 'Kozhikode, Kerala, India',
        'email': 'yourmail@example.com',
        'phone': '+91 XXXXXXXXXX',
        'availability': 'Open to Work'
    })

    if request.method == 'POST':
        # Handle skill deletion
        if 'delete_skill' in request.POST:
            skill_id = request.POST.get('delete_skill')
            try:
                skill = Skill.objects.get(id=skill_id, home_content=content)
                skill.delete()
                messages.success(request, 'Skill deleted successfully!')
            except Skill.DoesNotExist:
                messages.error(request, 'Skill not found.')
            return redirect('aboutme')
        
        # Handle skill addition
        elif 'add_skill' in request.POST:
            skill_name = request.POST.get('new_skill', '').strip()
            if skill_name:
                Skill.objects.create(name=skill_name, home_content=content)
                messages.success(request, 'Skill added successfully!')
            else:
                messages.error(request, 'Please enter a skill name.')
            return redirect('aboutme')
        
        # Handle about me content update
        else:
            about_title = request.POST.get('about_title', '').strip()
            about_paragraph1 = request.POST.get('about_paragraph1', '').strip()
            about_paragraph2 = request.POST.get('about_paragraph2', '').strip()
            experience = request.POST.get('experience', '').strip()
            degree = request.POST.get('degree', '').strip()
            location = request.POST.get('location', '').strip()
            email = request.POST.get('email', '').strip()
            phone = request.POST.get('phone', '').strip()
            availability = request.POST.get('availability', '').strip()
            
            # Update the about me content
            content.about_title = about_title
            content.about_paragraph1 = about_paragraph1
            content.about_paragraph2 = about_paragraph2
            content.experience = experience
            content.degree = degree
            content.location = location
            content.email = email
            content.phone = phone
            content.availability = availability
            content.save()
            messages.success(request, 'About Me content updated successfully!')
            return redirect('aboutme')

    return render(request, 'backend/aboutme.html', {'content': content})


def portfolio(request):
    if request.method == "POST":
        # Add new project
        if "add_project" in request.POST:
            title = request.POST.get("title")
            date = request.POST.get("date")
            description = request.POST.get("description")
            tech_stack = request.POST.get("tech_stack")
            file = request.FILES.get("file")
            
            Project.objects.create(
                title=title,
                date=date,
                description=description,
                tech_stack=tech_stack,
                file=file
            )
            messages.success(request, "Project added successfully!")
            return redirect("portfolio")

        # Delete project
        if "delete_project" in request.POST:
            project_id = request.POST.get("delete_project")
            Project.objects.filter(id=project_id).delete()
            messages.success(request, "Project deleted successfully!")
            return redirect("portfolio")

        # Edit project
        if "edit_project" in request.POST:
            project_id = request.POST.get("project_id")
            project = Project.objects.get(id=project_id)
            project.title = request.POST.get("title")
            project.date = request.POST.get("date")
            project.description = request.POST.get("description")
            project.tech_stack = request.POST.get("tech_stack")
            if request.FILES.get("file"):
                project.file = request.FILES.get("file")
            project.save()
            messages.success(request, "Project updated successfully!")
            return redirect("portfolio")

    projects = Project.objects.all().order_by("-id")
    return render(request, "backend/portfolio.html", {"projects": projects})



def contact_submit(request):
    if request.method == 'POST':
        ContactMessage.objects.create(
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            phone=request.POST.get('phone'),
            subject=request.POST.get('subject'),
            message=request.POST.get('message'),
        )

        messages.success(request, "Your message has been sent successfully!")
        return redirect('index')   # MUST redirect

    return redirect('index')

# Admin view to see messages
def contact(request):
    messages = ContactMessage.objects.all().order_by('-created_at')
    return render(request, 'backend/contact.html', {'messages': messages})

def delete_contact_message(request, id):
    msg = get_object_or_404(ContactMessage, id=id)
    msg.delete()
    messages.success(request, "Message deleted successfully.")
    return redirect('contact')



# register
def register(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        
        if not name or not email or not password:
            return render(request, 'backend/register.html', {'error': 'All fields are required.'})
        
        if User.objects.filter(name=name).exists():
            return render(request,'backend/register.html',{'error':'Username already exists.'})
        
        if User.objects.filter(email=email).exists():
            return render(request,'backend/register.html',{'error':'email already exists.'})
        
        user=User(name=name,email=email,password=password)
        user.save()
        
        return render(request,'backend/login.html',{'msg':'User successfully registered.'})
    
    return render(request,'backend/register.html')


# login
def login(request):
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        
        try:
            user=User.objects.get(email=email,password=password)
            return render(request,'backend/dashboard.html',{'user':user})
        
        except User.DoesNotExist:
            return render(request,'backend/login.html',{'error':'Invalid credentials.'})
    
    return render(request,'backend/login.html')

# logout
def logout(request):
    request.session.flush()
    return render(request,'backend/login.html',{'msg':'You have been logged out successfully.'})
