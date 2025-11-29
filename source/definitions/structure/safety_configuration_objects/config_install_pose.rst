.. _struct_CONFIG_INSTALL_POSE:

CONFIG_INSTALL_POSE
===================

This is a structure information to set the install pose,  
and consists of the following fields.

.. list-table::
   :widths: 10 28 18 8 36
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_fGradient``
     - ``float``
     - -
     - Gradient of robot base on the ground (tilt or incline angle)
   * - 4
     - ``_fRotation``
     - ``float``
     - -
     - Rotation angle of robot base about the vertical axis

Total size: 8 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _CONFIG_INSTALL_POSE
   {
       /* robot gradient on ground */
       float _fGradient;
       /* robot rotation angle */
       float _fRotation;
   } CONFIG_INSTALL_POSE, *LPCONFIG_INSTALL_POSE;