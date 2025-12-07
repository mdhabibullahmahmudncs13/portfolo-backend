from django.contrib.auth import get_user_model
User = get_user_model()
try:
    user = User.objects.get(username='admin')
    user.set_password('admin123')
    user.save()
    print('Password set successfully for admin user')
except User.DoesNotExist:
    print('Admin user not found')
