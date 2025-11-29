.. _Linking_Library:

1.2.3 Linking Library
------------------------------------------

Linux Library
~~~~~~~~~~~~~~~~~~~~~
A file that has a .conf extension (e.g., DRFLib.conf) is 
generated in the /etc/ld.so.conf.d/ directory and the *.so*
file path is added in the file and the corresponding library 
is set by executing the ldconfig command.

The following example describes how to register and link the **DRFL library** in a Linux environment.
Actual installation paths may vary depending on the user's workspace and Linux distribution.

.. note::
   The library installation path may differ depending on your workspace or system configuration.  
   When creating the ``.conf`` file, specify the **actual directory path** where the DRFL and Poco libraries are located.

.. code-block:: bash
   :linenos:

   ## 1. Verify the library path
   # Make sure the directory contains libDRFL, libPocoFoundation.so, and libPocoNet.so.
   ls /home/<user>/API-DRFL/library/Linux/64bits/amd64/{your_ubuntu_version}

   ## 2. Add a .conf file under /etc/ld.so.conf.d/
   # Replace the path below with your actual library directory.
   sudo nano /etc/ld.so.conf.d/drfl.conf
   # Add the following single line to the file, then save and exit:
   /home/<user>/API-DRFL/library/Linux/64bits/amd64/{your_ubuntu_version}

   ## 3. Register the library
   sudo ldconfig

   ## 4. Verify registration
   ldconfig -p | grep DRFL

   ## 5. Build a sample C++ file
   # Specify the proper include and library directories.
   g++ test.cpp -o test \
     -I/home/<user>/API-DRFL/include \
     -L/home/<user>/API-DRFL/library/Linux/64bits/amd64/{your_ubuntu_version} \
     -lDRFL -lpthread


Windows Library
~~~~~~~~~~~~~~~~~
The Windows library may not operate normally unless the Microsoft Visual C++ 2010 (x86) redistributable package is installed.

The project setting to use this API in the C++ project is as follows.

- **Setting of header file (include)**

``[Configuration Properties]->[C/C++]->[General]->[Additional Include Directories]``

.. image:: /tutorials/images/introduction/linking_window_attribute.png
   :alt: linking_window_attribute
   :width: 50% 
   :align: center 

.. raw:: html

   <br><br>

.. image:: /tutorials/images/introduction/linking_window_c++.png
   :alt: linking_window_c++
   :width: 100%
   :align: center

.. raw:: html

   <br>

- **Setting of library (lib) path**

``[Configuration Properties]->[Linker]->[General]->[Additional Library Directories]``

    .. image:: /tutorials/images/introduction/linking_window_linker.png
       :alt: linking_window_c++
       :width: 100%
       :align: center