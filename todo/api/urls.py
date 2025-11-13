from rest_framework.routers import DefaultRouter
# from .views import TodoListView, TodoDetailApiView
from .views import TodoViewSet

router = DefaultRouter()
router.register("task-list", TodoViewSet, basename="task_list")
# router.register(
#     "task-detail",
#     TodoDetailApiView,
#     basename="task_detail",
# )

urlpatterns = []

urlpatterns += router.urls
