// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.grafana.inputs;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import java.lang.String;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class DataSourceSecureJsonDataArgs extends com.pulumi.resources.ResourceArgs {

    public static final DataSourceSecureJsonDataArgs Empty = new DataSourceSecureJsonDataArgs();

    /**
     * (CloudWatch, Athena) The access key used to access the data source.
     * 
     */
    @Import(name="accessKey")
    private @Nullable Output<String> accessKey;

    /**
     * @return (CloudWatch, Athena) The access key used to access the data source.
     * 
     */
    public Optional<Output<String>> accessKey() {
        return Optional.ofNullable(this.accessKey);
    }

    /**
     * (Github) The access token used to access the data source.
     * 
     */
    @Import(name="accessToken")
    private @Nullable Output<String> accessToken;

    /**
     * @return (Github) The access token used to access the data source.
     * 
     */
    public Optional<Output<String>> accessToken() {
        return Optional.ofNullable(this.accessToken);
    }

    /**
     * (Sentry) Authorization token.
     * 
     */
    @Import(name="authToken")
    private @Nullable Output<String> authToken;

    /**
     * @return (Sentry) Authorization token.
     * 
     */
    public Optional<Output<String>> authToken() {
        return Optional.ofNullable(this.authToken);
    }

    /**
     * (All) Password to use for basic authentication.
     * 
     */
    @Import(name="basicAuthPassword")
    private @Nullable Output<String> basicAuthPassword;

    /**
     * @return (All) Password to use for basic authentication.
     * 
     */
    public Optional<Output<String>> basicAuthPassword() {
        return Optional.ofNullable(this.basicAuthPassword);
    }

    /**
     * (Azure Monitor) Client secret for authentication.
     * 
     */
    @Import(name="clientSecret")
    private @Nullable Output<String> clientSecret;

    /**
     * @return (Azure Monitor) Client secret for authentication.
     * 
     */
    public Optional<Output<String>> clientSecret() {
        return Optional.ofNullable(this.clientSecret);
    }

    /**
     * (All) Password to use for authentication.
     * 
     */
    @Import(name="password")
    private @Nullable Output<String> password;

    /**
     * @return (All) Password to use for authentication.
     * 
     */
    public Optional<Output<String>> password() {
        return Optional.ofNullable(this.password);
    }

    /**
     * (Stackdriver) The service account key `private_key` to use to access the data source.
     * 
     */
    @Import(name="privateKey")
    private @Nullable Output<String> privateKey;

    /**
     * @return (Stackdriver) The service account key `private_key` to use to access the data source.
     * 
     */
    public Optional<Output<String>> privateKey() {
        return Optional.ofNullable(this.privateKey);
    }

    /**
     * (CloudWatch, Athena) The secret key to use to access the data source.
     * 
     */
    @Import(name="secretKey")
    private @Nullable Output<String> secretKey;

    /**
     * @return (CloudWatch, Athena) The secret key to use to access the data source.
     * 
     */
    public Optional<Output<String>> secretKey() {
        return Optional.ofNullable(this.secretKey);
    }

    /**
     * (Elasticsearch and Prometheus) SigV4 access key. Required when using &#39;keys&#39; auth provider.
     * 
     */
    @Import(name="sigv4AccessKey")
    private @Nullable Output<String> sigv4AccessKey;

    /**
     * @return (Elasticsearch and Prometheus) SigV4 access key. Required when using &#39;keys&#39; auth provider.
     * 
     */
    public Optional<Output<String>> sigv4AccessKey() {
        return Optional.ofNullable(this.sigv4AccessKey);
    }

    /**
     * (Elasticsearch and Prometheus) SigV4 secret key. Required when using &#39;keys&#39; auth provider.
     * 
     */
    @Import(name="sigv4SecretKey")
    private @Nullable Output<String> sigv4SecretKey;

    /**
     * @return (Elasticsearch and Prometheus) SigV4 secret key. Required when using &#39;keys&#39; auth provider.
     * 
     */
    public Optional<Output<String>> sigv4SecretKey() {
        return Optional.ofNullable(this.sigv4SecretKey);
    }

    /**
     * (All) CA cert for out going requests.
     * 
     */
    @Import(name="tlsCaCert")
    private @Nullable Output<String> tlsCaCert;

    /**
     * @return (All) CA cert for out going requests.
     * 
     */
    public Optional<Output<String>> tlsCaCert() {
        return Optional.ofNullable(this.tlsCaCert);
    }

    /**
     * (All) TLS Client cert for outgoing requests.
     * 
     */
    @Import(name="tlsClientCert")
    private @Nullable Output<String> tlsClientCert;

    /**
     * @return (All) TLS Client cert for outgoing requests.
     * 
     */
    public Optional<Output<String>> tlsClientCert() {
        return Optional.ofNullable(this.tlsClientCert);
    }

    /**
     * (All) TLS Client key for outgoing requests.
     * 
     */
    @Import(name="tlsClientKey")
    private @Nullable Output<String> tlsClientKey;

    /**
     * @return (All) TLS Client key for outgoing requests.
     * 
     */
    public Optional<Output<String>> tlsClientKey() {
        return Optional.ofNullable(this.tlsClientKey);
    }

    private DataSourceSecureJsonDataArgs() {}

    private DataSourceSecureJsonDataArgs(DataSourceSecureJsonDataArgs $) {
        this.accessKey = $.accessKey;
        this.accessToken = $.accessToken;
        this.authToken = $.authToken;
        this.basicAuthPassword = $.basicAuthPassword;
        this.clientSecret = $.clientSecret;
        this.password = $.password;
        this.privateKey = $.privateKey;
        this.secretKey = $.secretKey;
        this.sigv4AccessKey = $.sigv4AccessKey;
        this.sigv4SecretKey = $.sigv4SecretKey;
        this.tlsCaCert = $.tlsCaCert;
        this.tlsClientCert = $.tlsClientCert;
        this.tlsClientKey = $.tlsClientKey;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(DataSourceSecureJsonDataArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private DataSourceSecureJsonDataArgs $;

        public Builder() {
            $ = new DataSourceSecureJsonDataArgs();
        }

        public Builder(DataSourceSecureJsonDataArgs defaults) {
            $ = new DataSourceSecureJsonDataArgs(Objects.requireNonNull(defaults));
        }

        /**
         * @param accessKey (CloudWatch, Athena) The access key used to access the data source.
         * 
         * @return builder
         * 
         */
        public Builder accessKey(@Nullable Output<String> accessKey) {
            $.accessKey = accessKey;
            return this;
        }

        /**
         * @param accessKey (CloudWatch, Athena) The access key used to access the data source.
         * 
         * @return builder
         * 
         */
        public Builder accessKey(String accessKey) {
            return accessKey(Output.of(accessKey));
        }

        /**
         * @param accessToken (Github) The access token used to access the data source.
         * 
         * @return builder
         * 
         */
        public Builder accessToken(@Nullable Output<String> accessToken) {
            $.accessToken = accessToken;
            return this;
        }

        /**
         * @param accessToken (Github) The access token used to access the data source.
         * 
         * @return builder
         * 
         */
        public Builder accessToken(String accessToken) {
            return accessToken(Output.of(accessToken));
        }

        /**
         * @param authToken (Sentry) Authorization token.
         * 
         * @return builder
         * 
         */
        public Builder authToken(@Nullable Output<String> authToken) {
            $.authToken = authToken;
            return this;
        }

        /**
         * @param authToken (Sentry) Authorization token.
         * 
         * @return builder
         * 
         */
        public Builder authToken(String authToken) {
            return authToken(Output.of(authToken));
        }

        /**
         * @param basicAuthPassword (All) Password to use for basic authentication.
         * 
         * @return builder
         * 
         */
        public Builder basicAuthPassword(@Nullable Output<String> basicAuthPassword) {
            $.basicAuthPassword = basicAuthPassword;
            return this;
        }

        /**
         * @param basicAuthPassword (All) Password to use for basic authentication.
         * 
         * @return builder
         * 
         */
        public Builder basicAuthPassword(String basicAuthPassword) {
            return basicAuthPassword(Output.of(basicAuthPassword));
        }

        /**
         * @param clientSecret (Azure Monitor) Client secret for authentication.
         * 
         * @return builder
         * 
         */
        public Builder clientSecret(@Nullable Output<String> clientSecret) {
            $.clientSecret = clientSecret;
            return this;
        }

        /**
         * @param clientSecret (Azure Monitor) Client secret for authentication.
         * 
         * @return builder
         * 
         */
        public Builder clientSecret(String clientSecret) {
            return clientSecret(Output.of(clientSecret));
        }

        /**
         * @param password (All) Password to use for authentication.
         * 
         * @return builder
         * 
         */
        public Builder password(@Nullable Output<String> password) {
            $.password = password;
            return this;
        }

        /**
         * @param password (All) Password to use for authentication.
         * 
         * @return builder
         * 
         */
        public Builder password(String password) {
            return password(Output.of(password));
        }

        /**
         * @param privateKey (Stackdriver) The service account key `private_key` to use to access the data source.
         * 
         * @return builder
         * 
         */
        public Builder privateKey(@Nullable Output<String> privateKey) {
            $.privateKey = privateKey;
            return this;
        }

        /**
         * @param privateKey (Stackdriver) The service account key `private_key` to use to access the data source.
         * 
         * @return builder
         * 
         */
        public Builder privateKey(String privateKey) {
            return privateKey(Output.of(privateKey));
        }

        /**
         * @param secretKey (CloudWatch, Athena) The secret key to use to access the data source.
         * 
         * @return builder
         * 
         */
        public Builder secretKey(@Nullable Output<String> secretKey) {
            $.secretKey = secretKey;
            return this;
        }

        /**
         * @param secretKey (CloudWatch, Athena) The secret key to use to access the data source.
         * 
         * @return builder
         * 
         */
        public Builder secretKey(String secretKey) {
            return secretKey(Output.of(secretKey));
        }

        /**
         * @param sigv4AccessKey (Elasticsearch and Prometheus) SigV4 access key. Required when using &#39;keys&#39; auth provider.
         * 
         * @return builder
         * 
         */
        public Builder sigv4AccessKey(@Nullable Output<String> sigv4AccessKey) {
            $.sigv4AccessKey = sigv4AccessKey;
            return this;
        }

        /**
         * @param sigv4AccessKey (Elasticsearch and Prometheus) SigV4 access key. Required when using &#39;keys&#39; auth provider.
         * 
         * @return builder
         * 
         */
        public Builder sigv4AccessKey(String sigv4AccessKey) {
            return sigv4AccessKey(Output.of(sigv4AccessKey));
        }

        /**
         * @param sigv4SecretKey (Elasticsearch and Prometheus) SigV4 secret key. Required when using &#39;keys&#39; auth provider.
         * 
         * @return builder
         * 
         */
        public Builder sigv4SecretKey(@Nullable Output<String> sigv4SecretKey) {
            $.sigv4SecretKey = sigv4SecretKey;
            return this;
        }

        /**
         * @param sigv4SecretKey (Elasticsearch and Prometheus) SigV4 secret key. Required when using &#39;keys&#39; auth provider.
         * 
         * @return builder
         * 
         */
        public Builder sigv4SecretKey(String sigv4SecretKey) {
            return sigv4SecretKey(Output.of(sigv4SecretKey));
        }

        /**
         * @param tlsCaCert (All) CA cert for out going requests.
         * 
         * @return builder
         * 
         */
        public Builder tlsCaCert(@Nullable Output<String> tlsCaCert) {
            $.tlsCaCert = tlsCaCert;
            return this;
        }

        /**
         * @param tlsCaCert (All) CA cert for out going requests.
         * 
         * @return builder
         * 
         */
        public Builder tlsCaCert(String tlsCaCert) {
            return tlsCaCert(Output.of(tlsCaCert));
        }

        /**
         * @param tlsClientCert (All) TLS Client cert for outgoing requests.
         * 
         * @return builder
         * 
         */
        public Builder tlsClientCert(@Nullable Output<String> tlsClientCert) {
            $.tlsClientCert = tlsClientCert;
            return this;
        }

        /**
         * @param tlsClientCert (All) TLS Client cert for outgoing requests.
         * 
         * @return builder
         * 
         */
        public Builder tlsClientCert(String tlsClientCert) {
            return tlsClientCert(Output.of(tlsClientCert));
        }

        /**
         * @param tlsClientKey (All) TLS Client key for outgoing requests.
         * 
         * @return builder
         * 
         */
        public Builder tlsClientKey(@Nullable Output<String> tlsClientKey) {
            $.tlsClientKey = tlsClientKey;
            return this;
        }

        /**
         * @param tlsClientKey (All) TLS Client key for outgoing requests.
         * 
         * @return builder
         * 
         */
        public Builder tlsClientKey(String tlsClientKey) {
            return tlsClientKey(Output.of(tlsClientKey));
        }

        public DataSourceSecureJsonDataArgs build() {
            return $;
        }
    }

}