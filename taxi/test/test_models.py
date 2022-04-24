from django.contrib.auth import get_user_model
from django.test import TestCase

from taxi.models import Manufacturer, Car


class ModelsTests(TestCase):

    def test_model_manufacturer_str(self):
        name = Manufacturer.objects.create(name="ford", country="USA")

        self.assertEqual(str(name), "ford USA")

    def test_client_license_number(self):
        driver = get_user_model().objects.create_user(
            username='test',
            password='test',
            license_number='RTB12345'
        )

        self.assertEqual(driver.license_number, 'RTB12345')

    def test_car_creation(self):
        manufacturer = Manufacturer.objects.create(name="ford", country="USA")
        driver = get_user_model().objects.create_user(
            username='test',
            password='test',
        )

        car = Car.objects.create(
            model="test",
            manufacturer=manufacturer,
        )
        car.drivers.add(driver)

        self.assertEqual(*car.drivers.all(), driver)


