comuneimola.compensi
====================

Compatibility
-------------

Tests have been made with:

 * Plone 3.3.5
 * Plone 4.2.1

Installation Notes
------------------
 * If you are installing the product for use with versions prior to plone 4, the version of collective.js.datatables in the buildout must be set to 1.9.
 * The translation feature of the table, missing in collective.js.datatables 1.9 has been put in the package and under the condition Plone < 4.

Operation
---------
Once the product is installed you can add "Fees Area" objects. Inside these objects, you can add "Fees" objects.

The display area is set to use a view based on collective.js.datatables.

A button allows you to download the contents of the table / folder in csv format.

A manager must create the area. We suggest to add collection portlets to the area, to find private fees and the fees to be reviewed, for the convenience of authenticated users.


Workflow
--------
As for the workflow of "Fee" objects, for now we decided to stay as close as possible to the simple publication wf of Plone.

The publisher of the document (Contributor role)
 * can add an entry
 * can add one or more links / attachments
 * can not change private items belonging to other publishers
 * may require the publication to any reviewer
 * can publish directly
 * once published:

  * can no longer revoke the publication
  * can not add / remove links / attachments.

The Editor role given by sharing, takes the form of a proxy to work on the "fee" object.

A Reviewer:
 * may withdraw an item published to correct the data entered, or modify them limited to those data not affecting the effectiveness of the contract.

"Manager" and "Site Administrator" can do everything, but still they should be used just in cases when only a superuser can solve a specific situation. Only these two roles can perform actions to delete, rename, cut and paste "fees".

To apply workflow actions (such as sending in revision and publication, back, etc..) to "fee" objects and its "Link" attachments (the "File" does not have any workflow, are public but follow the workflow of their container), you must use the "Advanced ..." function from the "state" menu.


Credits
-------

Developed by the `City of Imola`__

The City of Imola supports the `PloneGov initiative`__.

__ http://www.comune.imola.bo.it/
__ http://www.plonegov.it/


Authors
-------
The product was developed by

.. image:: http://www.redturtle.net/redturtle_banner.png
   :alt: RedTurtle Technology Site
   :target: http://www.redturtle.net/
