from urllib import request
from decouple import config
import api.lightning_pb2 as ln
import api.lightning_pb2_grpc as lnrpc
import grpc
import os
import codecs


os.environ["GRPC_SSL_CIPHER_SUITES"] = "HIGH+ECDSA"


macaroon_path = config("MACAROON_PATH")


def metadata_callback(context, callback):
    with open(os.path.expanduser(macaroon_path), "rb") as f:
        macaroon_bytes = f.read()
        macaroon = codecs.encode(macaroon_bytes, "hex")
    callback([("macaroon", macaroon)], None)


def node_connection():
    cert_path = config("CERT_PATH")
    cert = open(os.path.expanduser(cert_path), "rb").read()
    cert_creds = grpc.ssl_channel_credentials(cert)
    auth_creds = grpc.metadata_call_credentials(metadata_callback)
    combined_creds = grpc.composite_channel_credentials(cert_creds, auth_creds)
    channel = grpc.secure_channel("localhost:10009", combined_creds)
    stub = lnrpc.LightningStub(channel)
    return stub


