import subprocess

def ngs_qc_trigger(event, context):

    """
    Cloud function that uses dsub (https://github.com/DataBiosphere/dsub) to execute
    pipeline jobs using lifesciences api in GCP.

    GCS EVENT TRIGGER:
    Triggered by a change to a Cloud Storage bucket.
    Function is triggered when a (e.g Fastq) file is added to a GCS bucket.
    The trigger event and bucket to be selected during the function creation

    Requirements:
    dsub is included in the requirements.txt and gets installed through pip
    Enable lifescience API for your GCP project if you havent already

    Python libraries:
    function executes dsub as a python subprocess. The function uses subprocess packaged already with python 3.8

    Args:
    To be defined: GCP_PROJECT,GCS_INPUT_BUCKET,GCS_OUTPUT_BUCKET,GCS_LOG_LOCATION,CONTAINER_IMAGE
    Based on the file events, variables around file name, path and bucket information are pulled from the event info
    """

    # file name and bucket information derived from GCS triger event
    file = event
    GCS_INPUT_BUCKET = file['bucket']
    GCS_INPUT_FASTQ_FILE = file['name']

    # User input fields <xxx>, to be updated with your GCP info
    GCP_PROJECT = "<YOUR-GCP-PROJECT-ID>"
    GCS_OUTPUT_BUCKET = "gs://<OUTPUT-GCS-BUCKET>"
    GCS_LOG_LOCATION = "gs://<LOGS-GCS-BUCKET>/logs"
    CONTAINER_IMAGE = "gcr.io/<FASTQ-CONTAINER-IMAGE>"
    REGION = "<LOCATION e.g: europe-west2>"

    print(f"Processing fastq file: {GCS_INPUT_FASTQ_FILE}.")

    DSUB_PARAMS = f"dsub --provider google-cls-v2 --project {GCP_PROJECT} --logging {GCS_LOG_LOCATION} --location {REGION} --input FASTQ=gs://{GCS_INPUT_BUCKET}/{GCS_INPUT_FASTQ_FILE} --output HTML={GCS_OUTPUT_BUCKET}/*  --image {CONTAINER_IMAGE}  "
    FASTQ_COMMAND = "--command 'fastqc ${FASTQ} --outdir=$(dirname ${HTML})' --wait"
    SP_COMMAND = DSUB_PARAMS + FASTQ_COMMAND
    #submitting dsub job
    p = subprocess.run(SP_COMMAND, shell=True)
    print("Submitting dsub job to lifesciences API")
    print(p)
