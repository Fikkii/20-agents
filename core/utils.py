import sys, io, markdown
from django.shortcuts import render

def run_crew_with_form(request, form_class, crew_runner):
    old_stdout = sys.stdout
    sys.stdout = mystdout = io.StringIO()
    result = ""
    task_outputs = {}

    form = form_class(request.POST or None)
    if request.method == "POST" and form.is_valid():
        try:
            crew_instance = crew_runner().crew()
            result = crew_instance.kickoff(inputs=form.cleaned_data)

            task_outputs = [
                {
                    "description": t.description,
                    "output": markdown.markdown(str(t.output))
                } for t in crew_instance.tasks
            ]

            result = markdown.markdown(str(result))
            logs = mystdout.getvalue()

            return render (request, form_success,
                {
                    "result": result,
                    "logs": logs,
                    "tasks": task_outputs,
                }
            )

        finally:
            sys.stdout = old_stdout
    else:
        form = ContentCreatorForm()

        return render(request, "form.html", {
            "form": form
        })


