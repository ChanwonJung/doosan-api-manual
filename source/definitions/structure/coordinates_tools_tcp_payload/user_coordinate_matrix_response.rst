.. _struct_USER_COORDINATE_MATRIX_RESPONSE:

USER_COORDINATE_MATRIX_RESPONSE
===============================

This structure defines a **3×3 rotation matrix** and **3D translation vector**  
representing the transformation of a user coordinate system.  
It is typically used as a response structure when querying the robot’s  
user coordinate matrix for transformation or calibration purposes.

.. list-table::
   :widths: 10 28 22 8 32
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_fOrientXYZ``
     - ``float[3][3]``
     - -
     - 3x3 rotation matrix representing orientation |br|
       (rows correspond to X, Y, Z axes of the user frame)
   * - 36
     - ``_fTranslXYZ``
     - ``float[3]``
     - [mm]
     - Translation vector (X, Y, Z) of the user coordinate frame  
       with respect to the reference frame

Total size: 48 bytes  

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _USER_COORDINATE_MATRIX_RESPONSE
   {
       /* 3×3 rotation matrix (orientation) */
       float _fOrientXYZ[3][3];
       /* 3D translation vector (X, Y, Z) */
       float _fTranslXYZ[3];

   } USER_COORDINATE_MATRIX_RESPONSE, *LPUSER_COORDINATE_MATRIX_RESPONSE;
