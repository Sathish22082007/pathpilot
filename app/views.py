import requests
from django.shortcuts import redirect

from django.shortcuts import render, redirect


def home(request):
    """Landing page with resume upload form."""
    return render(request, "landing.html")


def dashboard(request):
    data = request.session.get("result", {})

    print("🔥 DASHBOARD DATA:", data)

    return render(request, "dashboard.html", data)


import requests

import requests

import requests
from django.shortcuts import render, redirect

def home(request):
    return render(request, "landing.html")


import requests
from django.shortcuts import redirect

import requests
from django.shortcuts import redirect

def analyze(request):
    if request.method == "POST":
        resume_file = request.FILES.get("resume")
        goal = request.POST.get("goal")

        try:
            response = requests.post(
                "http://localhost:5678/webhook/career-guidance",
                files={
                    "data": (
                        resume_file.name,
                        resume_file.read(),
                        resume_file.content_type
                    )
                },
                data={"goal": goal}
            )

            # 🔥 DEBUG START
            print("🔥 RAW RESPONSE:", response.text)

            data = response.json()
            print("🔥 PARSED JSON:", data)

            # 🔥 DEBUG END

        except Exception as e:
            print("❌ ERROR:", e)
            data = {}

        # 🔥 STORE SESSION
        request.session["result"] = data
        print("🔥 SESSION STORED:", request.session["result"])

        return redirect("/dashboard/")

    return redirect("/")
3