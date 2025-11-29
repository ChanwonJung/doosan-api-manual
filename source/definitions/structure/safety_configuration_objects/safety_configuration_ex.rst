.. _struct_SAFETY_CONFIGURATION_EX:

SAFETY_CONFIGURATION_EX
=======================

This structure provides the **current (legacy) safety configuration snapshot** of the controller.  
It aggregates joint/force ranges, safety functions, active tool/TCP sets, virtual fence & zones,  
Modbus list, world coordinates, speed ratios, and configurable I/O into a single payload.

.. warning::
   This type is **deprecated**. ``get_safety_configuration()`` no longer returns this type.

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
     - :ref:`CONFIG_SAFETY_IO <struct_CONFIG_SAFETY_IO>`
     - -
     - Safety I/O map (8 in, 8 out)
   * - 470
     - ``_tSafetySpaceVF``
     - :ref:`CONFIG_VIRTUAL_FENCE <struct_CONFIG_VIRTUAL_FENCE>`
     - -
     - Operation space (virtual fence)
   * - 582
     - ``_tSafetySpaceSZ``
     - :ref:`CONFIG_SAFE_ZONE <struct_CONFIG_ADD_SAFETY_ZONE>`
     - -
     - Safety zone
   * - 639
     - ``_tSafetySpaceESZ``
     - :ref:`ENABLE_SAFE_ZONE <struct_ENABLE_SAFE_ZONE>`
     - -
     - Enable safety zone
   * - 642
     - ``_tSafetySpacePZ``
     - :ref:`CONFIG_PROTECTED_ZONE <struct_CONFIG_PROTECTED_ZONE>`
     - -
     - Protected zone
   * - 1672
     - ``_tSafetySpaceCM``
     - :ref:`CONFIG_COLLISION_MUTE_ZONE <struct_CONFIG_COLLISION_MUTE_ZONE>`
     - -
     - Collision mute zone
   * - 3072
     - ``_tSafetySpaceTO``
     - :ref:`CONFIG_TOOL_ORIENTATION_LIMIT_ZONE <struct_CONFIG_TOOL_ORIENTATION_LIMIT_ZONE>`
     - -
     - Tool orientation limit zone
   * - 4262
     - ``_tSafetySpaceTS``
     - :ref:`CONFIG_TOOL_SHAPE <struct_CONFIG_TOOL_SHAPE>`
     - -
     - Tool shape
   * - 4777
     - ``_tConfigNudge``
     - :ref:`CONFIG_NUDGE <struct_CONFIG_NUDGE>`
     - -
     - Nudge setting
   * - 4786
     - ``_tCockPit``
     - :ref:`CONFIG_COCKPIT_EX <struct_CONFIG_COCKPIT_EX>`
     - -
     - Cockpit setting
   * - 4790
     - ``_tIdleOff``
     - :ref:`CONFIG_IDLE_OFF <struct_CONFIG_IDLE_OFF>`
     - -
     - Auto servo-off setting
   * - 4795
     - ``_tConfigTCP``
     - :ref:`CONFIG_TCP_LIST <struct_CONFIG_TCP_LIST>`
     - -
     - TCP list setting
   * - 7599
     - ``_tConfigTool``
     - :ref:`CONFIG_TOOL_LIST <struct_CONFIG_TOOL_LIST>`
     - -
     - Tool list setting
   * - 11203
     - ``_tConfigToolShape``
     - :ref:`CONFIG_TOOL_SHAPE_LIST <struct_CONFIG_TOOL_SHAPE_LIST>`
     - -
     - Tool shape list setting
   * - 38557
     - ``_szActiveTcp``
     - ``char[32]``
     - -
     - Active TCP name
   * - 38589
     - ``_szActiveTool``
     - ``char[32]``
     - -
     - Active tool name
   * - 38621
     - ``_szActiveToolShape``
     - ``char[32]``
     - -
     - Active tool-shape name
   * - 38653
     - ``_tModbusList``
     - :ref:`MODBUS_DATA_LIST <struct_MODBUS_DATA_LIST>`
     - -
     - Modbus list
   * - 45755
     - ``_tWorld2BaseRelation``
     - :ref:`CONFIG_WORLD_COORDINATE <struct_CONFIG_WORLD_COORDINATE>`
     - -
     - World coordination setting
   * - 45780
     - ``m_CwsSpeedRatio``
     - ``float``
     - -
     - CWS speed ratio
   * - 45784
     - ``m_IoSpeedRatio``
     - ``float``
     - -
     - IO speed ratio
   * - 45788
     - ``_iSafetyZoneCount``
     - ``int``
     - -
     - Number of safety zones
   * - 45792
     - ``_tSafetyZone[20]``
     - :ref:`CONFIG_SAFETY_ZONE <struct_CONFIG_ADD_SAFETY_ZONE>`
     - -
     - Safety zone array (max 20)
   * - 53952
     - ``_iUserCoordCount``
     - ``int``
     - -
     - Number of user coordinates
   * - 53956
     - ``_tUserCoordinates[20]``
     - :ref:`CONFIG_USER_COORDINATE_EX <struct_CONFIG_USER_COORDINATE_EX>`
     - -
     - User coordinate array (max 20)
   * - 54596
     - ``_tConfigurableIO``
     - :ref:`CONFIG_CONFIGURABLE_IO <struct_CONFIG_CONFIGURABLE_IO>`
     - -
     - Configurable IO configuration

