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
