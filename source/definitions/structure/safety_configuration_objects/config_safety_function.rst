.. _union_CONFIG_SAFETY_FUNCTION:

CONFIG_SAFETY_FUNCTION
======================

This is a structure information to set the safety function, and consists of the following fields.
It is implemented as a **union**, allowing two different views of the same memory region:

- Bitfield view (two 4-bit workspaces per function)
- Raw byte array view (1 byte per function)

.. list-table::
   :widths: 10 26 20 8 36
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_tStopCode[SAFETY_FUNC_LAST]``
     - ``unsigned char _iStdWorkSpace:4; }`` 
       
       ``unsigned char _iColWorkSpace:4; }``
     - -
     - Refer to the Definition of Below Struct
   * - 34
     - ``_iStopCode[SAFETY_FUNC_LAST]``
     - ``unsigned char``
     - -
     - Raw 1-byte stop function value per item |br|
       Overlays the same memory as ``_tStopCode`` via union mapping. |br| |br|
       
       - SF05: Emergency Stop
       - SF06: Protective Stop
       - SF07: Standstill Monitoring 
       - SF08: Joint Angle Monitoring
       - SF09: Joint Speed Monitoring
       - SF10: Joint Torque Monitoring
       - SF11: Collision Detection
       - SF12: TCP Position Monitoring
       - SF13: TCP Orientation Monitoring
       - SF14: TCP Speed Monitoring
       - SF15: TCP Force Monitoring
       - SF16: Momentum Monitoring
       - SF17: Power Monitoring

Total size: 34 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef union _CONFIG_SAFETY_FUNCTION
   {
       struct {
           unsigned char _iStdWorkSpace : 4;  /* Standalone Workspace */
           unsigned char _iColWorkSpace : 4;  /* Collaborative Workspace */
       } _tStopCode[SAFETY_FUNC_LAST];

       unsigned char _iStopCode[SAFETY_FUNC_LAST];
   } CONFIG_SAFETY_FUNCTION, *LPCONFIG_SAFETY_FUNCTION;

.. note::
   - This union allows reading or writing either by **bitfield** or **byte** view.  
   - ``_tStopCode`` uses 17 entries (SF05–SF17), each containing two 4-bit workspace codes.  
   - ``_iStopCode`` provides direct 1-byte access for all 17 safety functions.  