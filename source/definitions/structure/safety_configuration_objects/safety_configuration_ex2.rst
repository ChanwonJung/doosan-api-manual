.. _struct_SAFETY_CONFIGURATION_EX2:

SAFETY_CONFIGURATION_EX2
========================

This structure provides the **current safety configuration snapshot** of the controller (DRCF v2 path).  
Compared to :ref:`SAFETY_CONFIGURATION_EX <struct_SAFETY_CONFIGURATION_EX>`, it uses
:ref:`CONFIG_SAFETY_IO_OP <struct_CONFIG_SAFETY_IO_OP>` (operation options) and expands the
**User Coordinates** list to **100 items**.

.. list-table::
   :widths: 10 32 22 8 28
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_iDataVersion``
     - ``unsigned int``
     - -
     - Data version
   * - 4
     - ``_tJointRange``
     - :ref:`CONFIG_JOINT_RANGE <struct_CONFIG_JOINT_RANGE>`
     - -
     - Joint space range (Normal/Reduced)
   * - 232
     - ``_tGeneralRange``
     - :ref:`CONFIG_GENERAL_RANGE <struct_CONFIG_GENERAL_RANGE>`
     - -
     - Force/Power/Speed/Momentum limits
   * - 280
     - ``_fCollisionSensitivity``
     - ``float``
     - -
     - Collision sensitivity
   * - 284
     - ``_tSafetyFunc``
     - :ref:`CONFIG_SAFETY_FUNCTION <union_CONFIG_SAFETY_FUNCTION>`
     - -
     - Safety function map (SF05–SF17)
   * - 318
     - ``_tTool``
     - :ref:`CONFIG_TOOL_SYMBOL <struct_CONFIG_TOOL_SYMBOL>`
     - -
     - Tool name & data
   * - 390
     - ``_tTcp``
     - :ref:`CONFIG_TCP_SYMBOL <struct_CONFIG_TCP_SYMBOL>`
     - -
     - TCP name & data
   * - 446
     - ``_tInstallPose``
     - :ref:`CONFIG_INSTALL_POSE <struct_CONFIG_INSTALL_POSE>`
     - -
     - Install pose (gradient/rotation)
   * - 454
     - ``_tSafetyIO``
     - :ref:`CONFIG_SAFETY_IO_OP <struct_CONFIG_SAFETY_IO_OP>`
     - -
     - Safety I/O with **operation options** (2×16 map + flags)
   * - 520
     - ``_tSafetySpaceVF``
     - :ref:`CONFIG_VIRTUAL_FENCE <struct_CONFIG_VIRTUAL_FENCE>`
     - -
     - Operation space (virtual fence)
   * - 632
     - ``_tSafetySpaceSZ``
     - :ref:`CONFIG_SAFE_ZONE <struct_CONFIG_ADD_SAFETY_ZONE>`
     - -
     - Safety zone
   * - 689
     - ``_tSafetySpaceESZ``
     - :ref:`ENABLE_SAFE_ZONE <struct_ENABLE_SAFE_ZONE>`
     - -
     - Enable safety zone
   * - 692
     - ``_tSafetySpacePZ``
     - :ref:`CONFIG_PROTECTED_ZONE <struct_CONFIG_PROTECTED_ZONE>`
     - -
     - Protected zone
   * - 1722
     - ``_tSafetySpaceCM``
     - :ref:`CONFIG_COLLISION_MUTE_ZONE <struct_CONFIG_COLLISION_MUTE_ZONE>`
     - -
     - Collision mute zone
   * - 3122
     - ``_tSafetySpaceTO``
     - :ref:`CONFIG_TOOL_ORIENTATION_LIMIT_ZONE <struct_CONFIG_TOOL_ORIENTATION_LIMIT_ZONE>`
     - -
     - Tool orientation limit zone
   * - 4312
     - ``_tSafetySpaceTS``
     - :ref:`CONFIG_TOOL_SHAPE <struct_CONFIG_TOOL_SHAPE>`
     - -
     - Tool shape
   * - 4827
     - ``_tConfigNudge``
     - :ref:`CONFIG_NUDGE <struct_CONFIG_NUDGE>`
     - -
     - Nudge setting
   * - 4836
     - ``_tCockPit``
     - :ref:`CONFIG_COCKPIT_EX <struct_CONFIG_COCKPIT_EX>`
     - -
     - Cockpit setting
   * - 4840
     - ``_tIdleOff``
     - :ref:`CONFIG_IDLE_OFF <struct_CONFIG_IDLE_OFF>`
     - -
     - Auto servo-off setting
   * - 4845
     - ``_tConfigTCP``
     - :ref:`CONFIG_TCP_LIST <struct_CONFIG_TCP_LIST>`
     - -
     - TCP list setting
   * - 7649
     - ``_tConfigTool``
     - :ref:`CONFIG_TOOL_LIST <struct_CONFIG_TOOL_LIST>`
     - -
     - Tool list setting
   * - 11253
     - ``_tConfigToolShape``
     - :ref:`CONFIG_TOOL_SHAPE_LIST <struct_CONFIG_TOOL_SHAPE_LIST>`
     - -
     - Tool shape list setting
   * - 38607
     - ``_szActiveTcp``
     - ``char[32]``
     - -
     - Active TCP name
   * - 38639
     - ``_szActiveTool``
     - ``char[32]``
     - -
     - Active tool name
   * - 38671
     - ``_szActiveToolShape``
     - ``char[32]``
     - -
     - Active tool-shape name
   * - 38703
     - ``_tModbusList``
     - :ref:`MODBUS_DATA_LIST <struct_MODBUS_DATA_LIST>`
     - -
     - Modbus list
   * - 45805
     - ``_tWorld2BaseRelation``
     - :ref:`CONFIG_WORLD_COORDINATE <struct_CONFIG_WORLD_COORDINATE>`
     - -
     - World coordination setting
   * - 45830
     - ``m_CwsSpeedRatio``
     - ``float``
     - -
     - CWS speed ratio
   * - 45834
     - ``m_IoSpeedRatio``
     - ``float``
     - -
     - IO speed ratio
   * - 45838
     - ``_iSafetyZoneCount``
     - ``int``
     - -
     - Number of safety zones
   * - 45842
     - ``_tSafetyZone[20]``
     - :ref:`CONFIG_SAFETY_ZONE <struct_CONFIG_ADD_SAFETY_ZONE>`
     - -
     - Safety zone array (max 20)
   * - 54002
     - ``_iUserCoordCount``
     - ``int``
     - -
     - Number of user coordinates
   * - 54006
     - ``_tUserCoordinates[100]``
     - :ref:`CONFIG_USER_COORDINATE_EX <struct_CONFIG_USER_COORDINATE_EX>`
     - -
     - User coordinate array (max 100)
   * - 57206
     - ``_tConfigurableIO``
     - :ref:`CONFIG_CONFIGURABLE_IO <struct_CONFIG_CONFIGURABLE_IO>`
     - -
     - Configurable IO configuration

