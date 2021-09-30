from django import forms


class ContactForm(forms.Form):
    """ The class for the form sections accepting 
    user input. """

    your_email = forms.EmailField(
        required=True
    )
    subject = forms.CharField(
        required=True
    )
    message = forms.CharField(
        widget=forms.Textarea,
        required=True
    )
