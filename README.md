# List S3 Object URLs


Python utility that generates and lists object URLs within a defined S3 bucket.

## Usage

Run inside a virtual env

```
python3 -m venv env
source env/bin/activate
pip install boto3
```

Virtual-hosted style path
```
./s3_list_object_urls.py -b <bucket name>
```

Legacy Path-style formatting
```
./s3_list_object_urls.py -b <bucket name> -p
```


