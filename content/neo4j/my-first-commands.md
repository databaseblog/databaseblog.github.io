Title: Neo4J - My First Commands
Date: 2017-03-28 12:54
Category: Neo4J

Once you've got access to a Neo4J instance, you're going to want to do something with it. It's not much use otherwise. This will show some very basic commands, and show what you can expect to get out of this system with virtually no effort.

All of the examples here are going to be using the command line `cypher-shell` simply because it renders better in text form. You can do everything in the Web UI as well.

### Creating a node
Creating a node can be achieved using the `CREATE` command. 
```
neo4j> CREATE (n);
Added 1 nodes
```

This creates a new Node, with no properties or labels associated with it. It's pretty boring, but it works. Note that the definition of the Node is wrapped in parenthesis. Every time you declare a Node you will do this.

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

### Retrieving a node
Once a node has been created, you can then retrieve it. This is done with the MATCH command.
```
neo4j> MATCH (n) RETURN n;
n
()
(:User {username: "graham"})
```

This output is not the most obvious to read, but it displays two Nodes that were returned - the two that we've just created. The first one has no labels and no properties, and the second has a single label - User - and a single property - username: "graham".

This can be extended to match on certain criteria, by specifying it in the nodes that you want to match. For example:
```
neo4j> MATCH (n:User) RETURN n;
n
(:User {username: "graham"})

neo4j> MATCH (n {username: "graham"}) RETURN n;
n
(:User {username: "graham"})

neo4j> MATCH (n:User {username: "graham"}) RETURN n;
n
(:User {username: "graham"})
```

Two different queries, matching in two different ways, but both return the same one node. The first of these queries will return all nodes that have a label of "User", but doesn't care about any other data. The second of these will return all nodes that have a property of "username" that has a value of "graham", but also doesn't care about any other data. These can of course be combined as much as needed to get the matches you want.

This is all very good, but it only gives a very limited support for matching. We can match on exactly the data we want being present, but nothing more complicated. For this we can make use of the WHERE clause to the MATCH command. This gives us full boolean logic for complete matching control, the same as in any other database engihe. However, this can be very powerful when we start doing matching across multiple nodes as we will later see.

For a simple example here, we can re-write the above queries using the WHERE clause as follows:
```
neo4j> MATCH (n) WHERE n:User RETURN n;
n
(:User {username: "graham"})

neo4j> MATCH (n) WHERE n.username = "graham" RETURN n;
n
(:User {username: "graham"})

neo4j> MATCH (n) WHERE n:User AND n.username = "graham" RETURN n;
n
(:User {username: "graham"})
```

These all return exactly the same as the ones above, but using a different structure that may be more familiar. Where this gets better is when we start to do more complicated matches. For example, we might want all nodes that have a username, but not care what it is:
```
neo4j> MATCH (n) WHERE exists(n.username) RETURN n;
n
(:User {username: "graham"})
```

### Creating a relationship
Now that we can create and retrieve Nodes, we want to work with Relationships. After all, that's the entire point of a Graph Database. Not surprisingly, these are also really easy to work with. Firstly though, we'll create some more data to work with:
```
neo4j> CREATE (c:Character {name: 'Bob'});
Added 1 nodes, Set 1 properties, Added 1 labels
```

And now that we've got a User node and a Character node, we'll tell the system that the User is the OWNER of the Character.
```
neo4j> MATCH (u:User), (c:Character) CREATE (u)-[:OWNER]->(c);
Created 1 relationships
```

There's a lot going on here. Firstly you'll notice that we have both a MATCH and a CREATE command in the same statement. This is a method of chaining the output of one command into the next one. Secondly, you'll notice that the MATCH command is returning two different, distinct nodes. There's no reason not to do this, and you can return as many as you need. Finally, you'll notice the syntax for the CREATE statement is a little bit different to before. In this case, what we are creating is the relationship between to nodes that we've already matched. You'll also see that the CREATE statement re-uses the tags that we gave the nodes in the MATCH statement. This is used by the system to know that these are not new nodes to be created, but existing ones to re-use. As it happens, you can create nodes and relationships all in one go if you desire, simply by defining them in the CREATE instead of re-using them from a MATCH.

You'll note here that the definition of the Relationship is inside square brackets, and has lines on either side. In fact, what we've got here is a directional relationship, which is why the lines look like an arrow. You can draw the arrow either way around, and it will work as expected. You can also leave the arrowhead off altogether and have a non-directional relationship. These are all perfectly valid, and slightly different to each other, so you'll want to make sure you use the correct one for your data.

### Retrieving relationships
Now that we've got a relationship, we want to make use of it. Lets start with the obvious one - all of the Characters that belong to the User "graham":
```
neo4j> MATCH (u:User {username:"graham"})-[r:OWNER]->(c:Character) RETURN c;
c
(:Character {name: "Bob"})
```

It really is as simple as that. We're specifying a MATCH command, where we want to Match a "User" node that has a property "username" equal to "graham". We want to traverse from this node across a Relationship with a label of "OWNER" to the target "Character" nodes, and we want to return the Character nodes. In this case theres only one, but there might be lots more.

All of the filtering that we user before can be used at any part of this match. We've filtered the relationship by label, but can equally do so by properties, and we can do so with WHERE clauses too.
