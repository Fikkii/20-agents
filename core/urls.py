from django.contrib import admin
from django.shortcuts import render
from django.urls import path, include

from .forms import ContentCreatorForm, ResumeCreatorForm, ResearcherForm, SeoOptimizerForm, SmediaCampaignForm

from .projects.content_creator.main import ContentCreatorCrew
from .projects.resume_creator.main import ResumeCreatorCrew
from .projects.researcher.main import ResearcherCrew
from .projects.seo_optimizer.main import SeoOptimizerCrew
from .projects.smedia_campaign.main import SmediaCampaignCrew

from .views import CrewView, dashboard_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", dashboard_view, name="home"),
]

agent_urls = [
    path('agents/content-creator', CrewView.as_view(
        form_class=ContentCreatorForm,
        crew_runner=ContentCreatorCrew,
    ), name="content_creator"),
    path('agents/resume-creator', CrewView.as_view(
        form_class=ResumeCreatorForm,
        crew_runner=ResumeCreatorCrew,
    ), name="resume_creator"),
    path('agents/researcher', CrewView.as_view(
        form_class=ResearcherForm,
        crew_runner=ResearcherCrew,
    ), name="researcher"),
    path('agents/seo-optimizer', CrewView.as_view(
        form_class=SeoOptimizerForm,
        crew_runner=SeoOptimizerCrew,
    ), name="seo_optimizer"),
    path('agents/smedia-campaign', CrewView.as_view(
        form_class=SmediaCampaignForm,
        crew_runner=SmediaCampaignCrew,
    ), name="smedia-campaign"),
]

urlpatterns = urlpatterns + agent_urls

