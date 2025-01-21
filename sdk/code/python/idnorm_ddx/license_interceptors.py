import grpc
import grpc.aio as agrpc

# Custom interceptor to add metadata
class LicenseInterceptorSync(grpc.UnaryUnaryClientInterceptor):
    def __init__(self, license_key: str):
        self.metadata = [('vdil-license-key', license_key)]

    def intercept_unary_unary(self, continuation, client_call_details, request):
        # Create new client call details with added metadata
        new_metadata = []
        if client_call_details.metadata:
            new_metadata = list(client_call_details.metadata)
        new_metadata.extend(self.metadata)

        new_client_call_details = grpc.ClientCallDetails()

        new_client_call_details.method=client_call_details.method
        new_client_call_details.timeout=client_call_details.timeout
        new_client_call_details.credentials=client_call_details.credentials
        new_client_call_details.metadata=new_metadata
        new_client_call_details.wait_for_ready=client_call_details.wait_for_ready

        # Continue the request with updated metadata
        return continuation(new_client_call_details, request)

class LicenseInterceptorAsync(agrpc.UnaryUnaryClientInterceptor):
    def __init__(self, license_key: str):
        self.metadata = [('vdil-license-key', license_key)]

    async def intercept_unary_unary(self, continuation, client_call_details, request):
        # Create new client call details with added metadata
        new_metadata = []
        if client_call_details.metadata:
            new_metadata = list(client_call_details.metadata)
        new_metadata.extend(self.metadata)

        new_client_call_details = agrpc.ClientCallDetails(
            method=client_call_details.method,
            timeout=client_call_details.timeout,
            credentials=client_call_details.credentials,
            metadata=new_metadata,
            wait_for_ready=client_call_details.wait_for_ready
        )

        # Continue the request with updated metadata
        return await continuation(new_client_call_details, request)