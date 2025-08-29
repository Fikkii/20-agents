import io
import sys
import markdown
from django.shortcuts import render

from django.views import View

class CrewView(View):
    form_class = None
    crew_runner = None
    template_name = "crew_output.html"

    def __init__(self, **kwargs):
        # Prepare to capture stdout
        super().__init__(**kwargs)
        self.old_stdout = sys.stdout
        sys.stdout = self.mystdout = io.StringIO()
        self.result = ""
        self.task_outputs = {}


    def get(self, request):
        form = self.form_class() # Ignore

        return render(request, "form.html", {
            "form": form
        })

    def post(self, request):
        try:
            ## Fetch the user form
            form = self.form_class(request.POST)

            if form.is_valid():
                # Build crew only once
                crew_instance = self.crew_runner().crew()

                # Run execution
                self.result = crew_instance.kickoff(inputs=form.cleaned_data)

                self.task_outputs = [
                    {
                        "description": t.description,
                        "output": markdown.markdown(str(t.output))  # convert markdown → HTML
                    } for t in crew_instance.tasks
                ]

        finally:
            # Restore stdout
            sys.stdout = self.old_stdout

            # Collect verbose logs
            logs = self.mystdout.getvalue()

            self.result = markdown.markdown(str(self.result))
            context = {
                  "result": self.result,
                  "logs": logs,
                  "tasks": self.task_outputs
              }

            return render(request, "crew_output.html", context)

