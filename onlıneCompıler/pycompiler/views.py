from django.shortcuts import render
import sys


# Create your views here.
# create index
def index(request):
    return render(request, "index.html")


def runcode(request):
    if request.method == "POST":
        codeareadata = request.POST["codearea"]

        try:
            #!orijinal standart ouput
            original_stdout = sys.stdout
            sys.stdout = open("file.txt", "w")
            exec(codeareadata)
            sys.stdout.close()
            sys.stdout = original_stdout
            output = open("file.txt", "r").read()

        except Exception as e:
            sys.stdout = original_stdout
            output = e
    return render(
        request,
        "index.html",
        {
            "code": codeareadata,
            "output": output,
        },
    )
