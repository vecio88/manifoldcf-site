Apache ManifoldCF Website
=============================

This is the source of the Apache ManifoldCF team's website, 
found at https://manifoldcf.apache.org/

## How to build the ManifoldCF Site:

This builds the website and puts its pages in output/

```bash
virtualenv $venvname
source $venvname/bin/activate
pip install -r requirements.txt

git pull origin master

# Edit all the markdown! (manifoldcf-site/content/pages/)

pelican -t theme
```

To preview:

```bash
cd output/
python -m pelican.server
# Browse to localhost:8000
```

## How to build the ManifoldCF Site From Docker Container:

After you clone the project on your system, in the project root dir, you can find a DockerFile. Build this with command

```bash
docker build -t image_name .
```

Docker it will create an image with the name you have specified.

For create a container based on the image previusly created, run this command

```bash
docker run --name my-container-name -v=path\project\mySystem:/app -p 8001:8000 -it image_name
```

```bash
virtualenv $venvname
source $venvname/bin/activate
pip install -r requirements.txt

git pull origin master

# Edit all the markdown! (manifoldcf-site/content/pages/)

pelican -t theme
```

To preview:

```bash
cd output/
python -m pelican.server
# Browse to localhost:8000
```

`-v` is important because  it allows us to see from the container the local dir, and we can modify the project in local and have the same file on the container too, without to do files copy from local to container and vice versa 

Now the container is been created, we can exec a terminal on this with docker exec command

```bash
docker exec -it my-container-name bash 
```
Now the container started from the /app folder, and you can see all project file. From this folder you can generate the output file and launch the pelican server for the rendering of the site.

```bash
# Edit all the markdown! (manifoldcf-site/content/pages/)

pelican -t theme
```

To preview:

```bash
cd output/
python -m pelican.server
# Browse to localhost:8000
```

## Technical site documentation:
Any time you check in a file, the site regenerates:
https://ci2.apache.org/#/builders/3

## Preparation
The `gfm_reader.py` script points to a specific directory on
bb-slave1 for loading the `libcmark-gfm.so` and `libcmark-gfmextensions.so`
libraries. The path should be adjusted for your local installation.

Run `build_cmark.sh` to build the two libraries. It is
then helpful to create a directory (say, `build_cmark/lib`) with
two symlinks from the `.so` to the longer, version-specific libraries
that the above shell script builds.

## Preview PRs
To stage a preview of what a PR would result in, be sure to name your branches 
using the `preview/$foo` syntax, for instance `preview/cleanup-dec-2021`. This 
will auto-build and -stage your changes and make them available at 
`manifoldcf-$foo.staged.apache.org`, i.e. `manifoldcf-cleanup-dec-2021.staged.apache.org`

