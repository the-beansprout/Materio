from django.urls import path
from .views import DashboardsView

from .views import (
    PieCountbySeverity,
    LineCountbyMonth,
    MultilineIncidentTop3Country,
    multipleBarbySeverity,)

# urlpatterns = [
#     path(
#         "",
#         DashboardsView.as_view(template_name="dashboard_analytics.html"),
#         name="index",
#     )
# ]

urlpatterns = [
    # charts
    path('', DashboardsView.as_view(template_name="dashboard_analytics.html"), name="index"),
    path('dashboard/analytics/', DashboardsView.as_view(template_name="dashboard_analytics.html"), name='dashboard-chart'),
    path("chart/", PieCountbySeverity, name="chart"),
    path("lineChart/", LineCountbyMonth, name="chart"),
    path("multilineChart/", MultilineIncidentTop3Country, name="chart"),
    path("multiBarChart/", multipleBarbySeverity, name="chart"),
    ]