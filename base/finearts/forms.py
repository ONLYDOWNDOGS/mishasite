from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(
        attrs={'placeholder': 'Name', 'style': 'width: 300px;'}))
    from_email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(
        attrs={'placeholder' :'Email', 'style': 'width: 300px;'}))
    subject = forms.CharField(
        required=True,
        widget=forms.TextInput(
        attrs={'placeholder': 'Subject', 'style': 'width: 300px;'}))
    message = forms.CharField(
        widget=forms.Textarea(
        attrs={'placeholder': 'Message', 'style': 'width: 500px;'}),
        required=True)
