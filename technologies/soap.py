from spyne import Application, rpc, ServiceBase, Iterable, Integer, String
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from wsgiref.simple_server import make_server


class WeatherService(ServiceBase):
    @rpc(String, _returns=String)
    def getWeatherForecast(ctx, city):
        # Print the incoming request data (Note: ctx.in_object is used to get the raw input object)
        print(f"Received request for city: {city}")
        # Here you'd implement your logic to get the weather forecast
        return f"The weather in {city} is sunny with a high of 27 degrees Celsius."


# Creating a SOAP application
application = Application([WeatherService],
                          tns='myapp.soap.weather',
                          in_protocol=Soap11(validator='lxml'),
                          out_protocol=Soap11())

# Deploy the application using a WSGI server
if __name__ == '__main__':
    server = make_server('127.0.0.1', 8000, WsgiApplication(application))
    print("SOAP service is running...")

    # The WSDL can be accessed at http://127.0.0.1:8000/?wsdl
    print("WSDL is at: http://127.0.0.1:8000/?wsdl")

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.shutdown()
