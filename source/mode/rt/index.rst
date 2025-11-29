.. _rt_stream:

3.4 RT Stream
===================================
Real-Time modes provide a high-speed communication interface that enables external systems to control 
the robot with minimal latency. RT Stream supports continuous trajectory updates, force-feedback loops, 
external sensor fusion, and other time-critical operations that require deterministic data exchange.

It offers a structured channel for transmitting real-time motion commands, receiving state information, 
and monitoring diagnostics at high frequency. RT Stream is widely used in advanced research, adaptive control, 
and precision applications where standard Auto Mode execution is not sufficient. This section describes the RT session workflow, schema versions, data I/O format, command handling, and diagnostics—core components for implementing real-time external control.

.. toctree::
   :maxdepth: 1

   create_destroy/create_destroy
   session_lifecycle/session_lifecycle
   schema_version/schema_version
   data_io/data_io
   command_control/command_control
   diagnostics_callbacks/diagnostics_callbacks