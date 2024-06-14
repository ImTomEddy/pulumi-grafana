// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace Pulumiverse.Grafana.SyntheticMonitoring.Inputs
{

    public sealed class CheckSettingsHttpArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Basic auth settings.
        /// </summary>
        [Input("basicAuth")]
        public Input<Inputs.CheckSettingsHttpBasicAuthArgs>? BasicAuth { get; set; }

        /// <summary>
        /// Token for use with bearer authorization header.
        /// </summary>
        [Input("bearerToken")]
        public Input<string>? BearerToken { get; set; }

        /// <summary>
        /// The body of the HTTP request used in probe.
        /// </summary>
        [Input("body")]
        public Input<string>? Body { get; set; }

        /// <summary>
        /// The name of the query parameter used to prevent the server from using a cached response. Each probe will assign a random value to this parameter each time a request is made.
        /// </summary>
        [Input("cacheBustingQueryParamName")]
        public Input<string>? CacheBustingQueryParamName { get; set; }

        [Input("failIfBodyMatchesRegexps")]
        private InputList<string>? _failIfBodyMatchesRegexps;

        /// <summary>
        /// List of regexes. If any match the response body, the check will fail.
        /// </summary>
        public InputList<string> FailIfBodyMatchesRegexps
        {
            get => _failIfBodyMatchesRegexps ?? (_failIfBodyMatchesRegexps = new InputList<string>());
            set => _failIfBodyMatchesRegexps = value;
        }

        [Input("failIfBodyNotMatchesRegexps")]
        private InputList<string>? _failIfBodyNotMatchesRegexps;

        /// <summary>
        /// List of regexes. If any do not match the response body, the check will fail.
        /// </summary>
        public InputList<string> FailIfBodyNotMatchesRegexps
        {
            get => _failIfBodyNotMatchesRegexps ?? (_failIfBodyNotMatchesRegexps = new InputList<string>());
            set => _failIfBodyNotMatchesRegexps = value;
        }

        [Input("failIfHeaderMatchesRegexps")]
        private InputList<Inputs.CheckSettingsHttpFailIfHeaderMatchesRegexpArgs>? _failIfHeaderMatchesRegexps;

        /// <summary>
        /// Check fails if headers match.
        /// </summary>
        public InputList<Inputs.CheckSettingsHttpFailIfHeaderMatchesRegexpArgs> FailIfHeaderMatchesRegexps
        {
            get => _failIfHeaderMatchesRegexps ?? (_failIfHeaderMatchesRegexps = new InputList<Inputs.CheckSettingsHttpFailIfHeaderMatchesRegexpArgs>());
            set => _failIfHeaderMatchesRegexps = value;
        }

        [Input("failIfHeaderNotMatchesRegexps")]
        private InputList<Inputs.CheckSettingsHttpFailIfHeaderNotMatchesRegexpArgs>? _failIfHeaderNotMatchesRegexps;

        /// <summary>
        /// Check fails if headers do not match.
        /// </summary>
        public InputList<Inputs.CheckSettingsHttpFailIfHeaderNotMatchesRegexpArgs> FailIfHeaderNotMatchesRegexps
        {
            get => _failIfHeaderNotMatchesRegexps ?? (_failIfHeaderNotMatchesRegexps = new InputList<Inputs.CheckSettingsHttpFailIfHeaderNotMatchesRegexpArgs>());
            set => _failIfHeaderNotMatchesRegexps = value;
        }

        /// <summary>
        /// Fail if SSL is not present. Defaults to `false`.
        /// </summary>
        [Input("failIfNotSsl")]
        public Input<bool>? FailIfNotSsl { get; set; }

        /// <summary>
        /// Fail if SSL is present. Defaults to `false`.
        /// </summary>
        [Input("failIfSsl")]
        public Input<bool>? FailIfSsl { get; set; }

        [Input("headers")]
        private InputList<string>? _headers;

        /// <summary>
        /// The HTTP headers set for the probe.
        /// </summary>
        public InputList<string> Headers
        {
            get => _headers ?? (_headers = new InputList<string>());
            set => _headers = value;
        }

        /// <summary>
        /// Options are `V4`, `V6`, `Any`. Specifies whether the corresponding check will be performed using IPv4 or IPv6. The `Any` value indicates that IPv6 should be used, falling back to IPv4 if that's not available. Defaults to `V4`.
        /// </summary>
        [Input("ipVersion")]
        public Input<string>? IpVersion { get; set; }

        /// <summary>
        /// Request method. One of `GET`, `CONNECT`, `DELETE`, `HEAD`, `OPTIONS`, `POST`, `PUT`, `TRACE` Defaults to `GET`.
        /// </summary>
        [Input("method")]
        public Input<string>? Method { get; set; }

        /// <summary>
        /// Do not follow redirects. Defaults to `false`.
        /// </summary>
        [Input("noFollowRedirects")]
        public Input<bool>? NoFollowRedirects { get; set; }

        [Input("proxyConnectHeaders")]
        private InputList<string>? _proxyConnectHeaders;

        /// <summary>
        /// The HTTP headers sent to the proxy URL
        /// </summary>
        public InputList<string> ProxyConnectHeaders
        {
            get => _proxyConnectHeaders ?? (_proxyConnectHeaders = new InputList<string>());
            set => _proxyConnectHeaders = value;
        }

        /// <summary>
        /// Proxy URL.
        /// </summary>
        [Input("proxyUrl")]
        public Input<string>? ProxyUrl { get; set; }

        /// <summary>
        /// TLS config.
        /// </summary>
        [Input("tlsConfig")]
        public Input<Inputs.CheckSettingsHttpTlsConfigArgs>? TlsConfig { get; set; }

        [Input("validHttpVersions")]
        private InputList<string>? _validHttpVersions;

        /// <summary>
        /// List of valid HTTP versions. Options include `HTTP/1.0`, `HTTP/1.1`, `HTTP/2.0`
        /// </summary>
        public InputList<string> ValidHttpVersions
        {
            get => _validHttpVersions ?? (_validHttpVersions = new InputList<string>());
            set => _validHttpVersions = value;
        }

        [Input("validStatusCodes")]
        private InputList<int>? _validStatusCodes;

        /// <summary>
        /// Accepted status codes. If unset, defaults to 2xx.
        /// </summary>
        public InputList<int> ValidStatusCodes
        {
            get => _validStatusCodes ?? (_validStatusCodes = new InputList<int>());
            set => _validStatusCodes = value;
        }

        public CheckSettingsHttpArgs()
        {
        }
        public static new CheckSettingsHttpArgs Empty => new CheckSettingsHttpArgs();
    }
}
