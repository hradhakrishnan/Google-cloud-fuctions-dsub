# Google-cloud-fuctions-dsub- lifesciences API

## Overview

 This Google cloud function demonstrates how to take a serverless approach to automate execution of pipeline jobs. e.g running QC checks on incoming fastq files using FastQC.

 The functions uses databiosphere `dsub`, containerized tools (`FastQC`) and `Google cloud lifescience API` to automate execution of pipeline jobs. The function can be easily modified to adopt to other bioinformatic tools out there.

`dsub` is a command-line tool that makes it easy to submit and run batch scripts
in the cloud. The cloud function will demonstrate how to invoke dsub to execute pipeline jobs in Google cloud.

we will run `FastQC` (credit to https://www.bioinformatics.babraham.ac.uk/projects/fastqc/) as a docker container using `lifesciences API` against fastq files and store the QC reports generated in a GCS bucket.

`Cloud Life Sciences API` provides a simple way to execute a series of Compute Engine containers on Google Cloud.


Also included the Docker file for FastQC. Use `Cloud build` to build the image and store it in the Google cloud `Container registry`

![alt text](https://github.com/hradhakrishnan/Google-cloud-fuctions-dsub/blob/master/fastqc_gcp.png)
