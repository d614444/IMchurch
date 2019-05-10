from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from king.models import UserProfile
import datetime
# Register your models here.
# 
class Profileadmin(admin.StackedInline):
	model = UserProfile
	can_delete = False
	verbose_name_plural = 'UserProfile'
	fk_name = 'user'


class CustomUserAdmin(UserAdmin):
	inlines = (Profileadmin,)
	list_display = (
		'username', 'get_name', 'get_address',
		'email',  'get_birth', 'get_tel', 
		'get_christian', 'get_immember'
		)
	list_select_related = ('profile', )

	def get_birth(self, instance):
		return instance.profile.birth
	get_birth.short_description = '生日'

	def get_address(self, instance):
		return instance.profile.address
	get_address.short_description = '地址'	
	
	def get_tel(self, instance):
		return instance.profile.phone_number
	get_tel.short_description = '電話'	

	def get_name(self, instance):
		return 	instance.last_name + instance.first_name	
	get_name.short_description = '姓名'
	
	def get_age(self, instance):
		age = int((datetime.date.today() - instance.profile.birth).days / 365.25 )
		return age
	get_age.short_description = '年齡'
	
	def get_christian(self, instance):
		return instance.profile.christian
	get_christian.short_description = '是否受洗'

	def get_immember(self, instance):
		return instance.profile.immember
	get_immember.short_description = '是否為im成員'		

	def get_inline_instances(self, request, obj=None):
		if not obj:
			return list()
		return super(CustomUserAdmin, self).get_inline_instances(request, obj)
	
	
	
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)