from locust import HttpUser, TaskSet, task
from lxml import etree


class SoapTestTaskSet(TaskSet):
    @task
    def test_get_user(self):
        # Define the user ID
        user_id = "123"  # Change this to a valid user ID

        # Create the SOAP envelope
        soap_envelope = etree.Element("{http://schemas.xmlsoap.org/soap/envelope/}Envelope", nsmap={
            None: "http://schemas.xmlsoap.org/soap/envelope/",
            "dat": "myapp.soap.data"
        })
        body = etree.SubElement(soap_envelope, "{http://schemas.xmlsoap.org/soap/envelope/}Body")
        get_user_request = etree.SubElement(body, "{myapp.soap.data}getUser")
        user_id_element = etree.SubElement(get_user_request, "{myapp.soap.data}user_id")
        user_id_element.text = user_id

        # Convert the SOAP envelope to a string
        body = etree.tostring(soap_envelope, pretty_print=True, xml_declaration=True, encoding='UTF-8')

        # Define the headers for the SOAP request
        headers = {
            "Content-Type": "text/plain",
            "SOAPAction": "myapp.soap.data/getUser"
        }

        # Send the SOAP request
        response = self.client.post("/",
                                    data=body,
                                    headers=headers,
                                    name="SOAP getUser request")


class SoapTestUser(HttpUser):
    tasks = [SoapTestTaskSet]
    min_wait = 500
    max_wait = 1000
