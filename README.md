# Document data extraction

This repository holds documentation and resources to help developers
get started with our identity document data extraction service.

This service allows you to analyse identity documents images
and extract data present in the document in a structured format.

## Cloud SaaS

The extraction service is available as an API hosted on `ddx.idnorm.com`. It implements RESTful and gRPC APIs one can use
for service integration.

## Hosting it on-premise

Our extraction service can be hosted on your infrastructure. We provide two main deployment options
 - smaller scale and testing solutions can be effortlessly deployed using our prepared [docker-compose configuration](onprem/docker-compose).
 - for production purposes, where horizontal scaling is "a must", we release and maintain the helm chart package.

# Quick start

If you don't want to read a bunch of documentation and want to
send a request in-code ASAP, you can go straight away to the [example
code snippets](sdk/README.md) you can use to get a working integration within a few minutes.

# API integration

Both Cloud SaaS and On-premise solutions use the same APIs. For integration
we offer gRPC and REST APIs you can use to communicate with the service. To reduce integration complexity we also
release and maintain code SDKs that should make integration to your programming language of choice as easy
as adding one more package dependency. For more information please follow [coding libraries section](sdk/README.md).

## gRPC

Focusing on performance, readability, and ease of code integration we recommend using gRPC whilst integrating our
extraction solution. Working with gRPC and protobuf for the first time can have a challenging learning curve.
To make working with gRPC enjoyable and easy we leverage [buf build tool](https://buf.build/docs/introduction). Here we will provide more information on how to use it to integrate our solution.

Simply put, Buf is a tool that helps configure and execute [protoc](https://grpc.io/docs/protoc-installation/) plugins to generate code you can then easily use to integrate our gRPC service with your codebase.

Buf also provides us with his [protobuf schema registry](https://buf.build/explore) where one can publish its gRPC/protobuf service schema definitions. You can think of it as a "git" for protobuf schema definitions.

On the bufs schema registry, we publish our service definitions.

### ID extraction service schema
**The latest version** of our service schema can be found [here](https://buf.build/idnorm/ddx/docs/main:proto.ddx.v1).

There you can see detailed documentation on the available methods service defines, as well as input and output messages. There you can find all information about input data requirements, what is the expected result the service will return, as well as different options for request configurations.

## REST

REST is, arguably, still the most popular choice for building backend services APIs. Therefore, our ID extraction service comes with REST as well as gRPC API.

API documentation is maintained and shipped using Swagger. You can browse the documentation [here](todo) as it is hosted using Swagger UI.

Same as with gRPC, in the documentation you can find all the details about available paths, expected request and response payloads, and different request configuration options.