Total size: 57,238 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _SAFETY_CONFIGURATION_EX2
   {
       unsigned int _iDataVersion;
       CONFIG_JOINT_RANGE _tJointRange;
       CONFIG_GENERAL_RANGE _tGeneralRange;
       float _fCollisionSensitivity;
       CONFIG_SAFETY_FUNCTION _tSafetyFunc;
       CONFIG_TOOL_SYMBOL _tTool;
       CONFIG_TCP_SYMBOL _tTcp;
       CONFIG_INSTALL_POSE _tInstallPose;
       CONFIG_SAFETY_IO_OP _tSafetyIO;    // operation options variant
       //CONFIG_SAFETY_IO_EX _tSafetyIO;  // (unused here)

       CONFIG_VIRTUAL_FENCE _tSafetySpaceVF;
       CONFIG_SAFE_ZONE _tSafetySpaceSZ;
       ENABLE_SAFE_ZONE _tSafetySpaceESZ;
       CONFIG_PROTECTED_ZONE _tSafetySpacePZ;
       CONFIG_COLLISION_MUTE_ZONE _tSafetySpaceCM;
       CONFIG_TOOL_ORIENTATION_LIMIT_ZONE _tSafetySpaceTO;
       CONFIG_TOOL_SHAPE _tSafetySpaceTS;

       CONFIG_NUDGE _tConfigNudge;
       CONFIG_COCKPIT_EX _tCockPit;
       CONFIG_IDLE_OFF _tIdleOff;
       CONFIG_TCP_LIST _tConfigTCP;
       CONFIG_TOOL_LIST _tConfigTool;
       CONFIG_TOOL_SHAPE_LIST _tConfigToolShape;

       char _szActiveTcp[MAX_SYMBOL_SIZE];
       char _szActiveTool[MAX_SYMBOL_SIZE];
       char _szActiveToolShape[MAX_SYMBOL_SIZE];

       MODBUS_DATA_LIST _tModbusList;
       CONFIG_WORLD_COORDINATE _tWorld2BaseRelation;
       float m_CwsSpeedRatio;
       float m_IoSpeedRatio;

       int _iSafetyZoneCount;
       CONFIG_SAFETY_ZONE _tSafetyZone[20];

       int _iUserCoordCount;
       CONFIG_USER_COORDINATE_EX _tUserCoordinates[100];

       CONFIG_CONFIGURABLE_IO _tConfigurableIO;

   } SAFETY_CONFIGURATION_EX2, *LPSAFETY_CONFIGURATION_EX2;
