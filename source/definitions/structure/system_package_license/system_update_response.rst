.. _struct_SYSTEM_UPDATE_RESPONSE:

SYSTEM_UPDATE_RESPONSE
======================

This structure contains the update process status of the robot system, including both the overall update state and per-axis inverter update results.

.. list-table::
   :widths: 10 25 15 10 40
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_iProcess``
     - ``unsigned char``
     - 0 ~ 2
     - 0: Updating |br| 
       1: Completed |br|
       2: Fail
   * - 1
     - ``_iInverter``
     - ``unsigned char[NUM_AXIS]``
     - 0 ~ 100
     - **Inverter update status per axis** |br| 
       0: Non-update |br| 
       1: Update |br| 
       2: Success |br| 
       3: Fail |br| 
       **Safety Controller (CPU A/B)**: 0-100

Total size: 7 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _SYSTEM_UPDATE_RESPONSE
   {
       /* updating: 0, completed: 1 fail: 2*/
       unsigned char               _iProcess;
       /* inverter : non-update: 0, update: 1, sucess: 2, fail: 3*/
       /* safety controller(CPUA / B) : 0 - 100 */
       unsigned char               _iInverter[NUM_AXIS];
   } SYSTEM_UPDATE_RESPONSE, *LPSYSTEM_UPDATE_RESPONSE;
