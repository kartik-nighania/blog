Title: Build testing with Docker and VMs Week 9
Date: 2017-08-01 21:13:00
Tags: gsoc, docker
Author: Saurabh Gupta


Two matrix configurations were created under the name of "docker-matrix-test"  
and "docker-matrix-test-2". The former contains the configurations with clang 
version and the latter with gcc. They can be seen on Jenkins dashboard running
at [masterblaster.mlpack.org](http://masterblaster.mlpack.org)

Although, there are build failures due to size constraints. I am looking into
those now!