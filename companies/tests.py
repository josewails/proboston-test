import json

from django.test import TestCase

from faker import Faker

fake = Faker()


class TestCompanies(TestCase):

    def test_company_create(self):
        # test a non-valid ares won't work

        url = "/"

        data = dict(
            name=fake.name(),
            email=fake.email(),
            ico="fadfksdf"
        )

        response = self.client.post(url, data=data)
        json_response = json.loads(response.content.decode('utf-8'))

        self.assertEqual(json_response["success"], False)

        # test a valid ares will work

        data.update(dict(ico="68407700"))

        response = self.client.post(url, data)
        json_response = json.loads(response.content.decode("utf-8"))
        self.assertEqual(json_response["success"], True)
