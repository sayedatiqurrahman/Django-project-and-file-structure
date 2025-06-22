from django.contrib import admin
from .models import AppVariety, AppReview,AppStore,AppCertificates



# Register your models here.
class AppReviewInline(admin.TabularInline):
    model = AppReview
    extra = 1

class AppVarietyAdmin(admin.ModelAdmin):
    list_display= ('name', 'app_type', 'date_added', 'is_active', 'price')
    inlines= [AppReviewInline]

class AppStoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'mother_company', 'contact_number', 'email')
    filter_horizontal = ['app_varieties']


class AppCertificateAdmin(admin.ModelAdmin):
    list_display= ('app','certificate_name','certificate_number','issued_by','issue_date','expiry_date')

admin.site.register(AppVariety, AppVarietyAdmin)
# admin.site.register(AppReview, AppReviewInline)
admin.site.register(AppStore, AppStoreAdmin)
admin.site.register(AppCertificates, AppCertificateAdmin)
