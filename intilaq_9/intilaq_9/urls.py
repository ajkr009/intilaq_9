import sys
import os
from django.contrib import admin
from django.urls import path, include

# പൈത്തൺ പാത്തിലേക്ക് ഈ ഫോൾഡർ കൂടി ചേർക്കുന്നു (ഇത് എറർ വരുന്നത് തടയും)
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# ഇനി നേരിട്ട് views ഇമ്പോർട്ട് ചെയ്യാം
import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('fun/', views.fun_page, name='fun_page'),
]
