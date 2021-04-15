from django.test import TestCase
from . models import Appointment,TakeAppointment
from django.core.files import File
# Create your tests here.
class CreateAppointmentTesting(TestCase):
     def setUp(self):
         self.appointment = Appointment.objects.create(full_name='MD.Will Smith',location='Ahmedabad,Gujarat',start_time='9 AM', end_time='5 PM',qualification_name='MBBS',institute_name='Ganpat University', hospital_name='CIMS', department='Cardiology')

     def test_appointment_model(self):
         a = self.appointment
         self.assertTrue(isinstance(a,Appointment))

class TakeAppointmentTestting(TestCase):
    def setUp(self):
        self.appointment = TakeAppointment.objects.create(full_name='Kush Patel',message='fever',phone_number='9106678088')
        return
    def test_takeappointment_model(self):
        b = self.appointment
        self.assertEqual(str(b),'Kush Patel')

class URLTests(TestCase):
    def test_testhomepage(self):
        response_home = self.client.get('/')

        self.assertEqual(response_home.status_code,200)
    def test_testservciepage(self):
        response_service = self.client.get('/service')
        self.assertEqual(response_service.status_code,200)
# comment unshallow