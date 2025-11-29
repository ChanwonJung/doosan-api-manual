.. _struct_SAFETY_CONFIGURATION_EX2_V3:

SAFETY_CONFIGURATION_EX2_V3
===========================

This structure provides the **current safety configuration snapshot** of the controller for **DRCF v3**.
Compared to :ref:`SAFETY_CONFIGURATION_EX2 <struct_SAFETY_CONFIGURATION_EX2>` (v2 path), this version adopts the new
“_EX” data types for TCP, world coordinates, user coordinates, safety I/O, and configurable I/O:

- :ref:`CONFIG_TCP_SYMBOL_EX <struct_CONFIG_TCP_SYMBOL_EX>` / :ref:`CONFIG_TCP_LIST_EX <struct_CONFIG_TCP_LIST_EX>`
- :ref:`CONFIG_WORLD_COORDINATE_EX <struct_CONFIG_WORLD_COORDINATE_EX>`
- ``CONFIG_USER_COORDINATE_EX2`` (100 entries)
- :ref:`CONFIG_SAFETY_IO_EX <struct_CONFIG_SAFETY_IO_EX>`
- :ref:`CONFIG_CONFIGURABLE_IO_EX <struct_CONFIG_CONFIGURABLE_IO_EX>`

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
     - Safety function map (SF05-SF17)
   * - 318
     - ``_tTool``
     - :ref:`CONFIG_TOOL_SYMBOL <struct_CONFIG_TOOL_SYMBOL>`
     - -
     - Tool name & data
   * - 390
     - ``_tTcp``  *(v3)*
     - :ref:`CONFIG_TCP_SYMBOL_EX <struct_CONFIG_TCP_SYMBOL_EX>`
     - -
     - TCP name & data (supports :ref:`POSITION_EX <struct_POSITION_EX>`)
   * - 495
     - ``_tInstallPose``
     - :ref:`CONFIG_INSTALL_POSE <struct_CONFIG_INSTALL_POSE>`
     - -
     - Install pose (gradient/rotation)
   * - 503
     - ``_tSafetyIO`` *(v3)*
     - :ref:`CONFIG_SAFETY_IO_EX <struct_CONFIG_SAFETY_IO_EX>`
     - -
     - Safety I/O map (extended 2x16)
   * - 535
     - ``_tSafetySpaceVF``
     - :ref:`CONFIG_VIRTUAL_FENCE <struct_CONFIG_VIRTUAL_FENCE>`
     - -
     - Operation space (virtual fence)
   * - 684
     - ``_tSafetySpaceSZ``
     - :ref:`CONFIG_SAFE_ZONE <struct_CONFIG_ADD_SAFETY_ZONE>`
     - -
     - Safety zone
   * - 1086
     - ``_tSafetySpaceESZ``
     - :ref:`ENABLE_SAFE_ZONE <struct_ENABLE_SAFE_ZONE>`
     - -
     - Enable safety zone
   * - 1089
     - ``_tSafetySpacePZ``
     - :ref:`CONFIG_PROTECTED_ZONE <struct_CONFIG_PROTECTED_ZONE>`
     - -
     - Protected zone
   * - 2119
     - ``_tSafetySpaceCM``
     - :ref:`CONFIG_COLLISION_MUTE_ZONE <struct_CONFIG_COLLISION_MUTE_ZONE>`
     - -
     - Collision mute zone
   * - 3519
     - ``_tSafetySpaceTO``
     - :ref:`CONFIG_TOOL_ORIENTATION_LIMIT_ZONE <struct_CONFIG_TOOL_ORIENTATION_LIMIT_ZONE>`
     - -
     - Tool orientation limit zone
   * - 6349
     - ``_tSafetySpaceTS``
     - :ref:`CONFIG_TOOL_SHAPE <struct_CONFIG_TOOL_SHAPE>`
     - -
     - Tool shape
   * - 6864
     - ``_tConfigNudge``
     - :ref:`CONFIG_NUDGE <struct_CONFIG_NUDGE>`
     - -
     - Nudge setting
   * - 6873
     - ``_tCockPit``
     - :ref:`CONFIG_COCKPIT_EX <struct_CONFIG_COCKPIT_EX>`
     - -
     - Cockpit setting
   * - 6877
     - ``_tIdleOff``
     - :ref:`CONFIG_IDLE_OFF <struct_CONFIG_IDLE_OFF>`
     - -
     - Auto servo-off setting
   * - 6882
     - ``_tConfigTCP`` *(v3)*
     - :ref:`CONFIG_TCP_LIST_EX <struct_CONFIG_TCP_LIST_EX>`
     - -
     - TCP list setting (EX entries)
   * - 12136
     - ``_tConfigTool``
     - :ref:`CONFIG_TOOL_LIST <struct_CONFIG_TOOL_LIST>`
     - -
     - Tool list setting
   * - 15740
     - ``_tConfigToolShape``
     - :ref:`CONFIG_TOOL_SHAPE_LIST <struct_CONFIG_TOOL_SHAPE_LIST>`
     - -
     - Tool shape list setting
   * - 43094
     - ``_szActiveTcp``
     - ``char[MAX_SYMBOL_SIZE]``
     - -
     - Active TCP name
   * - 43126
     - ``_szActiveTool``
     - ``char[MAX_SYMBOL_SIZE]``
     - -
     - Active tool name
   * - 43158
     - ``_szActiveToolShape``
     - ``char[MAX_SYMBOL_SIZE]``
     - -
     - Active tool-shape name
   * - 43190
     - ``_tModbusList``
     - :ref:`MODBUS_DATA_LIST <struct_MODBUS_DATA_LIST>`
     - -
     - Modbus list
   * - 54392
     - ``_tWorld2BaseRelation``
     - :ref:`CONFIG_WORLD_COORDINATE_EX <struct_CONFIG_WORLD_COORDINATE_EX>`
     - -
     - World ↔ Base relation (EX)
   * - 54424
     - ``m_CwsSpeedRatio``
     - ``float``
     - -
     - CWS speed ratio
   * - 54428
     - ``m_IoSpeedRatio``
     - ``float``
     - -
     - IO speed ratio
   * - 54432
     - ``_iSafetyZoneCount``
     - ``int``
     - -
     - Number of safety zones
   * - 54436
     - ``_tSafetyZone[20]``
     - :ref:`CONFIG_SAFETY_ZONE <struct_CONFIG_ADD_SAFETY_ZONE>`
     - -
     - Safety zone array (max 20)
   * - 62476
     - ``_iUserCoordCount``
     - ``int``
     - -
     - Number of user coordinates
   * - 62480
     - ``_tUserCoordinates[100]``
     - ``CONFIG_USER_COORDINATE_EX2[100]``
     - -
     - User coordinate array (EX2, max 100)
   * - 65680
     - ``_tConfigurableIO``
     - :ref:`CONFIG_CONFIGURABLE_IO_EX <struct_CONFIG_CONFIGURABLE_IO_EX>`
     - -
     - Configurable IO mapping (extended)

