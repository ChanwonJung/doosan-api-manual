.. _struct_RT_OUTPUT_DATA_LIST:

RT_OUTPUT_DATA_LIST
===================

This structure provides **real-time robot state data** transmitted from the controller  
to the external PC during Realtime External Control.  
It contains comprehensive motion, torque, and I/O information of the robot.

.. list-table::
   :widths: 10 30 18 8 34
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``time_stamp``
     - ``double``
     - -
     - Timestamp at data acquisition (s)
   * - 8
     - ``actual_joint_position``
     - ``float[NUMBER_OF_JOINT]``
     - [deg]
     - Joint position (motor-side incremental encoder)
   * - 32
     - ``actual_joint_position_abs``
     - ``float[NUMBER_OF_JOINT]``
     - [deg]
     - Joint position (link-side absolute encoder)
   * - 56
     - ``actual_joint_velocity``
     - ``float[NUMBER_OF_JOINT]``
     - [deg/s]
     - Joint velocity (motor-side)
   * - 80
     - ``actual_joint_velocity_abs``
     - ``float[NUMBER_OF_JOINT]``
     - [deg/s]
     - Joint velocity (link-side)
   * - 104
     - ``actual_tcp_position``
     - ``float[NUM_TASK]``
     - [mm, deg]
     - TCP position (x, y, z, a, b, c)
   * - 128
     - ``actual_tcp_velocity``
     - ``float[NUM_TASK]``
     - [mm/s, deg/s]
     - TCP velocity (in base coordinates)
   * - 152
     - ``actual_flange_position``
     - ``float[NUM_TASK]``
     - [mm, deg]
     - Flange position (in base coordinates)
   * - 176
     - ``actual_flange_velocity``
     - ``float[NUM_TASK]``
     - [mm/s, deg/s]
     - Flange velocity (in base coordinates)
   * - 200
     - ``actual_motor_torque``
     - ``float[NUMBER_OF_JOINT]``
     - [Nm]
     - Motor torque (applied with gear ratio)
   * - 224
     - ``actual_joint_torque``
     - ``float[NUMBER_OF_JOINT]``
     - [Nm]
     - Estimated joint torque
   * - 248
     - ``raw_joint_torque``
     - ``float[NUMBER_OF_JOINT]``
     - [Nm]
     - Raw torque sensor values (calibrated)
   * - 272
     - ``raw_force_torque``
     - ``float[NUMBER_OF_JOINT]``
     - [N, Nm]
     - Force/Torque sensor data (flange coordinates)
   * - 296
     - ``external_joint_torque``
     - ``float[NUMBER_OF_JOINT]``
     - [Nm]
     - Estimated external torque per joint
   * - 320
     - ``external_tcp_force``
     - ``float[NUM_TASK]``
     - [N, Nm]
     - External TCP force (in base coordinates)
   * - 344
     - ``target_joint_position``
     - ``float[NUMBER_OF_JOINT]``
     - [deg]
     - Target joint position
   * - 368
     - ``target_joint_velocity``
     - ``float[NUMBER_OF_JOINT]``
     - [deg/s]
     - Target joint velocity
   * - 392
     - ``target_joint_acceleration``
     - ``float[NUMBER_OF_JOINT]``
     - [deg/s²]
     - Target joint acceleration
   * - 416
     - ``target_motor_torque``
     - ``float[NUMBER_OF_JOINT]``
     - [Nm]
     - Target motor torque
   * - 440
     - ``target_tcp_position``
     - ``float[NUM_TASK]``
     - [mm, deg]
     - Target TCP position
   * - 464
     - ``target_tcp_velocity``
     - ``float[NUM_TASK]``
     - [mm/s, deg/s]
     - Target TCP velocity
   * - 488
     - ``jacobian_matrix``
     - ``float[NUMBER_OF_JOINT][NUMBER_OF_JOINT]``
     - -
     - Jacobian matrix J(q)
   * - 632
     - ``gravity_torque``
     - ``float[NUMBER_OF_JOINT]``
     - [Nm]
     - Gravity torque g(q)
   * - 656
     - ``coriolis_matrix``
     - ``float[NUMBER_OF_JOINT][NUMBER_OF_JOINT]``
     - -
     - Coriolis matrix C(q, q̇)
   * - 800
     - ``mass_matrix``
     - ``float[NUMBER_OF_JOINT][NUMBER_OF_JOINT]``
     - -
     - Mass matrix M(q)
   * - 944
     - ``solution_space``
     - ``unsigned short``
     - -
     - Robot configuration (solution space)
   * - 946
     - ``singularity``
     - ``float``
     - -
     - Minimum singular value
   * - 950
     - ``operation_speed_rate``
     - ``float``
     - [%]
     - Current speed ratio
   * - 954
     - ``joint_temperature``
     - ``float[NUMBER_OF_JOINT]``
     - [°C]
     - Joint temperature
   * - 978
     - ``controller_digital_input``
     - ``unsigned short``
     - -
     - Controller DI (16-channel)
   * - 980
     - ``controller_digital_output``
     - ``unsigned short``
     - -
     - Controller DO (16-channel)
   * - 982
     - ``controller_analog_input_type``
     - ``unsigned char[2]``
     - -
     - Controller AI type (0: voltage, 1: current)
   * - 984
     - ``controller_analog_input``
     - ``float[2]``
     - [V/mA]
     - Controller analog inputs
   * - 992
     - ``controller_analog_output_type``
     - ``unsigned char[2]``
     - -
     - Controller AO type (0: voltage, 1: current)
   * - 994
     - ``controller_analog_output``
     - ``float[2]``
     - [V/mA]
     - Controller analog outputs
   * - 1002
     - ``flange_digital_input``
     - ``unsigned char``
     - -
     - Flange DI (A-series: 2ch, M/H-series: 6ch)
   * - 1003
     - ``flange_digital_output``
     - ``unsigned char``
     - -
     - Flange DO (A-series: 2ch, M/H-series: 6ch)
   * - 1004
     - ``flange_analog_input``
     - ``float[4]``
     - [V/mA]
     - Flange analog input channels
   * - 1020
     - ``external_encoder_strobe_count``
     - ``unsigned char[2]``
     - -
     - Encoder strobe event count
   * - 1022
     - ``external_encoder_count``
     - ``unsigned int[2]``
     - -
     - External encoder pulse counts
   * - 1030
     - ``goal_joint_position``
     - ``float[NUMBER_OF_JOINT]``
     - [deg]
     - Reserved for final goal joint
   * - 1054
     - ``goal_tcp_position``
     - ``float[NUM_TASK]``
     - [mm, deg]
     - Reserved for final goal TCP
   * - 1078
     - ``robot_mode``
     - ``unsigned char``
     - 0~2
     - Robot mode (0: Manual, 1: Auto, 2: Recovery)
   * - 1079
     - ``robot_state``
     - ``unsigned char``
     - 0~9
     - Operation state (Standby, Moving, etc.)
   * - 1080
     - ``control_mode``
     - ``unsigned short``
     - -
     - Servo mode (Position, Torque)
   * - 1082
     - ``reserved``
     - ``unsigned char[256]``
     - -
     - Reserved bytes for future expansion

