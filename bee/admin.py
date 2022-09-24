from django.contrib import admin
from .models import *

class InfoAdmin(admin.ModelAdmin):
	list_display = ('id', 'info_title', 'info_text', 'info_image')
	list_display_links = ('id', 'info_title', 'info_image')
	search_fields = ('info_title', 'info_text')

class MarafonAdmin(admin.ModelAdmin):
	list_display = ('id', 'marafon_name', 'marafon_tiers', 'total_place', 'marafon_desc')
	list_display_links = ('id', 'marafon_name')
	search_fields = ('marafon_name', 'marafon_tiers')
	prepopulated_fields = {'slug': ('marafon_name',)}

class FaqAdmin(admin.ModelAdmin):
	list_display = ('id', 'text_ask', 'text_answer')
	list_display_links = ('id', 'text_answer')
	search_fields = ('text_ask', 'text_answer')

class SponsorAdmin(admin.ModelAdmin):
	list_display = ('id', 'title_sponsor', 'desc_sponsor', 'url_image', 'link')
	list_display_links = ('id', 'title_sponsor', 'url_image')
	search_fields = ('title_sponsor', 'desc_sponsor')





admin.site.register(Info, InfoAdmin)
admin.site.register(Marafon, MarafonAdmin)
admin.site.register(Faq, FaqAdmin)
admin.site.register(Sponsor, SponsorAdmin)

