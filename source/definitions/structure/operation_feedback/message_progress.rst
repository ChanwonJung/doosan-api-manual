.. _struct_MESSAGE_PROGRESS:

MESSAGE_PROGRESS
================

This is a structure information to provide information on the current progress  
when the robot controller executes the DRL program, and consists of the following fields.

.. list-table::
   :widths: 10 28 18 8 36
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_iCurrentCount``
     - ``unsigned char``
     - -
     - Current progress step(progress information)
   * - 1
     - ``_iTotalCount``
     - ``unsigned char``
     - -
     - Total progress step count(progress information)

Total size: 2 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _MESSAGE_PROGRESS
   {
       unsigned char _iCurrentCount;  /* current step */
       unsigned char _iTotalCount;    /* total step */
   } MESSAGE_PROGRESS, *LPMESSAGE_PROGRESS;