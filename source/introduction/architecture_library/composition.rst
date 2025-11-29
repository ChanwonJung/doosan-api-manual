.. _composition_of_library:

1.2.2 Composition of Library
-----------------------------------------

This API is composed of **four C/C++ header files**, a **library file** related to them,  
and additional **support (third-party) library files** required for proper operation
on both Linux and Windows environments.

.. list-table::
   :header-rows: 1
   :widths: 15 30 35 20

   * - **Type**
     - **File Name**
     - **Description**
     - **Remarks**
   * - **Header File**
     - DRFL.h
     - Core API Function Definition File
     -
   * -
     - DRFLEx.h
     - Extended Function Definition File
     -
   * -
     - DRFS.h
     - Library-related Structure Definition File
     -
   * -
     - DRFC.h
     - Library-related Constant Definition File
     -

   * - **Library File**
     - libDRFL.a

       libDRFL.so
     - Linux Library File
     -
   * -
     - DRFLWin64.lib  
       
       DRFLWin64.dll
     - Windows (x64)Library File
     -

   * - **Other Support Files**
     - libPocoFoundation.so  
       
       libPocoFoundation.so.16  
       
       libPocoNet.so  
       
       libPocoNet.so.16
     - Linux Dependency Library File
     - Registering library using ldconfig function
   * -
     - PocoFoundation.lib  
       
       PocoFoundation.dll  
       
       PocoNet.lib  
       
       PocoNet.dll
     - Windows Dependency Library File  
     - **Microsoft Visual C++ 2019 (x64) Redistributable** or newer is required.

.. note::
   - The **Poco** framework is used internally by DRFL for TCP/UDP communication and
     multi-threaded operations.  
   - On **Linux**, ensure that ``/usr/lib`` or ``/usr/local/lib`` contains symbolic links
     (e.g., ``libPocoFoundation.so → libPocoFoundation.so.16``).  
   - On **Windows**, verify that the Visual Studio project targets the correct architecture
     (preferably **x64**) and that Poco DLLs are available in the system PATH.
