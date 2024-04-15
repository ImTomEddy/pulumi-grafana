// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace Pulumiverse.Grafana.Outputs
{

    [OutputType]
    public sealed class ContactPointThreema
    {
        /// <summary>
        /// The Threema API key.
        /// </summary>
        public readonly string ApiSecret;
        /// <summary>
        /// The templated description of the message.
        /// </summary>
        public readonly string? Description;
        /// <summary>
        /// Whether to disable sending resolve messages.
        /// </summary>
        public readonly bool? DisableResolveMessage;
        /// <summary>
        /// The Threema gateway ID.
        /// </summary>
        public readonly string GatewayId;
        /// <summary>
        /// The ID of the recipient of the message.
        /// </summary>
        public readonly string RecipientId;
        /// <summary>
        /// Additional custom properties to attach to the notifier.
        /// </summary>
        public readonly ImmutableDictionary<string, string>? Settings;
        /// <summary>
        /// The templated title of the message.
        /// </summary>
        public readonly string? Title;
        /// <summary>
        /// The UID of the contact point.
        /// </summary>
        public readonly string? Uid;

        [OutputConstructor]
        private ContactPointThreema(
            string apiSecret,

            string? description,

            bool? disableResolveMessage,

            string gatewayId,

            string recipientId,

            ImmutableDictionary<string, string>? settings,

            string? title,

            string? uid)
        {
            ApiSecret = apiSecret;
            Description = description;
            DisableResolveMessage = disableResolveMessage;
            GatewayId = gatewayId;
            RecipientId = recipientId;
            Settings = settings;
            Title = title;
            Uid = uid;
        }
    }
}
