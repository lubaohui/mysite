"""定义learning_logs的URL模式"""
from django.conf.urls import url

#句点让Python从当前的urls.py模块所在的文件夹中导入视图
from . import views

app_name = 'learning_logs'

urlpatterns = [
    # 主页
    #r 让Python将接下来的字符串视为原始字符串，而引号告诉Python正则表达式始于和终于何处
    url(r'^$', views.index, name='index'),

    #显示所有的主题
    url(r'^topics/$', views.topics, name='topics'),

    # 特定主题的详细页面
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),

]