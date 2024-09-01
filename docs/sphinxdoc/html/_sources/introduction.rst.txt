.. introduction.rst file for OSCAR Requirements PoC Manual

.. _introduction:

============
Introduction
============

Purpose
-------

This Manual is written in the first place to help the Points of Contact
(PoC) and Earth System Application Category (ESAC) Coordinators in
assigning new and editing existing variable requirements in the
OSCAR/Requirements database.

To keep it simple and well structured, this manual is organized as
follows:

-  | Information on how OSCAR/Requirements is *structured*
   | *it is important to know and understand the rationale behind this
     database and its functionalities*

-  | A *cookbook* on editing the database
   | *a step-by-step guide for the editor like a recipe to insert new
     and modify existing variables and the associated requirements
     details.*

-  | Background *references*
   | *Authoritative references and guidance material to help for a
     better understanding of the practices and rules behind OSCAR and
     the Roling Review of Requirements (RRR)*

-  | History
   | *A brief overview of the historic development of OSCAR/Requirements
     to better understand its structure and development*

-  | FAQ
   | *Frequently asked questions based on input from the editors (PoCs
     and Coordinators) raised during workshops and incoming e-mail
     request.*

Requirements for Observations
-----------------------------

The user requirements are not system-dependent; they are intended to be
technology-free. No consideration is given to what type of measurement
characteristics, observing platforms or data processing systems are
necessary (or even possible) to meet them. The requirements are aimed at
the WIGOS Vision time frame.

The basic structure used to record each individual requirement is shown
in the figure below. There are three basic elements needed to express
a requirement:

a.  the first element is to specify who wants the observation, this is
    one of the Application Areas together with a comment which may
    elaborate further, for example to identify a specific activity
    within the overall Application;

b.  the second element is to specify what the observation is,
    importantly this combines a geophysical variable with the place/s
    where it is to be observed within a defined list of 31 vertical
    layers and 8 types of horizontal coverage (requirements should only
    be expressed where it makes sense to do so);

c.  then the third element is to specify the performance level required
    for this observation for this user.

|figureI01| 

*Schematic diagram of the basic structure used to express an observation
requirement in the OSCAR/Requirements database.*

The Rolling Review of Requirements process
------------------------------------------

The Rolling Review of Requirements (RRR) process is defined by
the Manual on the WMO Integrated Global Observing
System (`WMO-No. 1160 <WMO1160_>`_, section 2.2.4, Appendix 2.3 and Attachment
3.1). The purpose of the RRR process is to provide a systematic and
transparent process to support the high-level design and evolution of
the WMO Integrated Global Observing System
(`WIGOS <WIGOS-link_>`_) aligned
with its `Vision in 2040 <VISION2040-link_>`_.
The RRR process compiles information about requirements for
observations, about observing system capabilities, their
cost-effectiveness, and draws on experts and impact studies to provide
guidance on the most important priorities for addressing the gaps
between requirements and capabilities, with consideration of WMO
priorities.

|figureI02| 

*RRR process diagram*

Structure of the OSCAR Requirements database
--------------------------------------------

The OSCAR Requirements database made available via the OSCAR weblinks is
in fact a Variables oriented (flat) database, but associated with or
ordered in specific Layers, Themes and the Application Areas. The list
of all requirements is a table containing for each variable the
associated items and the quantitative values associated with required
quality, performance and geographical availability. References to the
sources of these requirements are provided as well.

After entering the OSCAR Observation Requirements web page, several
weblinks are shown indicated as “tabs” (Overview \| Variables \|
Requirements \| Layers \| Themes \| Application Areas), which will
redirect to their specific themes. This Graphical User Interface (GUI)
structure is typical throughout the OSCAR Observations Requirements web
structure. Details of this structure and the further design of the
layout is explained in section “Structure” of this Manual.

Historic background
-------------------

Until about 1970 weather forecasting was primarily based on synoptic
observations. These observations were managed by the national weather
services. Weather stations reported at fixed time intervals (every 6 ort
3 hours) at fixed (synoptic) timestamps data expressed as quantities
(e.g. pressure) and weather phenomena (e.g. present weather). The
reported observations were performed in line with the requirements as
stated in the Manual on the GOS (`WMO-No. 544 <WMO544_>`_, discontinued), the Manual
on Codes (`WMO-No. 306 <WMO306_>`_) and in line with methods of observations as
recommended in the Guide to Instruments and Methods of Observations
(`WMO-No. 8 <WMO8_>`_). The set of reported quantities was relative limited, but
enough to generate the synoptic weather charts used for deterministic
forecast. Data was and is exchanged internationally as part of the World
Weather Watch programme. These activities were common practice for many
decades and can be regarded as the classical approach. Other aeras of
interest (climatology, hydrology, oceanography) followed in fact the
same practices. Typically, the user requirements were limited to this
classical set of variables and other types of observations, i.e. weather
phenomena visually observed (e.g. type of clouds). Also, the density of
the observing networks, particularly the Regional Basic Synoptic
Networks (RBSN) was regarded as acceptable, although certainly not
worldwide.

During the 1970’s two important developments were recognized: (1) New
large and fast computer systems became capable to calculate the state of
the atmosphere within a shorter time interval than the forecast (e.g.
within 24 hours), and (2) new earth observing satellites came into orbit
and delivered large amounts of numeric data in near real time
stimulating the numerical weather prediction development (NWP). It
became clear that satellite observations in combination with NWP
introduced a new phase in weather forecasting. This significant change
also affected the other areas of interest, and it became apparent that a
review of the current practices on observations was necessary. Because
observations by satellites are costly it was relevant to investigate the
best practices providing the most cost-effective results. The growing
satellite community therefore initiated and developed a policy focussing
or requirements, existing capabilities and gap analyses. This policy is
in fact the base of the Rolling Review of Requirements and the reference
for the vision of future developments of the WIGOS.

The requirements are formulated and kept up to date in
`OSCAR/Requirements <OSCAR-req_>`_. These requirements are essential to be able to
formulate the future approach and development of WIGOS and the system to
exchange data, satellite and surface based.

For some more details on the history of OSCAR, see the :doc:`History <history>` section.

Contact
-------

In case of comments or questions, please contact_ us by e-mail

|  
|  
|  

----------------------------------------------------------

:ref:`Goto top <introduction>`

----------------------------------------------------------

:Version: |version| (|today|)

:editor: `JPM`

:update: `2024-08-31 22:44 CEST`

:status: `TEST`


.. _WIGOS-link: https://community.wmo.int/en/activity-areas/WIGOS

.. _VISION2040-link: https://community.wmo.int/en/vision2040

.. _WMO1160: https://library.wmo.int/records/item/55063-manual-on-the-wmo-integrated-global-observing-system?language_id=15&offset=9

.. _OSCAR-req: https://space.oscar.wmo.int/observingrequirements

.. _WMO8: https://library.wmo.int/records/item/41650-guide-to-instruments-and-methods-of-observation?offset=2

.. _WMO544: https://library.wmo.int/records/item/58672-manual-on-the-global-observing-system-volume-i-global-aspects-discontinued?offset=2

.. _WMO306: https://library.wmo.int/records/item/35713-manual-on-codes-volume-i-1-international-codes?offset=2


.. introduction

.. |figureI01| image:: _static/fig-int-01.gif
   :width: 468px
   :height: 369px

.. |figureI02| image:: _static/fig-int-02.gif
   :width: 100 % 

.. vv 
   :width: 1403px
   :height: 992px
   :scale: 50 %
   
.. _contact: obs-rrr@wmo.int    

