.. _Using_header_file:

1.2.4 Using Header File
------------------------------------------

When there is a #include library function-related header file (DRFL.h), 
when the compile option is set in C++ language, programming is possible 
using CDRFLEx class, but when set in C language, a “_function name” type 
global function should be used for programming.


Some functions may have different interface usage depending on the controller version. 
Before importing the DRFL header, please declare **#define DRCF_VERSION 2** or 
**#define DRCF_VERSION 3** according to the controller version.

.. code-block:: cpp
   :linenos:
   :caption: Example of including and initializing DRFLEx in C++

   #define DRCF_VERSION 3
   #include "../../include/DRFLEx.h"
   #include "util.hpp"

   const std::string IP_ADDRESS = "192.168.137.100";

   using namespace DRAFramework;
   CDRFLEx robot;

   bool g_bHasControlAuthority = FALSE;
   bool g_TpInitailizingComplted = FALSE;
   bool control_authority_granted = FALSE;
