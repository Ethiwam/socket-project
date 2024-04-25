# socket-project
### A project for Computer Networking CS 4390. This was built with Python to learn server/client interaction.

### Below is the text of the quick project description I wrote for the project:

This is a quick design document for Socket Programming Project by Ethan Iwama for CS
4390 Computer Networking. I designed two programs for this project, both a client and a
server, both written in Python using the socket module.

The client is simple, the socket created for the client uses IPv4 (IF_INET) and TCP
(SOCK_STREAM) to send and receive information. It must be run each time you want to
send information to the server, it does not stay on after receiving information from the
server. This could easily be changed with a while True loop, but I thought it wasn’t
necessary to show the sending and receiving functions of the client.

The client asks the user for an integer, then sends a message to the server including both
the user’s integer and the name of the client. In the case of this project, I haven’t created it
for different users since I was focused on the sending and receiving between the client and
server. So the message is hardcoded to send the message, “Client of Ethan Iwama: {user
integer}” after getting the user’s integer. After sending the message, the client waits for the
server response, prints it to console, then terminates the client session.

The server is also straightforward. The socket created also uses IPv4 and TCP to send and
receive information, but the server will maintain the socket until told to terminate. Anytime
it receives a message from a client it does 3 things: (1) it prints that the client has
connected to itself (e.g. “Ethan Iwama has connected to Server of Ethan Iwama”), (2) it
takes the integer from the client and adds it to its own integer (my server’s number is 42
and does not change) printing the client, server, and combined numbers to terminal, and
lastly (3) terminates the server socket if the client number is less than 1 or more than 100.
The server uses regex to parse the client message for name and number, but to do so the
client message must be in the form “Client of {username}: {user number}”. The server’s
name is “Server of Ethan Iwama” and the server’s number is hardcoded as 42. When the
server receives the client number it will add it to the server number and save it as the
combined number, which will all be printed.

Below are examples of the terminals of the server and client. These were taken from the
same sessions, so each line group of lines from the client matches with the group of lines
in the server.

### Client
![Image of Client Terminal](https://github.com/Ethiwam/socket-project/blob/main/client.png)

### Server
![Image of Server Terminal](https://github.com/Ethiwam/socket-project/blob/main/server.png)

Note: I could not test with a second computer. Unfortunately at time of creation, I live in an on-campus apartment and the wifi
routers they gave us do not allow us to have two computers connect directly through IP. It
would require me to configure the routers firewall, which I do not have access to do.
