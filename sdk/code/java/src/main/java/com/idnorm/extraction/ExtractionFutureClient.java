package com.idnorm.extraction;

import com.google.protobuf.ByteString;
import com.google.common.util.concurrent.ListenableFuture;
import proto.ddx.v1.ExtractionGrpc;
import proto.ddx.v1.Service;

public class ExtractionFutureClient {

    private final ExtractionGrpc.ExtractionFutureStub stub;

    protected ExtractionFutureClient(ExtractionGrpc.ExtractionFutureStub stub) {
        this.stub = stub;
    }

    public static ExtractionClientBuilder<ExtractionFutureClient> builder() {
        return new ExtractionClientBuilder<>(c -> new ExtractionFutureClient(ExtractionGrpc.newFutureStub(c)));
    }

    public ListenableFuture<Service.ScanDocumentResponse> scanDocument(ByteString imgData) {
        return stub.scanDocument(Service.ScanDocumentRequest.newBuilder()
                .setImageJpeg(imgData)
                .build());
    }

    public ListenableFuture<Service.ScanDocumentResponse> scanDocument(ByteString imgData, Service.ScanConfig cfg) {
        return stub.scanDocument(Service.ScanDocumentRequest.newBuilder()
                .setImageJpeg(imgData)
                .setConfig(cfg)
                .build());
    }

}