Total size: 1,024 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

    typedef struct _RT_OUTPUT_DATA_LIST
    {
    /* timestamp at the data of data acquisition */
    double                      time_stamp;
    /* actual joint position from incremental encoder at motor side(used for control) [deg] */
    float                       actual_joint_position[NUMBER_OF_JOINT];
    /* actual joint position from absolute encoder at link side (used for exact link position) [deg] */
    float                       actual_joint_position_abs[NUMBER_OF_JOINT];
    /* actual joint velocity from incremental encoder at motor side [deg/s] */
    float                       actual_joint_velocity[NUMBER_OF_JOINT];
    /* actual joint velocity from absolute encoder at link side [deg/s] */
    float                       actual_joint_velocity_abs[NUMBER_OF_JOINT];
    /* actual robot tcp position w.r.t. base coordinates: (x, y, z, a, b, c), where (a, b, c) follows Euler ZYZ notation [mm, deg] */
    float                       actual_tcp_position[NUM_TASK];
    /* actual robot tcp velocity w.r.t. base coordinates [mm, deg/s] */
    float                       actual_tcp_velocity[NUMBER_OF_TASK];
    /* actual robot flange position w.r.t. base coordinates: (x, y, z, a, b, c), where (a, b, c) follows Euler ZYZ notation [mm, deg] */
    float                       actual_flange_position[NUMBER_OF_TASK];
    /* robot flange velocity w.r.t. base coordinates [mm, deg/s] */
    float                       actual_flange_velocity[NUMBER_OF_TASK];
    /* actual motor torque applying gear ratio = gear_ratio * current2torque_constant * motor current [Nm] */
    float                       actual_motor_torque[NUMBER_OF_JOINT];
    /* estimated joint torque by robot controller [Nm] */
    float                       actual_joint_torque[NUMBER_OF_JOINT];
    /* calibrated joint torque sensor data [Nm] */
    float                       raw_joint_torque[NUMBER_OF_JOINT];
    /* calibrated force torque sensor data w.r.t. flange coordinates [N, Nm] */
    float                       raw_force_torque[NUMBER_OF_JOINT];
    /* estimated external joint torque [Nm] */
    float                       external_joint_torque[NUMBER_OF_JOINT];
    /* estimated tcp force w.r.t. base coordinates [N, Nm] */
    float                       external_tcp_force[NUMBER_OF_TASK];
    /* target joint position [deg] */
    float                       target_joint_position[NUMBER_OF_JOINT];
    /* target joint velocity [deg/s] */
    float                       target_joint_velocity[NUMBER_OF_JOINT];
    /* target joint acceleration [deg/s^2] */
    float                       target_joint_acceleration[NUMBER_OF_JOINT];
    /* target motor torque [Nm] */
    float                       target_motor_torque[NUMBER_OF_JOINT];
    /* target tcp position w.r.t. base coordinates: (x, y, z, a, b, c), where (a, b, c) follows Euler ZYZ notation [mm, deg] */
    float                       target_tcp_position[NUMBER_OF_TASK];
    /* target tcp velocity w.r.t. base coordinates [mm, deg/s] */
    float                       target_tcp_velocity[NUMBER_OF_TASK];
    /* jacobian matrix=J(q) w.r.t. base coordinates */
    float                       jacobian_matrix[NUMBER_OF_JOINT][NUMBER_OF_JOINT];
    /* gravity torque=g(q) [Nm] */
    float                       gravity_torque[NUMBER_OF_JOINT];
    /* coriolis matrix=C(q,q_dot)  */
    float                       coriolis_matrix[NUMBER_OF_JOINT][NUMBER_OF_JOINT];
    /* mass matrix=M(q) */
    float                       mass_matrix[NUMBER_OF_JOINT][NUMBER_OF_JOINT];
    /* robot configuration */
    unsigned short              solution_space;
    /* minimum singular value */
    float                       singularity;
    /* current operation speed rate(1~100 %) */
    float                       operation_speed_rate;
    /* joint temperature(celsius) */
    float                       joint_temperature[NUMBER_OF_JOINT];
    /* controller digital input(16 channel) */
    unsigned short              controller_digital_input;
    /* controller digital output(16 channel) */
    unsigned short              controller_digital_output;
    /* controller analog input type(2 channel) */
    unsigned char               controller_analog_input_type[2];
    /* controller analog input(2 channel) */
    float                       controller_analog_input[2];
    /* controller analog output type(2 channel) */
    unsigned char               controller_analog_output_type[2];
    /* controller analog output(2 channel) */
    float                       controller_analog_output[2];
    /* flange digital input(A-Series: 2 channel, M/H-Series: 6 channel) */
    unsigned char               flange_digital_input;
    /* flange digital output(A-Series: 2 channel, M/H-Series: 6 channel) */
    unsigned char               flange_digital_output;
    /* flange analog input(A-Series: 2 channel, M/H-Series: 4 channel) */
    float                       flange_analog_input[4];
    /* strobe count(increased by 1 when detecting setting edge) */
    unsigned char               external_encoder_strobe_count[2];
    /* external encoder count */
    unsigned int                external_encoder_count[2];
    /* final goal joint position (reserved) */
    float                       goal_joint_position[NUMBER_OF_JOINT];
    /* final goal tcp position (reserved) */
    float                       goal_tcp_position[NUMBER_OF_TASK];
    /* ROBOT_MODE_MANUAL(0), ROBOT_MODE_AUTONOMOUS(1), SAFETY_MODE_RECOVERY(2)*/
    /* Refer to 'SAFETY_MODE' struct*/
    unsigned char               robot_mode;
    /* STATE_INITIALIZING(0), STATE_STANDBY(1), STATE_MOVING(2), STATE_SAFE_OFF(3), STATE_TEACHING(4), STATE_SAFE_STOP(5), STATE_EMERGENCY_STOP, STATE_HOMMING, STATE_RECOVERY, STATE_SAFE_STOP2, STATE_SAFE_OFF2, */
    /* Refer to 'OPERATION_STATE' struct in DRCF 'ROBOT_STATE' struct in DRFL.*/
    unsigned char               robot_state;
    /* position control mode, torque mode */
    /* Refer to 'SERVO_MODE' struct*/
    unsigned short              control_mode;
    /* Reserved */
    unsigned char               reserved[256];
    
    } RT_OUTPUT_DATA_LIST, *LPRT_OUTPUT_DATA_LIST;

.. note::
   - Provides **all robot dynamic and sensor data** in real-time.
   - Used for **external torque control**, **compliance**, and **RT logging**.
   - Transmitted at high frequency (default: 1 kHz) via UDP during Realtime Control.
   - All positions and torques follow **SI units** (mm, deg, N, Nm).