Total size: 54,628 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _SAFETY_CONFIGURATION_EX
   {
       unsigned int                 _iDataVersion;
       CONFIG_JOINT_RANGE           _tJointRange;
       CONFIG_GENERAL_RANGE         _tGeneralRange;
       float                        _fCollisionSensitivity;
       CONFIG_SAFETY_FUNCTION       _tSafetyFunc;
       CONFIG_TOOL_SYMBOL           _tTool;
       CONFIG_TCP_SYMBOL            _tTcp;
       CONFIG_INSTALL_POSE          _tInstallPose;
       CONFIG_SAFETY_IO             _tSafetyIO; /* legacy */
       //CONFIG_SAFETY_IO_EX        _tSafetyIO; /* newer variants */

       CONFIG_VIRTUAL_FENCE         _tSafetySpaceVF;
       CONFIG_SAFE_ZONE             _tSafetySpaceSZ;
       ENABLE_SAFE_ZONE             _tSafetySpaceESZ;
       CONFIG_PROTECTED_ZONE        _tSafetySpacePZ;
       CONFIG_COLLISION_MUTE_ZONE   _tSafetySpaceCM;
       CONFIG_TOOL_ORIENTATION_LIMIT_ZONE _tSafetySpaceTO;
       CONFIG_TOOL_SHAPE            _tSafetySpaceTS;

       CONFIG_NUDGE                 _tConfigNudge;
       CONFIG_COCKPIT_EX            _tCockPit;
       CONFIG_IDLE_OFF              _tIdleOff;
       CONFIG_TCP_LIST              _tConfigTCP;
       CONFIG_TOOL_LIST             _tConfigTool;
       CONFIG_TOOL_SHAPE_LIST       _tConfigToolShape;

       char                         _szActiveTcp[MAX_SYMBOL_SIZE];
       char                         _szActiveTool[MAX_SYMBOL_SIZE];
       char                         _szActiveToolShape[MAX_SYMBOL_SIZE];

       MODBUS_DATA_LIST             _tModbusList;
       CONFIG_WORLD_COORDINATE      _tWorld2BaseRelation;
       float                        m_CwsSpeedRatio;
       float                        m_IoSpeedRatio;

       int                          _iSafetyZoneCount;
       CONFIG_SAFETY_ZONE           _tSafetyZone[20];

       int                          _iUserCoordCount;
       CONFIG_USER_COORDINATE_EX    _tUserCoordinates[20];

       CONFIG_CONFIGURABLE_IO       _tConfigurableIO;

   } SAFETY_CONFIGURATION_EX, *LPSAFETY_CONFIGURATION_EX;
