from pythonosc import osc_message_builder
from pythonosc import udp_client

client = udp_client.UDPClient('localhost', 5005)
msg = osc_message_builder.OscMessageBuilder(address="/debug")
msg = msg.build()
print('Sending')
print(msg.dgram)
client.send(msg)

# msg.add_arg(1)
