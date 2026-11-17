from django.http import HttpResponse
from django.views.generic import TemplateView
from kitchen.models import Cook, DishType, Dish


class IndexView(TemplateView):
    template_name = "kitchen/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["num_cooks"] = Cook.objects.count()
        context["num_dish_types"] = DishType.objects.count()
        context["num_dishes"] = Dish.objects.count()
        num_visits = self.request.session.get("num_visits", 0)
        num_visits += 1
        self.request.session["num_visits"] = num_visits
        context["num_visits"] = num_visits
        return context
