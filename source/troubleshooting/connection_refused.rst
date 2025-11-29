.. _troubleshooting_connection_refused:

7.1 Connection Refused (API Link Error)
============================================

This issue occurs when the API fails to establish a connection with the robot controller or emulator.

A. Error Case
----------------

During initialization, the following error message may appear:

.. code-block:: bash

   [Error] Connection refused by host
   [Info] Failed to connect to 192.168.137.100:12345

B. Root Cause Analysis
----------------------

This error typically indicates one of the following:

- The **DART Platform** or **Emulator** is not running. (in virtual mode)
- The **target IP address** or **port** is incorrect.
- A **firewall** or **VPN** is blocking the connection.

C. Solution
-----------

1. Start the **DART Platform** or **Emulator** before running your API program.  
2. Verify the robot IP configuration in your code:

   .. code-block:: cpp

      Drfl.open_connection("192.168.137.100");

3. Confirm network access with ping or netcat:

   .. code-block:: bash

      ping 192.168.137.100
      nc -zv 192.168.137.100 12345

4. If running on a company network, check internal firewall settings.
5. Disable any active VPNs that may interfere with local network connections.
6. Ensure no other applications are using the same port (12345/TCP).
7. Restart your PC and robot controller/emulator to clear any stale network states.
