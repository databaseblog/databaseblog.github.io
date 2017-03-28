Title: Neo4J - My First Commands
Date: 2017-03-27 18:54
Category: Neo4J
Status: draft

Once you've got access to a Neo4J instance, you're going to want to do something with it. It's not much use otherwise. This will show some very basic commands, and show what you can expect to get out of this system with virtually no effort.

All of the examples here are going to be using the command line `cypher-shell` simply because it renders better in text form. You can do everything in the Web UI as well.

### Creating a node
Creating a node can be achieved using the `CREATE` command. 
```
neo4j> CREATE (n);
Added 1 nodes
```

This creates a new Node, with no properties or labels associated with it. It's pretty boring, but it works.

A more interesting node would be one with a Label, and some associated data. Let's create a User record for some made up game.
```
neo4j> CREATE (u:User {username:'graham'});
Added 1 nodes, Set 1 properties, Added 1 labels
```
There. It really is that simple.

Note that this breaks down into a number of parts, as follows:

* `CREATE` - This is the command being executed
* `u` - This is just a local tag for this command to represent this node. It must be unique, but it doesn't matter what it is.
* `:User` - This is a Label associated with the newly created Node
* `{username:'graham'}` - This is the properties of the node

