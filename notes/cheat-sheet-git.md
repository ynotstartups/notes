# Cheat Sheet Git

## How many images can I put in repo for github?

[Github](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github#repository-size-limits) recommends repo to have size ideally less than 1 GB, and less than 5GB is strongly recommended.

Looking at existing images in this repo, an jpg is in average 3M. If I use the 5GB recommended size, I can store 1706 (5GB/3M) images, which is a large amount of images until I exceed that limit.

## Find repo size

```
$ git bundle create tmp.bundle --all
$ du -sh tmp.bundle

52M	tmp.bundle

```

See more in [stackoverflow](https://stackoverflow.com/questions/8185276/find-size-of-git-repository)


