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


def add_routes(api, transformer_manager, rabbit_mq_adaptor):
    from servicex import servicex_resources
    from servicex.resources.submit_transformation_request import SubmitTransformationRequest
    from servicex.resources.transform_start import TransformStart

    SubmitTransformationRequest.make_api(rabbit_mq_adaptor)
    api.add_resource(SubmitTransformationRequest, '/servicex/transformation')

    api.add_resource(servicex_resources.QueryTransformationRequest,
                     '/servicex/transformation/<string:request_id>',
                     '/servicex/transformation')
    api.add_resource(servicex_resources.TransformationStatus,
                     '/servicex/transformation/<string:request_id>/status')

    servicex_resources.AddFileToDataset.make_api(rabbit_mq_adaptor)
    api.add_resource(servicex_resources.AddFileToDataset,
                     '/servicex/transformation/<string:request_id>/files')

    servicex_resources.PreflightCheck.make_api(rabbit_mq_adaptor)
    api.add_resource(servicex_resources.PreflightCheck,
                     '/servicex/transformation/<string:request_id>/preflight')

    api.add_resource(servicex_resources.FilesetComplete,
                     '/servicex/transformation/<string:request_id>/complete')

    TransformStart.make_api(transformer_manager)
    api.add_resource(TransformStart, '/servicex/transformation/<string:request_id>/start')

    servicex_resources.TransformerFileComplete.make_api(transformer_manager)
    api.add_resource(servicex_resources.TransformerFileComplete,
                     '/servicex/transformation/<string:request_id>/file-complete')
