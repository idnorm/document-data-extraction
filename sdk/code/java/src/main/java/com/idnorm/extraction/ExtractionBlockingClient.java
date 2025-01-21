package com.idnorm.extraction;

import com.google.protobuf.ByteString;
import proto.ddx.v1.ExtractionGrpc;
import proto.ddx.v1.Service;

public class ExtractionBlockingClient {

    private final ExtractionGrpc.ExtractionBlockingStub stub;

    protected ExtractionBlockingClient(ExtractionGrpc.ExtractionBlockingStub stub) {
        this.stub = stub;
    }

    public static ExtractionClientBuilder<ExtractionBlockingClient> builder() {
        return new ExtractionClientBuilder<>(c -> new ExtractionBlockingClient(ExtractionGrpc.newBlockingStub(c)));
    }

    public Service.ScanDocumentResponse scanDocument(ByteString imgData) {
        return stub.scanDocument(Service.ScanDocumentRequest.newBuilder()
                .setImageJpeg(imgData)
                .build());
    }

    public Service.ScanDocumentResponse scanDocument(ByteString imgData, Service.ScanConfig cfg) {
        return stub.scanDocument(Service.ScanDocumentRequest.newBuilder()
                .setImageJpeg(imgData)
                .setConfig(cfg)
                .build());
    }

}
