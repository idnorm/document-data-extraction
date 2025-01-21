package com.idnorm.extraction;

import io.grpc.Channel;
import io.grpc.ClientInterceptors;
import io.grpc.ManagedChannelBuilder;
import io.grpc.Metadata;
import io.grpc.stub.MetadataUtils;

public class ExtractionClientBuilder<T> {

    final private static String CLOUD_SERVICE_URL = "ddx.idnorm.com:443";
    final private static String LICENSE_KEY_HEADER = "vdil-license-key";

    private final Config config;
    private final StubFn<T> stubFn;

    protected interface StubFn<T> {
        T create(io.grpc.Channel channel);
    }

    protected ExtractionClientBuilder(StubFn<T> stubFn) {
        this.stubFn = stubFn;
        this.config = new Config();
        this.config.url = CLOUD_SERVICE_URL;
        this.config.isSecure = true;
    }

    public static class Config {
        public String url;
        public boolean isSecure;
        public String licenseKey;
    }

    private static class Host {
        public String host;
        public int port;
    }

    private Host parseUrl(String url) {
        String[] parts = url.split(":");
        if (parts.length != 2) {
            throw new IllegalArgumentException("url should be in format hostname:port. Got: " + url);
        }
        Host host = new Host();
        host.host = parts[0];
        host.port = Integer.parseInt(parts[1]);
        return host;
    }

    private Channel buildChannel() {
        var host = parseUrl(this.config.url);
        var builder = ManagedChannelBuilder.forAddress(host.host, host.port);

        if (config.isSecure || host.port == 443) {
            builder.useTransportSecurity();
        } else {
            builder.usePlaintext();
        }

        var channel = builder.build();

        Metadata headers = new Metadata();
        Metadata.Key<String> licenseKey = Metadata.Key.of(LICENSE_KEY_HEADER, Metadata.ASCII_STRING_MARSHALLER);
        headers.put(licenseKey, config.licenseKey);

        var interceptor = MetadataUtils.newAttachHeadersInterceptor(headers);

        return ClientInterceptors.intercept(channel, interceptor);
    }

    public ExtractionClientBuilder<T> setLicenseKey(String licenseKey) {
        this.config.licenseKey = licenseKey;
        return this;
    }

    public ExtractionClientBuilder<T> setUrl(String url) {
        this.config.url = url;
        return this;
    }

    public ExtractionClientBuilder<T> setSecure(boolean isSecure) {
        this.config.isSecure = isSecure;
        return this;
    }

    private void checkConfig() {
        if (this.config.licenseKey == null || this.config.licenseKey.isEmpty()) {
            throw new IllegalStateException("License key is not set");
        }
    }

    public T build() {
        this.checkConfig();
        return this.stubFn.create(buildChannel());
    }

}