.. _env_linux:

1.3.4 Linux (Ubuntu) Environment (64-bit)
------------------------------------------

.. note::
   - **Supported Ubuntu Versions:** 18.04, 20.04, 22.04, 24.04
   - **Supported Architectures:** x86_64, ARM64  
   - **Simulator:** RViz (ROS2 visualization tool)  
   - Ensure ROS2 (Humble or compatible) and RViz2 are properly installed.

A. Create a workspace
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block:: bash

   mkdir -p ~/api_ws/src
   cd ~/api_ws/src

B. Clone the DRFL repository
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Clone the official DRFL repository and move into the example directory.

.. code-block:: bash

   git clone https://github.com/doosan-robotics/API-DRFL.git
   cd API-DRFL/example/Linux_64

C. Install required dependencies
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Before building, install the required Poco development libraries.

.. code-block:: bash

   sudo apt update
   sudo apt-get install libpoco-dev

D. Launch Simulator (Virtual Mode)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Before building and running the example, you must start the **RViz simulator** using **Docker** and **ROS2**.

Open a new terminal and launch the Doosan RViz simulator in **virtual mode**. Keep this terminal running, it will act as your robot simulator.

.. code-block:: bash

      cd ~/ros2_ws
      ros2 launch dsr_bringup2 dsr_bringup2_rviz.launch.py mode:=virtual host:=127.0.0.1 port:=12345 model:=m0609

**Explanation:**

- ``mode:=virtual`` : Runs in virtual (simulation) mode  
- ``host:=127.0.0.1`` : Localhost connection  
- ``port:=12345`` : Default controller/emulator port  
- ``model:=m0609`` : Selects robot model (e.g., M0609)

.. note::
   - If you are connecting to a **real robot**, replace the parameters accordingly:

     .. code-block:: bash

        ros2 launch dsr_bringup2 dsr_bringup2_rviz.launch.py mode:=real host:=192.168.137.100 port:=12345 model:=m0609

     - Make sure your robot controller and PC are in the same network subnet.  
     - The robot must be in **Auto (Remote)** mode to accept API commands.

.. tip::
   Before running the build script, confirm that **Docker** and the **virtual port (12345)** are active:

   .. code-block:: bash

      sudo docker ps
      nc -vz 127.0.0.1 12345

   - If the above commands show an active container and successful connection,  
     the simulator is running correctly and ready for API communication.  
   - The build script should be executed **after** launching the RViz simulator,  
     as it depends on the active socket port (12345).

E. Build the project
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Now return to your API workspace terminal and build the DRFL example.

.. code-block:: bash

   ./API_DRFL_BUILD.sh

This script automatically:

- Detects your Ubuntu version and architecture  
- Scans all ``.cpp`` files in the directory  
- Allows you to select which file to build (1, 2, 3...)  
- Handles library linking automatically  
- Creates executables in the ``out/`` directory  
- Optionally runs the built executable

.. tip::
   If you encounter a *connection failure* after building, double-check: |br|
   1. Your IP address in the source file (must match the robot or emulator). |br| 
   2. That the controller or DART emulator is running on port **12345/TCP**.  |br|
   3. Network access is not blocked by firewall or Docker isolation.

**Clean Script**

To remove build artifacts and executables:

.. code-block:: bash

   ./API_DRFL_CLEAN.sh

This script:

- Removes all ``.o`` object files  
- Removes the ``out/`` directory and all executables  
- Asks for confirmation before cleaning

.. tip::
   The automated build scripts are the fastest and safest way to compile DRFL examples,  
   especially if you are switching between Ubuntu versions or CPU architectures.

.. raw:: html
      
   <br>

.. .. image:: /tutorials/images/introduction/ubuntu_demo.gif
..    :alt: ubuntu_demo
..    :width: 120%
..    :align: center

.. .. raw:: html
      
..    <br><br>


F. Manual build (alternative)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you prefer to compile manually, use ``g++`` according to your Ubuntu version and architecture.

*Ubuntu supports versions*: 18.04, 20.04, 22.04 and 24.04.

**x86 (Ubuntu 18.04)**

.. code-block:: bash

   g++ -c main.cpp
   g++ -o drfl_test main.o ../../library/Linux/64bits/amd64/18.04/libDRFL.a \
       /usr/lib/libPocoFoundation.so /usr/lib/libPocoNet.so

**x86 (Ubuntu 20.04 / 22.04 / 24.04)**

.. code-block:: bash

   g++ -c main.cpp
   g++ -o drfl_test main.o ../../library/Linux/64bits/amd64/{your_ubuntu_version}/libDRFL.a \
       /usr/lib/x86_64-linux-gnu/libPocoFoundation.so \
       /usr/lib/x86_64-linux-gnu/libPocoNet.so

**ARM64 (Ubuntu 18.04)**

.. code-block:: bash

   g++ -c main.cpp
   g++ -o drfl_test main.o ../../library/Linux/64bits/arm64/18.04/libDRFL.a \
       /usr/lib/libPocoFoundation.so /usr/lib/libPocoNet.so

**ARM64 (Ubuntu 20.04 / 22.04 / 24.04)**

.. code-block:: bash

   g++ -c main.cpp
   g++ -o drfl_test main.o ../../library/Linux/64bits/arm64/{your_ubuntu_version}/libDRFL.a \
       /usr/lib/aarch64-linux-gnu/libPocoFoundation.so \
       /usr/lib/aarch64-linux-gnu/libPocoNet.so

.. note::
   Although library versions traditionally differed across Ubuntu releases, Ubuntu 24.04 now uses the same **.80** version as Ubuntu 22.04 for compatibility.