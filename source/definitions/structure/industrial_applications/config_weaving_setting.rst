.. _struct_CONFIG_WEAVING_SETTING:

CONFIG_WEAVING_SETTING
======================

This structure defines the **generic weaving configuration** for welding.  
It supports trapezoid-style and circular (Lissajous-like) patterns via a detail **union**.

.. list-table::
   :widths: 10 28 22 8 32
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_iType``
     - ``unsigned char``
     - -
     - Weaving type selector (e.g., trapezoid vs. circular)
   * - 4
     - ``_fOffsetY``
     - ``float``
     - mm
     - Weaving offset along Y
   * - 8
     - ``_fOffsetZ``
     - ``float``
     - mm
     - Weaving offset along Z
   * - 12
     - ``_fGradient``
     - ``float``
     - -
     - Weaving gradient (tilt)
   * - 16
     - ``_tDetail``
     - ``union{ _tTrap | _tCirc | _szBuffer }``
     - -
     - Pattern-specific parameters (see below)

Total size: 64 bytes

**Detail union**

- **Trapezoid** (``_tTrap``)

  .. list-table::
     :widths: 12 28 22 10 28
     :header-rows: 1

     * - **BYTE#**
       - **Field Name**
       - **Data Type**
       - **Value**
       - **Remarks**
     * - 16
       - ``_tDetail._tTrap._tPoint1``
       - :ref:`POINT_2D <struct_POINT_2D>`
       - -
       - Corner point #1 (X,Y)
     * - 24
       - ``_tDetail._tTrap._tPoint2``
       - :ref:`POINT_2D <struct_POINT_2D>`
       - -
       - Corner point #2 (X,Y)
     * - 32
       - ``_tDetail._tTrap._fTMove1``
       - ``float``
       - s
       - Move time #1
     * - 36
       - ``_tDetail._tTrap._fTMove2``
       - ``float``
       - s
       - Move time #2
     * - 40
       - ``_tDetail._tTrap._fTAcc1``
       - ``float``
       - s
       - Acc time #1
     * - 44
       - ``_tDetail._tTrap._fTAcc2``
       - ``float``
       - s
       - Acc time #2
     * - 48
       - ``_tDetail._tTrap._fTDwell1``
       - ``float``
       - s
       - Dwell time #1
     * - 52
       - ``_tDetail._tTrap._fTDwell2``
       - ``float``
       - s
       - Dwell time #2

- **Circular** (``_tCirc``)

  .. list-table::
     :widths: 12 28 22 10 28
     :header-rows: 1

     * - **BYTE#**
       - **Field Name**
       - **Data Type**
       - **Value**
       - **Remarks**
     * - 16
       - ``_tDetail._tCirc._fWidthX``
       - ``float``
       - mm
       - X width (amplitude)
     * - 20
       - ``_tDetail._tCirc._fWidthY``
       - ``float``
       - mm
       - Y width (amplitude)
     * - 24
       - ``_tDetail._tCirc._fPeriodX``
       - ``float``
       - s
       - X period
     * - 28
       - ``_tDetail._tCirc._fPeriodY``
       - ``float``
       - s
       - Y period

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _CONFIG_WEAVING_SETTING
   {
       unsigned char _iType;
       float _fOffsetY;
       float _fOffsetZ;
       float _fGradient;

       union {
           struct {
               POINT_2D _tPoint1;
               POINT_2D _tPoint2;
               float _fTMove1;
               float _fTMove2;
               float _fTAcc1;
               float _fTAcc2;
               float _fTDwell1;
               float _fTDwell2;
           } _tTrap;

           struct {
               float _fWidthX;
               float _fWidthY;
               float _fPeriodX;
               float _fPeriodY;
           } _tCirc;

           unsigned char _szBuffer[48];
       } _tDetail;
   } CONFIG_WEAVING_SETTING, *LPCONFIG_WEAVING_SETTING;
