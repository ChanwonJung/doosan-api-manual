1.4 Realtime External Control
==============================

Real-time External Control is a UDP/IP-based communication api for 
users who want to directly control the robot arm from an 
external PC through the Doosan controller. 

.. figure:: /tutorials/images/introduction/realtime_udp.png
   :alt: realtime_udp
   :width: 80%
   :align: center

   Realtime UDP Communication

.. raw:: html
      
   <br>      

It operates independently of the existing TCP/IP-based communication 
api, and sends and receives input data (external controller →  robot controller) 
and output data (robot controller →  external controller) required for real-time control 
up to 1 kHz at a set period, and separately you can send servo control 
commands (servoj_rt, servol_rt, speedj_rt, speedl_rt, torque_rt).

.. note::
   While the RT channel supports high-speed communication up to 1 kHz,
   the standard TCP/IP API operates at a slower cycle: **20 kHz on earlier version of the DRCF, and 50 kHz on DRCF version 3.5 or later.**

.. toctree::
   :maxdepth: 2

   version