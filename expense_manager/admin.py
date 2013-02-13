from django.contrib import admin
from models import *


class AndroidMetadataAdmin(admin.ModelAdmin):
	list_display = [f.name for f in AndroidMetadata._meta.fields] + ['__unicode__']


class ExpenseBudgetAdmin(admin.ModelAdmin):
	list_display = [f.name for f in ExpenseBudget._meta.fields] + ['__unicode__']


class ExpenseCategoryAdmin(admin.ModelAdmin):
	list_display = [f.name for f in ExpenseCategory._meta.fields] + ['__unicode__']


class ExpenseNoteAdmin(admin.ModelAdmin):
	list_display = [f.name for f in ExpenseNote._meta.fields] + ['__unicode__']


class ExpensePayeePayerAdmin(admin.ModelAdmin):
	list_display = [f.name for f in ExpensePayeePayer._meta.fields] + ['__unicode__']


class ExpensePreferenceAdmin(admin.ModelAdmin):
	list_display = [f.name for f in ExpensePreference._meta.fields] + ['__unicode__']


class ExpenseRepeatingAdmin(admin.ModelAdmin):
	list_display = [f.name for f in ExpenseRepeating._meta.fields] #+ ['__unicode__']


class ExpenseReportAdmin(admin.ModelAdmin):
	list_display = [f.name for f in ExpenseReport._meta.fields] + ['__unicode__']


admin.site.register(AndroidMetadata, AndroidMetadataAdmin)
admin.site.register(ExpenseBudget, ExpenseBudgetAdmin)
admin.site.register(ExpenseCategory, ExpenseCategoryAdmin)
admin.site.register(ExpenseNote, ExpenseNoteAdmin)
admin.site.register(ExpensePayeePayer, ExpensePayeePayerAdmin)
admin.site.register(ExpensePreference, ExpensePreferenceAdmin)
admin.site.register(ExpenseRepeating, ExpenseRepeatingAdmin)
admin.site.register(ExpenseReport, ExpenseReportAdmin)
