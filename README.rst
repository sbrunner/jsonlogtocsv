Json log to csv
===============

The goal of this project is to convert a json log into a csv file.

The json log is a file with one json per line.

Manage special cases for the attribute ``position``, ``bbox``, and ``layers`` that we needs in geospatial world.


------
Get it
------

Install::

    virtualenv buildout
    ./buildout/bin/pip install jsonlogtocsv

-------------
Example Usage
-------------

.. code::

   ./buildout/bin/jsonlogtocsv --filter layers[l1]=True example.jsonlog id example.csv

Creates the CSV file with:

.. code::

   id
   1
   2

.. code::

   ./buildout/bin/jsonlogtocsv example.jsonlog id,layers[l1] example.csv

Creates the CSV file with:

.. code::

   id,layers[l1]
   1,True
   2,True
   3,

.. code::

   ./buildout/bin/jsonlogtocsv --filter id=2 example.jsonlog bbox example.csv

Creates the CSV file with:

.. code::

   bbox
   "[1, 20, 3, 40]"

.. code::

   ./buildout/bin/jsonlogtocsv --filter id=2 example.jsonlog bbox[0],bbox[1],bbox[2],bbox[3] example.csv

Creates the CSV file with:

.. code::

   bbox[0],bbox[1],bbox[2],bbox[3]
   1,20,3,40

.. code::

   ./buildout/bin/jsonlogtocsv --filter id=2 example.jsonlog bbox_center example.csv

Creates the CSV file with:

.. code::

   bbox_center
   "[2, 30]"


-----------
From source
-----------

Build it::

    python bootstrap.py
    ./buildout/bin/buildout
