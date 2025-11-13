from rest_framework.response import Response
from todo.models import Task
from .serializers import TaskSerializer
from rest_framework import permissions
from rest_framework import viewsets
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


# class TodoListView(viewsets.ModelViewSet):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer
#     permission_classes = [permissions.IsAuthenticated]

#     def list(self, request):
#         # Note the use of `get_queryset()` instead of `self.queryset`
#         queryset = self.get_queryset()
#         serializer = TaskSerializer(queryset, many=True)
#         return Response(serializer.data)

#     def get_queryset(self, *args, **kwargs):
#         return (
#             super()
#             .get_queryset(*args, **kwargs)
#             .filter(user=self.request.user)
#         )

#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)

# class TodoDetailApiView(viewsets.ModelViewSet):
#     serializer_class = TaskSerializer
#     permission_classes = [permissions.IsAuthenticated]
#     lookup_field = "todo_id"

#     def get_object(self, queryset=None):
#         obj = Task.objects.get(pk=self.kwargs["todo_id"])
#         return obj

#     def delete(self, request, *args, **kwargs):
#         object = self.get_object()
#         object.delete()
#         return Response({"detail": "successfully removed"})

#     def perform_update(self, serializer):
#         serializer.save(user=self.request.user)

#     def post(self, request, *args, **kwargs):
#         object = self.get_object()
#         serializer = TaskSerializer(
#             data=request.data, instance=object, many=False
#         )
#         if serializer.is_valid():
#             serializer.save()
#         return Response(serializer.data)
# ---------------------------------------------------------------------------------------------------------------------------------------------------

class TodoViewSet(viewsets.ModelViewSet):
    """
    A single ViewSet for viewing and editing tasks.
    Handles List, Create, Retrieve, Update, and Destroy actions.
    """
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]
    # lookup_field = 'todo_id'
# -----------------------------------------
    def get_queryset(self):

        """
        This view should return a list of all the tasks
        for the currently authenticated user.
        This single method provides security for ALL actions.
        """

        return Task.objects.filter(user=self.request.user)
# -----------------------------------------
    def perform_create(self, serializer):
        """Ensure the task is created with the logged-in user."""
        serializer.save(user=self.request.user)
# -----------------------------------------
    @swagger_auto_schema(
        operation_summary="لیست کردن تمام کارها",
        operation_description="لیستی از تمام کارهای مربوط به کاربر احراز هویت شده را برمی‌گرداند.",
        responses={200: TaskSerializer(many=True)}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
# -----------------------------------------
    @swagger_auto_schema(
        operation_summary="ایجاد یک کار جدید",
        operation_description="یک کار جدید برای کاربر فعلی ایجاد می‌کند. فیلد 'title' الزامی است.",
        request_body=TaskSerializer,
        responses={
            201: openapi.Response('با موفقیت ایجاد شد', TaskSerializer),
            400: 'اطلاعات ارسالی نامعتبر است'
        }
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
# -----------------------------------------
    @swagger_auto_schema(
        operation_summary="دریافت جزئیات یک کار",
        operation_description="جزئیات کامل یک کار مشخص را با استفاده از ID آن برمی‌گرداند.",
        responses={
            200: TaskSerializer,
            404: "موردی یافت نشد"
        }
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
# -----------------------------------------
    @swagger_auto_schema(
        operation_summary="بروزرسانی کامل یک کار",
        operation_description="یک کار موجود را به طور کامل بروزرسانی می‌کند (متد PUT).",
        request_body=TaskSerializer,
        responses={
            200: TaskSerializer,
            400: 'اطلاعات ارسالی نامعتبر است',
            404: "موردی یافت نشد"
        }
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
# -----------------------------------------
    @swagger_auto_schema(
        operation_summary="بروزرسانی بخشی از یک کار",
        operation_description="یک یا چند فیلد از یک کار موجود را بروزرسانی می‌کند (متد PATCH).",
        request_body=TaskSerializer,
        responses={
            200: TaskSerializer,
            400: 'اطلاعات ارسالی نامعتبر است',
            404: "موردی یافت نشد"
        }
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)
# -----------------------------------------
    @swagger_auto_schema(
        operation_summary="حذف یک کار",
        operation_description="یک کار موجود را با استفاده از ID آن حذف می‌کند.",
        responses={
            204: "مورد با موفقیت حذف شد (No Content)",
            404: "موردی یافت نشد"
        }
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
# -------------------------------------------------------------------------------------------------------------------------------------------------    