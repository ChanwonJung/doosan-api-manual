.. _API_architectures:

1.2.1 API Layer Architecture
------------------------------------------

The **API Layer** of the Doosan Robotics Framework Library (DRFL) is composed of four hierarchical header files:
**DRFC**, **DRFS**, **DRFL**, and **DRFLEx**.

These headers define all constants, data structures, core APIs, and extended functionalities required for robot control
and communication between the user application and the controller.

DRFC.h
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Constant Layer**

Defines all global constants, enumerations, and macros used across the API.  
This includes motion types, robot states, I/O modes, and safety levels.  
It serves as the foundational definition file referenced by all higher layers.

DRFS.h
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Structure Layer**

Declares all data structures exchanged between the API and the robot controller.  
It includes monitoring data (``ROBOT_MONITORING_DATA_EX``), configuration structures
such as ``CONFIG_TOOL`` and ``CONFIG_SAFETY_ZONE``, as well as position and joint representations.  
This file ensures consistent data formatting and interoperability across all robot models.

DRFL.h
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Core API Layer**

Provides the main interface functions exposed to users, including motion commands (``movej()``, ``movel()``),
I/O operations (``set_digital_output()``), and system controls (``start_robot()``, ``manage_access_control()``).  
It references constants and structures defined in ``DRFC`` and ``DRFS`` to process requests and communicate with the robot controller.

DRFLEx.h
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Extension Layer**
 
Offers extended and high-level APIs built upon ``DRFL``.  
This layer supports advanced capabilities such as motion blending, asynchronous callbacks, and sequence automation,  
enabling developers to create complex and user-friendly robotic applications.

    .. image:: /tutorials/images/introduction/api_architecture_components.png
        :alt: api_architecture
        :width: 100%
        :align: center
