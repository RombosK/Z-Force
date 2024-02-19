from django import forms


class ContactForm(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email_address = forms.EmailField(max_length=150)
    message = forms.CharField(widget=forms.Textarea,
                              max_length=2000)

# from mainapp.models import CourseFeedback


# class CourseFeedbackForm(forms.ModelForm):
#
#     class Meta:
#         model = CourseFeedback
#         fields = ['course', 'user', 'rating', 'feedback']
#         widgets = {
#             'course': forms.HiddenInput(),
#             'user': forms.HiddenInput(),
#             # 'rating': forms.RadioSelect(),
#         }
#
#     def __init__(self, *args, course=None, user=None, **kwargs):
#         super().__init__(*args, **kwargs)
#         if course and user:
#             self.fields['course'].initial = course.pk
#             self.fields['user'].initial = user.pk
