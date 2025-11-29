.. _struct_CONVEYOR_OBJECT:

CONVEYOR_OBJECT
===============

This structure defines an **object tracked on the conveyor**,  
including its identifier, timeout, container type, and position.  
It is primarily used in robot–conveyor coordination for pick & place operations.

.. list-table::
   :widths: 10 28 22 8 32
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_iConId``
     - ``unsigned char``
     - 0~255
     - Conveyor identifier index
   * - 1
     - ``_tTimeout``
     - ``float``
     - -
     - Timeout threshold (seconds) for conveyor operation
   * - 5
     - ``_iContainerType``
     - ``unsigned char``
     - 0~1
     - **Container organization type** |br|
       0: FIFO |br|
       1: LIFO
   * - 6
     - ``_tPosObjCoord``
     - :ref:`POSITION <struct_POSITION>`
     - -
     - Object position in conveyor coordinate frame

Total size: 30 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _CONVEYOR_OBJECT
   {
       /* Conveyor ID (index) */
       unsigned char _iConId;

       /* Timeout threshold (seconds) */
       float _tTimeout;

       /* Container type (0: FIFO, 1: LIFO) */
       unsigned char _iContainerType;

       /* Object position in conveyor coordinate frame */
       POSITION _tPosObjCoord;

   } CONVEYOR_OBJECT, *LPCONVEYOR_OBJECT;
