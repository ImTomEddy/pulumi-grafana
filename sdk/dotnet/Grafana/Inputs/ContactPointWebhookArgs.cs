// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace Lbrlabs.PulumiPackage.Grafana.Inputs
{

    public sealed class ContactPointWebhookArgs : global::Pulumi.ResourceArgs
    {
        [Input("authorizationCredentials")]
        private Input<string>? _authorizationCredentials;

        /// <summary>
        /// Allows a custom authorization scheme - attaches an auth header with this value. Do not use in conjunction with basic auth parameters.
        /// </summary>
        public Input<string>? AuthorizationCredentials
        {
            get => _authorizationCredentials;
            set
            {
                var emptySecret = Output.CreateSecret(0);
                _authorizationCredentials = Output.Tuple<Input<string>?, int>(value, emptySecret).Apply(t => t.Item1);
            }
        }

        /// <summary>
        /// Allows a custom authorization scheme - attaches an auth header with this name. Do not use in conjunction with basic auth parameters.
        /// </summary>
        [Input("authorizationScheme")]
        public Input<string>? AuthorizationScheme { get; set; }

        [Input("basicAuthPassword")]
        private Input<string>? _basicAuthPassword;

        /// <summary>
        /// The username to use in basic auth headers attached to the request. If omitted, basic auth will not be used.
        /// </summary>
        public Input<string>? BasicAuthPassword
        {
            get => _basicAuthPassword;
            set
            {
                var emptySecret = Output.CreateSecret(0);
                _basicAuthPassword = Output.Tuple<Input<string>?, int>(value, emptySecret).Apply(t => t.Item1);
            }
        }

        /// <summary>
        /// The username to use in basic auth headers attached to the request. If omitted, basic auth will not be used.
        /// </summary>
        [Input("basicAuthUser")]
        public Input<string>? BasicAuthUser { get; set; }

        /// <summary>
        /// Whether to disable sending resolve messages. Defaults to `false`.
        /// </summary>
        [Input("disableResolveMessage")]
        public Input<bool>? DisableResolveMessage { get; set; }

        /// <summary>
        /// The HTTP method to use in the request. Defaults to `POST`.
        /// </summary>
        [Input("httpMethod")]
        public Input<string>? HttpMethod { get; set; }

        /// <summary>
        /// The maximum number of alerts to send in a single request. This can be helpful in limiting the size of the request body. The default is 0, which indicates no limit.
        /// </summary>
        [Input("maxAlerts")]
        public Input<int>? MaxAlerts { get; set; }

        /// <summary>
        /// Custom message. You can use template variables.
        /// </summary>
        [Input("message")]
        public Input<string>? Message { get; set; }

        [Input("settings")]
        private InputMap<string>? _settings;

        /// <summary>
        /// Additional custom properties to attach to the notifier. Defaults to `map[]`.
        /// </summary>
        public InputMap<string> Settings
        {
            get => _settings ?? (_settings = new InputMap<string>());
            set
            {
                var emptySecret = Output.CreateSecret(ImmutableDictionary.Create<string, string>());
                _settings = Output.All(value, emptySecret).Apply(v => v[0]);
            }
        }

        /// <summary>
        /// Templated title of the message.
        /// </summary>
        [Input("title")]
        public Input<string>? Title { get; set; }

        /// <summary>
        /// The UID of the contact point.
        /// </summary>
        [Input("uid")]
        public Input<string>? Uid { get; set; }

        /// <summary>
        /// The URL to send webhook requests to.
        /// </summary>
        [Input("url", required: true)]
        public Input<string> Url { get; set; } = null!;

        public ContactPointWebhookArgs()
        {
        }
        public static new ContactPointWebhookArgs Empty => new ContactPointWebhookArgs();
    }
}
