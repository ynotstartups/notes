# Docker In Action

## Question?

- What does `PublishMode: ingress` mean in docker service?
  - ingress handles traffics from outside of the docker swarm

## Page 158

Docker layers are collections of the changes made in union file system layer + metadata/context.
\- union file system is made up of layers
\- metadata/context are is such as environment variables...

```bash
docker container run --name mod_busybox_delete busybox:latest rm /etc/passwd
docker container diff mod_busybox_delete
```

This time, the output will have two rows:

C /etc
D /etc/passwd

The D indicates a deletion, but this time the parent folder of the file is also included.
The C indicates that it was changed.

## Page 161

An image is the collection of layers produced by traversing the parent graph
from a top layer.

## Linux Tip To See What's Change After A Command

```bash
docker container run --name diff-add-git --entrypoint /bin/bash ubuntu -c "apt-get update && apt-get install -y git"

docker container diff diff-add-git
```

## Page 164

design for attributes such as size and cacheability

## Page 166

Create an empty folder and copy the following code into a new file named
helloworld.go:

```go
package main
import "fmt"
func main() {
 fmt.Println("hello, world!")
}
```

Compile and statically link, which means it can run all by itself and place that program back into your folder

```bash
docker container run --rm -v "$(pwd)":/usr/src/hello \
 -w /usr/src/hello golang:1.9 go build -v
```

## Page 169 Summary

- New images are created when changes to a container are committed using the
- docker container commit command.
- An image is a stack of layers that’s identified by its top layer.
- An image’s size on disk is the sum of the sizes of its component layers.
- Images can be exported to and imported from a flat tarball representation by using the docker container export and docker image import commands.

## 187

Example for multi stage build

```dockerfile
FROM golang:1-alpine as builder

RUN apk update && apk add ca-certificates

ENV HTTP_CLIENT_SRC=$GOPATH/src/dia/http-client/
COPY . $HTTP_CLIENT_SRC
WORKDIR $HTTP_CLIENT_SRC

RUN CGO_ENABLED=0 GOOS=linux GOARCH=amd64 go build -v -o /go/bin/http-client

# ----

# See this FROM as
FROM scratch as runtime
ENV PATH="/bin"
# See this COPY --from
COPY --from=builder /etc/ssl/certs/ca-certificates.crt /etc/ssl/certs/ca-certificates.crt
COPY --from=builder /go/bin/http-client /http-client
ENTRYPOINT ["/http-client"]
```

## 197

SUID and SGID permissions

The well-known filesystem permissions (read, write, execute) are
only a portion of the set defined by Linux. In addition to those, two are of particular
interest: SUID and SGID.

These two are similar in nature. An executable file with the SUID bit set will always
execute as its owner. Consider a program like /usr/bin/passwd, which is owned by the
root user and has the SUID permission set. If a nonroot user such as bob executes
passwd, he will execute that program as the root user.

## 201

**Image Distribution Spectrum**

from simple/restrictive to complicated/flexible

- hosted registry with public repositories e.g. public docker hub
- hosted registry with private repositories e.g. private docker hub
- private repositories e.g. amazon ECR private container repository
- custom image distribution infrastructure
- image source distributions

**Selection criteria**

When making a decision, consider how important each of these is in your situation:

- Cost
- Visibility
- Transport speed or bandwidth overhead
- Longevity control
- Availability control
- Access control
- Artifact integrity
- Artifact confidentiality
- Requisite expertise

## 250

```json
[
    {
        "ID": "qpb18wpdf63qk4lkrg2zgfw64",
        "Version": {
            "Index": 12
        },
        "CreatedAt": "2022-06-25T08:13:39.032086605Z",
        "UpdatedAt": "2022-06-25T08:13:39.053408876Z",
        "Spec": {
            "Name": "hello-world",
            "Labels": {},
            "TaskTemplate": {
                "ContainerSpec": {
                    "Image": "dockerinaction/ch11_service_hw:v1",
                    "Init": false,
                    "StopGracePeriod": 10000000000,
                    "DNSConfig": {},
                    "Isolation": "default"
                },
                "Resources": {
                    "Limits": {},
                    "Reservations": {}
                },
                "RestartPolicy": {
                    "Condition": "any",
                    "Delay": 5000000000,
                    "MaxAttempts": 0
                },
                "Placement": {},
                "ForceUpdate": 0,
                "Runtime": "container"
            },
            "Mode": {
                "Replicated": {
                    "Replicas": 1
                }
            },
            "UpdateConfig": {
                "Parallelism": 1,
                "FailureAction": "pause",
                "Monitor": 5000000000,
                "MaxFailureRatio": 0,
                "Order": "stop-first"
            },
            "RollbackConfig": {
                "Parallelism": 1,
                "FailureAction": "pause",
                "Monitor": 5000000000,
                "MaxFailureRatio": 0,
                "Order": "stop-first"
            },
            "EndpointSpec": {
                "Mode": "vip",
                "Ports": [
                    {
                        "Protocol": "tcp",
                        "TargetPort": 80,
                        "PublishedPort": 8080,
                        "PublishMode": "ingress"
                    }
                ]
            }
        },
        "Endpoint": {
            "Spec": {
                "Mode": "vip",
                "Ports": [
                    {
                        "Protocol": "tcp",
                        "TargetPort": 80,
                        "PublishedPort": 8080,
                        "PublishMode": "ingress"
                    }
                ]
            },
            "Ports": [
                {
                    "Protocol": "tcp",
                    "TargetPort": 80,
                    "PublishedPort": 8080,
                    "PublishMode": "ingress"
                }
            ],
            "VirtualIPs": [
                {
                    "NetworkID": "icjrjs9krq231yn647ih6w0gt",
                    "Addr": "10.0.0.3/24"
                }
            ]
        }
    }
]
```

The difficulty of running a service is, by definition, more about managing
availability of something on a network.

So it shouldn’t be too surprising that a service
definition is predominantly about how to run replicas, manage changes to the software, and route requests to the service endpoint to that software.

run three replicas of hello-world service

`docker service scale hello-world=3`

global, tells Docker to run one replica on each node in the swarm cluster.
Services in global mode are useful for maintaining a common set of
infrastructure services that must be available locally on each node in a
cluster.

## 257

Comment support is one of the most popular reasons to adopt YAML instead of
JSON today.

## 260

Docker stack is a named collection of services, volumes, networks, secrets, and configs.

The docker stack subcommands manage stacks.

## 271

Most application authors do not want to change the program’s source code and
rebuild the application each time they need to vary the behavior of an
application.  Instead, they program the application to read configuration
data on startup and adjust its behavior accordingly at runtime.

## 284

**Problems with secrets as environment variables**

The most important and common problems with using environment variables as
secret transfer mechanisms are as follows:
\- You can’t assign access-control mechanisms to an environment variable.
\- This means any process executed by the application will likely have access to
those env vars. To illustrate this, think about what it might mean for an application that does image resizing via ImageMagick to execute resizing operations
with untrusted input in the environment containing the parent application’s
secrets. If the environment contains API keys in well-known locations, as is
common with cloud providers, those secrets could be stolen easily. Some languages and libraries will help you prepare a safe process execution environment, but your mileage will vary.
\- Many applications will print all of their environment variables to standard out
when issued a debugging command or when they crash. This means you may
expose secrets in your logs on a regular basis.
