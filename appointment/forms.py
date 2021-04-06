from django import forms
from .models import Appointment, TakeAppointment, PatientPrescription
from accounts.models import User

class CreateAppointmentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CreateAppointmentForm, self).__init__(*args, **kwargs)
        self.fields['full_name'].label = "Full Name"
        self.fields['image'].label = "Image"
        self.fields['department'].label = "Department"
        self.fields['start_time'].label = "Start Time"
        self.fields['hospital_name'].label = "Hospital Name"
        self.fields['qualification_name'].label = "Qualification"
        self.fields['institute_name'].label = "Institute"

        self.fields['full_name'].widget.attrs.update(
            {
                'placeholder': 'Enter Full Name',
            }
        )

        self.fields['department'].widget.attrs.update(
            {
                'placeholder': 'Select Your Service',
            }
        )

        self.fields['start_time'].widget.attrs.update(
            {
                'placeholder': 'Ex : 9 AM',
            }
        )
        self.fields['end_time'].widget.attrs.update(
            {
                'placeholder': 'Ex: 5 PM',
            }
        )
        self.fields['location'].widget.attrs.update(
            {
                'placeholder': 'Ex : Ahmedabad, Gujarat',
            }
        )

        self.fields['hospital_name'].widget.attrs.update(
            {
                'placeholder': 'Enter Hospital Name',
            }
        )

        self.fields['qualification_name'].widget.attrs.update(
            {
                'placeholder': 'Ex : MBBS, BDS',
            }
        )

        self.fields['institute_name'].widget.attrs.update(
            {
                'placeholder': 'Ex : DMC',
            }
        )

    class Meta:
        model = Appointment
        fields = ['full_name', 'image', 'department', 'start_time', 'end_time', 'location',
                  'hospital_name', 'qualification_name', 'institute_name']

    def is_valid(self):
        valid = super(CreateAppointmentForm, self).is_valid()

        # if already valid, then return True
        if valid:
            return valid
        return valid

    def save(self, commit=True):
        appointment = super(CreateAppointmentForm, self).save(commit=False)
        if commit:
            appointment.save()
        return appointment


class TakeAppointmentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(TakeAppointmentForm, self).__init__(*args, **kwargs)
        self.fields['appointment'].label = "Choose Your Doctor"
        self.fields['full_name'].label = "Full Name"
        self.fields['phone_number'].label = "Phone Number"
        self.fields['message'].label = "Message"

        self.fields['appointment'].widget.attrs.update(
            {
                'placeholder': 'Choose Your Doctor',
            }
        )

        self.fields['full_name'].widget.attrs.update(
            {
                'placeholder': 'Write Your Name',
            }
        )

        self.fields['phone_number'].widget.attrs.update(
            {
                'placeholder': 'Enter Phone Number',
            }
        )
        self.fields['message'].widget.attrs.update(
            {
                'placeholder': 'Write a short message',
            }
        )

    class Meta:
        model = TakeAppointment
        fields = ['appointment', 'full_name', 'phone_number', 'message']

    def is_valid(self):
        valid = super(TakeAppointmentForm, self).is_valid()

        # if already valid, then return True
        if valid:
            return valid
        return valid

    def save(self, commit=True):
        appointment = super(TakeAppointmentForm, self).save(commit=False)
        if commit:
            appointment.save()
        return appointment


class PrescriptionForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PrescriptionForm, self).__init__(*args, **kwargs)
        self.fields['appointment'].label = "Choose Your Patient"
        self.fields['full_name'].label = "Full Name"
        self.fields['pres_message'].label = "Pres Message"

        self.fields['appointment'].widget.attrs.update(
            {
                'placeholder': 'Choose Your Patient',
            }
        )

        self.fields['full_name'].widget.attrs.update(
            {
                'placeholder': 'Write Your Name',
            }
        )

        self.fields['pres_message'].widget.attrs.update(
            {
                'placeholder': 'Provide a prescription message',
            }
        )

    class Meta:
        model = PatientPrescription
        fields = ['appointment', 'full_name', 'pres_message']

    def is_valid(self):
        valid = super(PrescriptionForm, self).is_valid()

        # if already valid, then return True
        if valid:
            return valid
        return valid

    def save(self, commit=True):
        prescription = super(PrescriptionForm, self).save(commit=False)
        if commit:
            prescription.save()
        return prescription
