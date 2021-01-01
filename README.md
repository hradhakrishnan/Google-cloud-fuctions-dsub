# dsub: Google cloud functions

## Overview

`dsub` is a command-line tool that makes it easy to submit and run batch scripts
in the cloud. The cloud function will demonstrate how to invoke dsub to execute pipeline jobs in Google cloud.

For this cloud functions - dsub example, we will run FastQC (https://www.bioinformatics.babraham.ac.uk/projects/fastqc/) as a docker container using lifesciences api against fastq files and store the QC report in a GCS bucket.

Also included the Docker file for FastQC. Use `Cloud build` to build the image and store it in the Google cloud `Container registry`
