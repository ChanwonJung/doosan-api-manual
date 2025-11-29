.. _env_drcf_version:

1.3.2 DRCF Version Compatibility
--------------------------------

This code uses a preprocessor macro ``DRCF_VERSION`` to maintain compatibility 
with different versions of the **Doosan Robot Controller Framework (DRCF)**.

To specify your DRCF version:

- For DRCF v2: Set ``DRCF_VERSION`` to 2.
- For DRCF v3: Set ``DRCF_VERSION`` to 3.

**Example Usage:**

.. code-block:: cpp

   #ifndef DRCF_VERSION
       #define DRCF_VERSION 3  // Set to 3 for DRCF v3
   #endif

