from django.shortcuts import render, redirect
from app.models import Link


def creating_view(request):
    if request.method == "POST":
        url = request.POST["url"]
        link = Link.shorten(url)
        if link is None:
            return render(
                request, "app/create.html", {"invalid_url": True}, status=422)
        else:
            return redirect('app:show', link.short_code)
    return render(
        request,
        'app/create.html',
    )


def showing(request, short_code):
    return render(request, "app/show.html",
                  {'link': Link.find_by_short_code(short_code)})


def go_to(request, short_code):
    page = Link.find_by_short_code(short_code)
    if page is None:
        return redirect("app:create")
    else:
        return redirect(page.original)
