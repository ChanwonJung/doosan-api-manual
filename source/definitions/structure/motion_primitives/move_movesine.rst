.. _struct_MOVE_MOVESINE:

MOVE_MOVESINE
==============

This structure defines the parameters for **sinusoidal motion** of a single axis.  
It is used to generate smooth oscillatory motion along one direction (X, Y, or Z)  
in either the **base** or **tool** coordinate frame.

.. list-table::
   :widths: 10 30 18 8 34
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_iTargetAxs``
     - ``unsigned char``
     - 0~2
     - Target axis (0: X, 1: Y, 2: Z)
   * - 1
     - ``_iTargetRef``
     - ``unsigned char``
     - 0~1
     - Reference coordinate (0: Base, 1: Tool)
   * - 2
     - ``_fTargetAcc``
     - ``float``
     - -
     - Acceleration time (sec)
   * - 6
     - ``_fAmplitude``
     - ``float``
     - -
     - Motion amplitude (mm)
   * - 10
     - ``_fFrequency``
     - ``float``
     - -
     - Oscillation frequency (Hz)
   * - 14
     - ``_iRepeatCount``
     - ``unsigned int``
     - -
     - Number of sine repetitions
   * - 18
     - ``_iTargetAsyn``
     - ``unsigned char``
     - 0~1
     - Motion synchronization flag |br|  
       (0: Sync, 1: Async)

Total size: 19 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _MOVE_MOVESINE
   {
       /* X:0, Y:1, Z:2 */
       unsigned char _iTargetAxs;
       /* Base:0, Tool:1 */
       unsigned char _iTargetRef;
       /* Acceleration time */
       float _fTargetAcc;
       /* Sinusoidal amplitude (mm) */
       float _fAmplitude;
       /* Sinusoidal frequency (Hz) */
       float _fFrequency;
       /* Repeat count */
       unsigned int _iRepeatCount;
       /* 0: Sync, 1: Async */
       unsigned char _iTargetAsyn;
   } MOVE_MOVESINE, *LPMOVE_MOVESINE;

.. note::
   - The **MOVE_MOVESINE** command creates an oscillatory trajectory along a single axis.  
   - Use the ``_iTargetRef`` flag to define whether the motion occurs in the **Base** or **Tool** frame.  
   - When ``_iTargetAsyn = 1``, the motion runs asynchronously from other axes.
