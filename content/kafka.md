Title: kafka 

Since Kafka is a distributed system, topics are partitioned and replicated across multiple nodes.  Kafka treats each topic partition as a log (an ordered set of messages). Each message in a partition is assigned a unique offset.

Apache Kafka是分布式发布-订阅消息系统。它最初由LinkedIn公司开发，之后成为Apache项目的一部分。Kafka是一种快速、可扩展的、设计内在就是分布式的，分区的和可复制的提交日志服务

Kafka实际上是一个消息发布订阅系统。producer向某个topic发布消息，而consumer订阅某个topic的消息，进而一旦有新的关于某个topic的消息，broker会传递给订阅它的所有consumer。 在kafka中，消息是按topic组织的，而每个topic又会分为多个partition，这样便于管理数据和进行负载均衡。同时，它也使用了zookeeper进行负载均衡。
Kafka中主要有三种角色，分别为producer，broker和consumer。
