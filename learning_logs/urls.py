from django.urls import path
from . import views
app_name = 'learning_logs'
urlpatterns = [
    #主页
    path('', views.index, name='index'),
    #显示所有主题
    path('topics/', views.topics, name='topics'), 
    #特定页面主题
    path('topics/<int:topic_id>', views.topic, name='topic'),
    #新页面
    path('new_topic/', views.new_topic, name='new_topic'), 
    #编辑条目
    path('new_entry/<int:topic_id>', views.new_entry, name='new_entry')
]