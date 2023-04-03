from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
import os


def upload_blob_file(path, name):

    account_key = os.getenv('AZURE_STORAGE_CONNECTION_STRING')

    connection_string = f"DefaultEndpointsProtocol=https;AccountName=storesocialmediajson;AccountKey={account_key};" \
                        f"EndpointSuffix=core.windows.net"

    blob_service_client = BlobServiceClient.from_connection_string(connection_string)

    container_name = "socialmedia"

    container_client = blob_service_client.get_container_client(container=container_name)
    with open(file=os.path.join(path, name), mode="rb") as data:
        blob_client = container_client.upload_blob(name="social-media-data.json", data=data, overwrite=True)
