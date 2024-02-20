<tytle>NMAP SCRIPT</tytle>
<h1>Introduction:</h1>

<p>The script provides an efficient tool for port enumeration in a network, simplifying the process of discovering and analyzing services on connected devices. Unlike more complex tools like nmap, this script is designed to be straightforward and user-friendly, allowing users to quickly scan a network and obtain detailed information about open and filtered ports on a specific IP. Additionally, it offers the option to delve deeper into information about open ports, providing details such as state, service, product, version, and more.</p>
<h1>Installation Guide:</h1>

<h2>Clone the Repository:</h2>
<p>Clone the repository from GitHub using the following command:</p>

    git clone https://github.com/Tonyalg/Nmap-Script.git

<h2>Prerequisites:</h2>

<p>Ensure you have Python installed on your system. If not, you can download it from <a href="https://www.python.org/">python.org.</a></p>
<p>Install the nmap module using pip:</p>

    pip install python-nmap

<h1>Running the Script:</h1>

Navigate to the directory where you cloned the repository.
Execute the port_enumeration.py script using Python:

    python escaner.py

<p>Using the Script:
  -  Enter the network IP you want to scan when prompted.
  -  Select the specific IP for port enumeration.
  -  The script will display the open and filtered ports on the selected IP.
  -  If you want to get more information about open ports, respond "Y" when prompted.
  -  The script will provide detailed information about the open ports, including state, service, product, version, and more.</p>

<p>With this simple guide, you can use the script to perform a quick and detailed enumeration of ports in your network, thereby facilitating administration and security tasks.</p>
