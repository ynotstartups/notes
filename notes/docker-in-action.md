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