Total size : 65,744 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _SAFETY_CONFIGURATION_EX2_V3
   {
       unsigned int _iDataVersion;
       CONFIG_JOINT_RANGE _tJointRange;
       CONFIG_GENERAL_RANGE _tGeneralRange;
       float _fCollisionSensitivity;
       CONFIG_SAFETY_FUNCTION _tSafetyFunc;
       CONFIG_TOOL_SYMBOL _tTool;
       CONFIG_TCP_SYMBOL_EX _tTcp; // v3
       CONFIG_INSTALL_POSE _tInstallPose;
       CONFIG_SAFETY_IO_EX _tSafetyIO; // v3

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
       CONFIG_TCP_LIST_EX _tConfigTCP; // v3
       CONFIG_TOOL_LIST _tConfigTool;
       CONFIG_TOOL_SHAPE_LIST _tConfigToolShape;

       char _szActiveTcp[MAX_SYMBOL_SIZE];
       char _szActiveTool[MAX_SYMBOL_SIZE];
       char _szActiveToolShape[MAX_SYMBOL_SIZE];

       MODBUS_DATA_LIST _tModbusList;
       CONFIG_WORLD_COORDINATE_EX _tWorld2BaseRelation; // v3
       float m_CwsSpeedRatio;
       float m_IoSpeedRatio;

       int _iSafetyZoneCount;
       CONFIG_SAFETY_ZONE _tSafetyZone[20];

       int _iUserCoordCount;
       CONFIG_USER_COORDINATE_EX2 _tUserCoordinates[100]; // v3

       CONFIG_CONFIGURABLE_IO_EX _tConfigurableIO; // v3

   } SAFETY_CONFIGURATION_EX2_V3, *LPSAFETY_CONFIGURATION_EX2_V3;

.. note::
   - ``_EX`` / ``EX2`` fields in v3 expand pose/orientation representations and lists.
   - If you want a **byte-accurate** table (BYTE# offsets and total size) like earlier sections,
     we can compute it precisely once the sizes for the following dependent types are fixed in your build: |br|
     :ref:`POSITION_EX <struct_POSITION_EX>`, :ref:`CONFIG_WORLD_COORDINATE_EX <struct_CONFIG_WORLD_COORDINATE_EX>`,
     ``CONFIG_USER_COORDINATE_EX2``. The rest (e.g., :ref:`CONFIG_SAFETY_IO_EX <struct_CONFIG_SAFETY_IO_EX>` = 32 bytes,
     :ref:`CONFIG_CONFIGURABLE_IO_EX <struct_CONFIG_CONFIGURABLE_IO_EX>` = 64 bytes) are already stable in this manual.
