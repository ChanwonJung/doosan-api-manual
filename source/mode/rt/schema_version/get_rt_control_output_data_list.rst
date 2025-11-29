.. _get_rt_control_output_data_list:

get_rt_control_output_data_list
------------------------------------------
This function returns a list of **output data fields** supported by a specific  
Real-time (RT) output data version. |br|
Each version defines which robot states or signals are periodically transmitted  
from the controller to the external PC during real-time streaming.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 585)

.. code-block:: cpp

   string get_rt_control_output_data_list(string strVersion) { 
       return _get_rt_control_output_data_list(_rbtCtrlUDP, strVersion.c_str()); 
   };

**Parameter**

.. list-table::
   :widths: 25 25 20 30
   :header-rows: 1

   * - **Parameter Name**
     - **Data Type**
     - **Default Value**
     - **Description**
   * - strVersion
     - string
     - -
     - Target **output data version** (e.g., `"v1.0"`).

**Return**

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - **Value**
     - **Description**
   * - string
     - Comma-separated list of available **output data fields** for the specified version.

**Output Data List**

.. list-table::
   :widths: 25 18 37 20
   :header-rows: 1

   * - **Parameter Name**
     - **Data Type**
     - **Description**
     - **First Supported Controller Version**
   * - time_stamp
     - double
     - Timestamp at the moment of data acquisition [s].
     - v1.0
   * - actual_joint_position
     - float[6]
     - Joint position from incremental encoder at motor side [deg].
     - v1.0
   * - actual_joint_position_abs
     - float[6]
     - Joint position from absolute encoder at link side [deg].
     - v1.0
   * - actual_joint_velocity
     - float[6]
     - Joint velocity from incremental encoder at motor side [deg/s].
     - v1.0
   * - actual_joint_velocity_abs
     - float[6]
     - Joint velocity from absolute encoder at link side [deg/s].
     - v1.0
   * - actual_tcp_position
     - float[6]
     - TCP position w.r.t. base coordinates (x, y, z, a, b, c).
     - v1.0
   * - actual_tcp_velocity
     - float[6]
     - TCP velocity w.r.t. base coordinates [mm, deg/s].
     - v1.0
   * - actual_flange_position
     - float[6]
     - Flange position w.r.t. base coordinates [mm, deg].
     - v1.0
   * - actual_flange_velocity
     - float[6]
     - Flange velocity w.r.t. base coordinates [mm, deg/s].
     - v1.0
   * - actual_motor_torque
     - float[6]
     - Motor torque (gear_ratio × torque_constant × current) [Nm].
     - v1.0
   * - actual_joint_torque
     - float[6]
     - Joint torque by robot controller [Nm].
     - v1.0
   * - raw_joint_torque
     - float[6]
     - Calibrated joint torque sensor data [Nm].
     - v1.0
   * - raw_force_torque
     - float[6]
     - Calibrated force/torque sensor data in flange coordinates [N, Nm].
     - v1.0
   * - external_joint_torque
     - float[6]
     - Estimated joint torque [Nm].
     - v1.0
   * - external_tcp_force
     - float[6]
     - Estimated TCP force in base coordinates [N, Nm].
     - v1.0
   * - target_joint_position
     - float[6]
     - Target joint position [deg].
     - v1.0
   * - target_joint_velocity
     - float[6]
     - Target joint velocity [deg/s].
     - v1.0
   * - target_joint_acceleration
     - float[6]
     - Target joint acceleration [deg/s²].
     - v1.0
   * - target_joint_torque
     - float[6]
     - Target joint torque [Nm].
     - v1.0
   * - target_tcp_position
     - float[6]
     - Target TCP position w.r.t. base coordinates [mm, deg].
     - v1.0
   * - target_tcp_velocity
     - float[6]
     - Target TCP velocity w.r.t. base coordinates [mm/s, deg/s].
     - v1.0
   * - jacobian_matrix
     - float[6][6]
     - Jacobian matrix J(q) w.r.t. base coordinates.
     - v1.0
   * - gravity_torque
     - float[6]
     - Gravity torque g(q) [Nm].
     - v1.0
   * - coriolis_matrix
     - float[6][6]
     - Coriolis matrix C(q, q̇) [Nm·s].
     - v1.0
   * - mass_matrix
     - float[6][6]
     - Mass matrix M(q) [kg·m²].
     - v1.0
   * - solution_space
     - uint8
     - Robot configuration/solution space.
     - v1.0
   * - singularity
     - float
     - Minimum singular value.
     - v1.0
   * - operation_speed_rate
     - float
     - Current operation speed rate (1~100%).
     - v1.0
   * - joint_temperature
     - float[6]
     - Joint temperature (°C).
     - v1.0
   * - controller_digital_input
     - uint16
     - Controller digital input (16 channels).
     - v1.0
   * - controller_digital_output
     - uint16
     - Controller digital output (16 channels).
     - v1.0
   * - controller_analog_input_type
     - uint8[2]
     - Analog input type (2 channels).
     - v1.0
   * - controller_analog_input
     - float[2]
     - Controller analog input (2 channels).
     - v1.0
   * - controller_analog_output_type
     - uint8[2]
     - Analog output type (2 channels).
     - v1.0
   * - controller_analog_output
     - float[2]
     - Controller analog output (2 channels).
     - v1.0
   * - flange_digital_input
     - uint8
     - Flange digital input (A-Series: 2ch, M/H-Series: 6ch).
     - v1.0
   * - flange_digital_output
     - uint8
     - Flange digital output (A-Series: 2ch, M/H-Series: 6ch).
     - v1.0
   * - flange_analog_input
     - float[4]
     - Flange analog input (A-Series: 2ch, M/H-Series: 4ch).
     - v1.0
   * - external_encoder_strobe_count
     - uint32
     - Strobe count (incremented by 1 when detecting edge).
     - v1.0
   * - external_encoder_count
     - uint32[2]
     - External encoder count.
     - v1.0
   * - goal_joint_position
     - float[6]
     - Reserved: final goal joint position.
     - v1.0
   * - goal_tcp_position
     - float[6]
     - Reserved: final goal TCP position.
     - v1.0
   * - robot_mode
     - uint8
     - ROBOT_MODE_MANUAL(0), ROBOT_MODE_AUTONOMOUS(1), ROBOT_MODE_MEASURE(2)
     - v1.0
   * - robot_state
     - uint8
     - State codes (INITIALIZING=0, STANDBY=1, MOVING=2, etc.).
     - v1.0
   * - control_mode
     - uint16
     - Position control mode, torque mode.
     - v1.0

**Example**

.. code-block:: cpp

   #include "DRFLEx.h"
   #include <iostream>
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;

       drfl.connect_rt_control("192.168.137.100", 12347);

       // Retrieve output data fields for version v1.0
       std::string data_list = drfl.get_rt_control_output_data_list("v1.0");
       std::cout << "Output data fields: " << data_list << std::endl;

       drfl.disconnect_rt_control();
       return 0;
   }

In this example, the function returns a comma-separated list of all RT output data fields  
for the specified version (`"v1.0"`), which can be used when configuring output streaming.

**Tips**

- Use this after :ref:`get_rt_control_output_version_list <get_rt_control_output_version_list>`  
  to confirm available schema fields.  
- Field availability may differ depending on **controller model and firmware version**.  
- Each element corresponds to data returned by :ref:`read_data_rt <read_data_rt>`.
