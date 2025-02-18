# Copyright (c) 2019, IRIS-HEP
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# * Redistributions of source code must retain the above copyright notice, this
#   list of conditions and the following disclaimer.
#
# * Redistributions in binary form must reproduce the above copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.
#
# * Neither the name of the copyright holder nor the names of its
#   contributors may be used to endorse or promote products derived from
#   this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.


class ObjectStoreManager:

    def __init__(self, url, username, password, use_https=False):
        from minio import Minio
        self.minio_client = Minio(endpoint=url, access_key=username,
                                  secret_key=password, secure=use_https)

    def create_bucket(self, bucket_name):
        self.minio_client.make_bucket(bucket_name)

    def list_buckets(self):
        return self.minio_client.list_buckets()

    def delete_bucket_and_contents(self,  bucket_name):
        if not self.minio_client.bucket_exists(bucket_name):
            print(f"Bucket '{bucket_name}' does not exist. Nothing to delete.")
            return

        # List all objects in the bucket
        objects = self.minio_client.list_objects(bucket_name, recursive=True)

        # Remove each object
        for obj in objects:
            self.minio_client.remove_object(bucket_name, obj.object_name)

        # Remove the bucket itself
        self.minio_client.remove_bucket(bucket_name)
        print(f"Bucket '{bucket_name}' deleted successfully.")
