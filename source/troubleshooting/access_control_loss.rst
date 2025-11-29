.. _troubleshooting_access_control_loss:

7.2 Access Control Loss
===========================

A. Error Case
-------------

When attempting to send motion or system commands, you may encounter the following message:

.. code-block:: bash

   [Error] Access Control Denied
   [Info] Another client currently holds control authority

This indicates that your client program cannot obtain robot control authority from the controller.

B. Root Cause Analysis
----------------------

The Doosan Robot system allows **only one active client** to have control authority at a time.  
If another process — such as **DART Studio**, **another API client**, or **RT monitoring tool** — is currently connected,  
additional clients will be denied access until the control is released.

This issue often occurs when:

- DART Studio is left connected in **Monitor or Control Mode**.  
- A previous API session did not close properly (e.g., abnormal termination).  
- Multiple applications are trying to control the same robot simultaneously.  

C. Solution
-----------

1. Open **DART Studio**, check if another connection is active.

   - Navigate to **Settings → API Control Authority**.  
   - Click **Release Control** if another client holds it.

2. If using multiple devices, ensure only one program connects to the same robot IP.

3. Restart the controller service to clear stale sessions (if necessary):

   .. code-block:: bash

      sudo systemctl restart dsr-control

4. In your client code, always release control after use:

   .. code-block:: cpp

      Drfl.release_control();
      Drfl.close_connection();

.. note::
   Only one API instance can hold authority for motion or I/O control.  
   Monitoring and logging can still be performed by other clients in parallel.
