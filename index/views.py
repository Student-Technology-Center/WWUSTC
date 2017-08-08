from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from index.models import IssueForm

def index(request):

    context = {
        "user":request.user,
    }

    return render(
        request,
        "main_page.html",
        context
    )

@login_required
def issue(request):
    context = {}
    context['issue_form'] = IssueForm(request.POST or None)

    if request.method == 'POST':
        if context['issue_form'].is_valid():
            instance = context['issue_form'].save(commit=False)
            instance.user = request.user
            instance.save()
            context['received'] = True

    return render(
        request,
        'issues.html',
        context
    )