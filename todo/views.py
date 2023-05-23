from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        
        # Filter by status
        status = self.request.query_params.get('status')
        if status:
            queryset = queryset.filter(status=status)
        
        # Filter by priority
        priority = self.request.query_params.get('priority')
        if priority:
            queryset = queryset.filter(priority=priority)
        
        # Filter by title (fulltext search)
        title = self.request.query_params.get('title')
        if title:
            queryset = queryset.filter(title__icontains=title)
        
        # Sort by creation time or priority
        sort_by = self.request.query_params.get('sort_by')
        if sort_by == 'creation_time':
            queryset = queryset.order_by('created_at')
        elif sort_by == 'priority':
            queryset = queryset.order_by('priority')
        
        return queryset

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        
        # Check if the task has uncompleted subtasks
        if not instance.can_be_completed():
            return Response({'error': 'Cannot delete task with uncompleted subtasks.'}, status=status.HTTP_400_BAD_REQUEST)
        
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=True, methods=['patch'])
    def mark_as_done(self, request, pk=None):
        task = self.get_object()
        
        # Check if the task has uncompleted subtasks
        if not task.can_be_completed():
            return Response({'error': 'Cannot mark task as done. Subtasks are incomplete.'}, status=status.HTTP_400_BAD_REQUEST)
        
        task.status = 'done'
        task.save()
        return Response({'message': 'Task marked as done.'}, status=status.HTTP_200_OK)