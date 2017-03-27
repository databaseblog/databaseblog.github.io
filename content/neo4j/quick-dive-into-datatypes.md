Title: Neo4J - Quick Dive into Data Types
Date: 2017-03-27 17:16
Category: Neo4J

Neo4J offers two different types of data that it can store - Nodes and Relationships. Nodes are the actual real data entities in your application, and Relationships are the links between them.  The only difference between these two types of data is that a Relationship must be between two Nodes. Otherwise, anything you can represent on one you can represent on another.

Both Nodes and Relationships can also contain zero or more Labels, where a Label is simply a String tag that is used to identify the type of data being used. These will become important later when we are working with the data in our database, and also when we want to create schemas to restrict the data.

Both Nodes and Relationships can contain zero or more Properties, where a Property is simply a Key - which is always a String - and a Value - which is one of:

* Boolean
* Number
    * Byte - 8 bit Integer
    * Short - 16 bit Integer
    * Int - 32 bit Integer
    * Long - 64 bit Integer
    * Float - 32 bit IEEE-754 floating-point number
    * Double - 64 bit IEEE-754 floating-point number
* Char - UTF-16 Characters
* String
* Arrays of the above

One thing to note is that there is no support for any Time based data types. This may seem surprising, but it is not actually as restrictive as it may appear. The best options for this are to store it as an ISO-8601 string, or else as an offset since the epoch. The exact use here will depend on what you want to do with it. The String format allows for more information - such as timezone - to be included, but makes it difficult to do range queries. 

There is no technical limit to the number of properties or to the size of them. (Note, there will be realistic limits imposed by things such as storage space)

