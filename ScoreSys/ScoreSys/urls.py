"""ScoreSys URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from score.views import IndexView, ReusltView, InserDataView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('index/', IndexView.as_view(), name="index"),  # 首页
                  path('insert/', InserDataView.as_view(), name="inser_data"),  # 插入数据
                  path('result/', ReusltView.as_view(), name="result"),  # 结果页

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
