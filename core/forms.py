from django import forms

class ContentCreatorForm(forms.Form):
    topic = forms.CharField(
        label="enter a topic",
        max_length=200,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "e.g. nigeria economy and how it affects africa"
        })
    )

class ResearcherForm(forms.Form):
    topic = forms.CharField(
        label="Enter Research Topic",
        max_length=100,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Enter Research Topic",
        })
    )
    research_notes = forms.CharField(
        label="What are the key things to note regarding the research",
        max_length=600,
        widget=forms.Textarea(attrs={
            "class": "form-control",
            "placeholder": "Enter Reseach Notes",
            "rows": 5
        })
    )
    project_outline = forms.CharField(
        label="Project Outline",
        widget=forms.Textarea(attrs={
            "class": "form-control",
            "placeholder": "Enter Project Outline",
            "rows": 5
        })
    )
    project_draft = forms.CharField(
        label="Do you have a project draft, if not leave this field as blank",
        widget=forms.Textarea(attrs={
            "class": "form-control",
            "placeholder": "If you haven't started the project leave as black",
            "rows": 5
        })
    )

class SeoOptimizerForm(forms.Form):
    topic = forms.CharField(
        label="Topic",
        max_length=200,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Enter Blog Topic"
        })
    )

    draft_content = forms.CharField(
        label="Blog Content",
        widget=forms.Textarea(attrs={
            "class": "form-control",
            "placeholder": "Enter blog content"
        })
    )

class SmediaCampaignForm(forms.Form):
    topic = forms.CharField(
        label="Enter Campaign Topic",
        max_length=200,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "e.g Launching a new AI-powered study app for students"
        })
    )

class ResumeCreatorForm(forms.Form):
    job_description = forms.CharField(
        label="What is the Job Description",
        max_length=200,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "We are seeking a Data Analyst with experience in SQL, Python, and Tableau."
        })
    )

    resume = forms.CharField(
        label="What should the employer know about you...",
        max_length=200,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": " John Doe - Skills: Excel, PowerPoint, SQL basics - Experience: Marketing intern (2020-2021), Data assistant (2021-2022) - Education: BSc in Statistics"
        })
    )

