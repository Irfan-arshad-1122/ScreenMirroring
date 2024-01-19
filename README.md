**Wireless Screen Sharing Application**

**Overview**
This project implements a simple wireless screen sharing application using Python and PyQt5 for the GUI. The application consists of two parts: a server application that captures the screen and sends images to connected clients, and a client application that receives and displays the shared screen.

**Features**

**Server Application:**

Captures the screen using the Pillow library.

Sends screen images to connected clients over a socket connection.

Supports multiple clients.

**Client Application:**

Connects to the server using the server's IP address and port.

Displays the shared screen in real-time.

**Requirements**

Python 3.x

PyQt5

Pillow (PIL)

**How to Run**

**Server:**

Run the server script on the machine where you want to share the screen.

bash

Copy code

python server.py

The server will start listening on a specified port.

**Client:**

Run the client script on the machine where you want to view the shared screen.

bash

Copy code

python client.py

Enter the IP address of the server and connect.

pip install PyQt5 Pillow


**Known Issues**

Currently, the application might encounter connection issues due to network conditions or firewall settings. Ensure that the necessary ports are open and the firewall allows communication.

**License**

This project is licensed under the MIT License.

**Author**
**Irfan Arshad**
