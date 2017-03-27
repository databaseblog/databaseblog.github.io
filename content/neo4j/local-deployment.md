Title: Neo4J - Local Deployment
Date: 2017-03-27 17:16
Category: Neo4J/Hosting

Before you can do anything with Neo4J, you need to have access to a running instance. This is relatively easy, but has some subtle differences to many other data stores.

The biggest thing to note is that a single Neo4J instance is a single database. There is no support - at present - for multiple schemas or databases inside the same instance. You can fake this, but it's really recommended to just have a different instance for each database you want to work with.

Installing Neo4J locally is a really trivial process. You need to have Java already installed - since the entire Neo4J system is a Java Application - and then you simply visit [Neo4J](https://neo4j.com/download/community-edition/) and download for your appropriate OS.

If you are using macOS, and you download the DMG version, you will get an application that drops into the Applications area, which - when run - will do everything to set up and execute the system. I assume that the Windows version is the same, but I've not tried it.

If you are using Linux, or the tar.gz version on macOS, you will instead get a relatively standard (for Linux) layout unpacked and ready to go. Inside the `bin` directory there is a `neo4j` shell script that works using standard `init.d` parameters. Starting Neo4J is as simple as:
```bash
$ ./bin/neo4j start
Starting Neo4j.
Started neo4j (pid 13196). It is available at http://localhost:7474/
There may be a short delay until the server is ready.
See /Users/coxg/Downloads/neo4j/neo4j-community-3.1.2/logs/neo4j.log for current status.
```

And stopping it is:
```bash
$ ./bin/neo4j stop
Stopping Neo4j.. stopped
```

In both cases, you then get a Web UI available on [http://localhost:7474](http://localhost:7474) that you can use to interact with the database directly, and you also get access to command line tools to do the same without a browser.

At this point, you're ready to go. There is a lot more that *can* be configured, but nothing that *must* be configured for it to work.
