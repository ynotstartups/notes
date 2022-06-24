# Docker In Action

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
