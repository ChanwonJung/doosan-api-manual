.. _measure_welding_tcp:

measure_welding_tcp
------------------------------------------

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 1043)

.. code-block:: cpp

    LPMEASURE_TCP_RESPONSE measure_welding_tcp(unsigned char iMode, float fStickout, float fTargetPos[9][NUMBER_OF_JOINT])
    {
        return _measure_welding_tcp(_rbtCtrl, iMode, fStickout, fTargetPos);
    };

**Features**

This function measures the **Tool Center Point (TCP)** for a welding tool using the specified  
measurement mode and stick-out length.  

During measurement, the robot moves to up to **9 target positions** defined by the parameter  
`fTargetPos`. The result includes both TCP coordinates and measurement status information.  

This function is mainly used to **calibrate welding tool positions** for precise path execution  
and can be applied for **torch alignment**, **offset correction**, or **tool verification**.

**Arguments**

.. list-table::
   :widths: 20 20 20 40
   :header-rows: 1

   * - **Argument**
     - **Data Type**
     - **Default Value**
     - **Description**
   * - iMode
     - unsigned char
     - -
     - Measurement mode |br|
       (0: 4-point method, 1: 6-point method)
   * - fStickout
     - float
     - -
     - Stick-out distance of the welding torch (mm).
   * - fTargetPos
     - float[9][NUMBER_OF_JOINT]
     - -
     - Target joint or Cartesian positions for up to 9 points. |br|
       Used for TCP calculation and accuracy calibration.

**Return**

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - **Return Value**
     - **Description**
   * - LPMEASURE_TCP_RESPONSE
     - Structure containing the measured TCP position (X, Y, Z, RX, RY, RZ) |br|
       and measurement status (success or error type).

**Example**

.. code-block:: cpp

    // Example: Welding TCP measurement procedure
    unsigned char iMode = 0;  // 0: 4-point method, 1: 6-point method
    float fStickout = 30.0f;  // Stick-out value in millimeters

    // Define 9 target points (joint or Cartesian positions)
    float fTargetPos[9][NUMBER_OF_JOINT] = {
        {0.0, 0.0, 0.0, 0.0, 0.0, 0.0},
        {5.0, 0.0, 0.0, 0.0, 0.0, 0.0},
        {0.0, 5.0, 0.0, 0.0, 0.0, 0.0},
        {0.0, 0.0, 5.0, 0.0, 0.0, 0.0},
        {0.0, 0.0, 0.0, 5.0, 0.0, 0.0},
        {0.0, 0.0, 0.0, 0.0, 5.0, 0.0},
        {5.0, 5.0, 0.0, 0.0, 0.0, 0.0},
        {5.0, 0.0, 5.0, 0.0, 0.0, 0.0},
        {0.0, 5.0, 5.0, 0.0, 0.0, 0.0}
    };

    // Define structure to store TCP measurement results
    LPMEASURE_TCP_RESPONSE result;

    // Perform TCP measurement
    result = Drfl.measure_welding_tcp(iMode, fStickout, fTargetPos);

    // Check results
    if (result->_bResult == 1)
    {
        printf("TCP Measurement Successful!\n");
        printf("Measured TCP: X=%.3f, Y=%.3f, Z=%.3f, RX=%.3f, RY=%.3f, RZ=%.3f\n",
               result->_fTCPPos[0], result->_fTCPPos[1], result->_fTCPPos[2],
               result->_fTCPPos[3], result->_fTCPPos[4], result->_fTCPPos[5]);
    }
    else
    {
        printf("Welding TCP measurement failed. Error code: %d\n", result->_bResult);
    }

In this example, the robot measures the TCP of the welding tool using a **4-point method**.  
The returned structure contains both the **calculated TCP coordinates** and a **status flag**  
indicating whether the measurement succeeded or failed.
