.. _struct_MOVE_MOVELISSAJOUS:

MOVE_MOVELISSAJOUS
==================

This structure defines the parameters for generating a **Lissajous motion path**,  
a complex oscillatory trajectory produced by combining two sinusoidal signals  
on orthogonal planes (XY, YZ, or ZX).

.. list-table::
   :widths: 10 30 18 8 34
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_iMotionType``
     - ``unsigned char``
     - 0~2
     - Target motion axis (0: X, 1: Y, 2: Z)
   * - 1
     - ``_iPlaneType``
     - ``unsigned char``
     - 0~2
     - Plane selection (0: XY, 1: YZ, 2: ZX)
   * - 2
     - ``_iTargetRef``
     - ``unsigned char``
     - 0~1
     - Reference coordinate (0: Base, 1: Tool)
   * - 3
     - ``_fTargetAcc``
     - ``float``
     - -
     - Acceleration time (sec)
   * - 7
     - ``_fAmplitude``
     - ``float``
     - -
     - Amplitude (mm)
   * - 11
     - ``_fFrequency``
     - ``float``
     - -
     - Oscillation frequency (Hz)
   * - 15
     - ``_iRepeatCount``
     - ``unsigned int``
     - -
     - Number of repetitions
   * - 19
     - ``_iTargetAsyn``
     - ``unsigned char``
     - 0~1
     - Motion synchronization flag |br|  
       (0: Sync, 1: Async)

Total size: 20 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _MOVE_MOVELISSAJOUS
   {
       /* X:0, Y:1, Z:2 */
       unsigned char _iMotionType;
       /* XY:0, YZ:1, ZX:2 */
       unsigned char _iPlaneType;
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
   } MOVE_MOVELISSAJOUS, *LPMOVE_MOVELISSAJOUS;

.. note::
   - The **MOVE_MOVELISSAJOUS** command generates **Lissajous curve** motion  
     by combining two sinusoidal signals on orthogonal planes.  
   - It is useful for pattern generation and oscillation testing.  
   - When ``_iTargetAsyn = 1``, motion runs asynchronously across the selected axes.
