from django.shortcuts import render, redirect
from app.models import Link
from django.views import View


class Create(View):
    def post(self, request):
        url = request.POST["url"]
        link = Link.shorten(url)
        if link is None:
            return render(
                request, "app/create.html", {"invalid_url": True}, status=422)
        else:
            return redirect('app:show', link.short_code)

    def get(self, request):
        return render(
            request,
            'app/create.html',
        )


class Show(View):
    def get(self, request, short_code):
        return render(request, "app/show.html",
                      {'link': Link.find_by_short_code(short_code)})


class Goto(View):
    def get(self, request, short_code):
        page = Link.find_by_short_code(short_code)
        if page is None:
            return redirect("app:create")
        else:
            return redirect(page.original)
