from grpc_client_utils import StubMaker

from idnorm_ddx.license_interceptors import LicenseInterceptorSync, LicenseInterceptorAsync
from idnorm_ddx.proto.ddx.v1.service_pb2_grpc import ExtractionStub
from idnorm_ddx.proto.ddx.v1.service_pb2 import ScanDocumentRequest, ScanConfig, ScanDocumentResponse


class ExtractionClientConfig:

    def __init__(self, *, url: str = 'ddx.idnorm.com:443', is_secure: bool = False, license_key: str):
        self.url = url
        self.license_key = license_key
        self.is_secure = is_secure


class ExtractionClient:

    def __init__(self, cfg: ExtractionClientConfig):
        stub, channel = StubMaker[ExtractionStub]().create(
            url=cfg.url,
            interceptors=[
                LicenseInterceptorSync(license_key=cfg.license_key),
            ],
        )
        self._stub = stub
        self._channel = channel
        self._closed = False

    def __enter__(self):
        if self._closed:
            raise RuntimeError('Client already closed')
        self._channel.__enter__()
        return self

    def __exit__(self, exc_type, exc, tb):
        self._channel.__exit__(exc_type, exc, tb)
        self.close()

    def scan_document(self, img_bytes: bytes, config: ScanConfig = ScanConfig()) -> ScanDocumentResponse:
        if self._closed:
            raise RuntimeError('Client already closed')
        request = ScanDocumentRequest(imageJpeg=img_bytes, config=config)
        response = self._stub.ScanDocument(request)
        return response

    def close(self):
        self._channel.close()
        self._closed = True

class ExtractionClientAsync:

    def __init__(self, cfg: ExtractionClientConfig):
        stub, channel = StubMaker[ExtractionStub]().create_async(
            url=cfg.url,
            interceptors=[
                LicenseInterceptorAsync(license_key=cfg.license_key),
            ],
        )
        self._stub = stub
        self._channel = channel
        self._closed = False

    async def __aenter__(self):
        if self._closed:
            raise RuntimeError('Client already closed')
        await self._channel.__aenter__()
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self._channel.__aexit__(exc_type, exc, tb)
        await self.close()

    async def close(self):
        await self._channel.close()
        self._stub = None
        self._channel = None
        self._closed = True

    async def scan_document(self, img_bytes: bytes, config: ScanConfig = ScanConfig()) -> ScanDocumentResponse:
        if self._closed:
            raise RuntimeError('Client already closed')
        request = ScanDocumentRequest(imageJpeg=img_bytes, config=config)
        response = await self._stub.ScanDocument(request)
        return response