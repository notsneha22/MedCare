from django.shortcuts import render, redirect
from .models import LabReport
from .forms import LabReportForm

# Create your views here.

def report_list(request):

    reports = LabReport.objects.all()

    return render(
        request,
        "lab_reports/report_list.html",
        {"reports": reports},
    )
def upload_report(request):

    if request.method == "POST":

        form = LabReportForm(
            request.POST,
            request.FILES,
        )

        if form.is_valid():
            form.save()
            return redirect("report_list")

    else:
        form = LabReportForm()

    return render(
        request,
        "lab_reports/upload_report.html",
        {"form": form},
    )